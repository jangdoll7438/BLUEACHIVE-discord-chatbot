import discord
import openai
import time
import re
import asyncio
import threading
import requests
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

MIYU_TOKEN = os.environ.get('MIYU_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
openai.api_key = os.environ.get('OPENAI_API_KEY')
ASSISTANT_ID = os.environ.get('ASSISTANT_ID')

image_path = {
  'miyu': {
    'happy': 'images/miyu_happy.png',
    'neutral': 'images/miyu_neutral.png',
    'sad': 'images/miyu_sad.png',
    'panic': 'images/miyu_panic.png'
  },
}

history = []

def parse_conversations(input_text):
  data = []
  pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')
  matches = pattern.findall(input_text)

  for match in matches:
    sentiment, speaker, text = match
    entry = {
      "speaker": speaker,
      "sentiment": sentiment,
      "text": remove_tags(text)
    }
    data.append(entry)

  return data

def remove_tags(text):
  if text[0] == '"' and text[-1] == '"':
    text = text[1:-1]
  cleaned_text = re.sub(r'【.*?】', '', text)
  return cleaned_text

def wait_on_run(run, thread):
  while run.status == "queued" or run.status == "in_progress":
    run = openai.beta.threads.runs.retrieve(
      thread_id=thread.id,
      run_id=run.id,
    )
    time.sleep(0.5)
  return run

async def get_response(text, type="chat", url=None):
  global history
  if type == "chat":
    history.append({"role": "user", "content": text, "image_path": None})
  elif type == "image":
    history.append({"role": "user", "content": text, "image_path": url})
  thread = openai.beta.threads.create()
  for entry in history:
    if entry.get("image_path") is None:
      openai.beta.threads.messages.create(
        thread_id=thread.id,
        role=entry["role"],
        content=[{
          "type": "text",
          "text": entry["content"]
        }]
      )
    else:
      openai.beta.threads.messages.create(
        thread_id=thread.id,
        role=entry["role"],
        content=[{
          "type": "text",
          "text": entry["content"]
        }, {
          "type": "image_url",
          "image_url": {"url": entry["image_path"]},
        }]
      )
  run = openai.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
  )
  run = wait_on_run(run, thread)
  messages = openai.beta.threads.messages.list(thread_id=thread.id)
  history.append({"role": "assistant", "content": messages.data[0].content[0].text.value})
  if len(history) > 20:
    history = history[-20:]
  return parse_conversations(messages.data[0].content[0].text.value)

 
class MiyuClient(discord.Client):
  async def on_ready(self):
    self.channel = self.get_channel(int(CHANNEL_ID))
    self.loading = False
  
  async def on_message(self, message):
    if message.author.bot:
      return
    if message.channel != self.channel:
      return
    if self.loading:
      return
    if message.attachments:
      for attachment in message.attachments:
        t = attachment.url
        self.loading = True
        async with message.channel.typing():
          text = "선생님이 사진을 보냈습니다."
          if message.content.strip():
            text += f"\n선생님: {message.content}"
          response = await get_response(text, type="image", url=attachment.url)
        for i in range(len(response)):
          if response[i]['speaker'] == '미유':
            await self.send_message(response[i]['text'], response[i]['sentiment'])
          await asyncio.sleep(1)
        self.loading = False
        return
    t = message.content.strip()
    self.loading = True
    async with message.channel.typing():
      t = f"선생님: {t}"
      response = await get_response(t)
    for i in range(len(response)):
      if response[i]['speaker'] == '미유':
        await self.send_message(response[i]['text'], response[i]['sentiment'])
      await asyncio.sleep(1)
    self.loading = False
  
  async def send_message(self, text, sentiment):
    if sentiment == '기쁨':
      file = discord.File(image_path['miyu']['happy'])
    elif sentiment == '당황':
      file = discord.File(image_path['miyu']['panic'])
    elif sentiment == '슬픔':
      file = discord.File(image_path['miyu']['sad'])
    else:
      file = discord.File(image_path['miyu']['neutral'])
    await self.channel.send(file=file)
    await self.channel.send(content=text)

assistant = openai.beta.assistants.retrieve(
  assistant_id=ASSISTANT_ID
)

miyu_intents = discord.Intents.default()
miyu_intents.message_content = True
miyu_client = MiyuClient(intents=miyu_intents)

async def logout_and_stop():
  await miyu_client.close()

async def run_bots():
  await asyncio.gather(
    miyu_client.start(MIYU_TOKEN),
  )

def stop_bots(loop):
    print("Logging out...")
    asyncio.run_coroutine_threadsafe(logout_and_stop(), loop)

def wait_for_enter(loop):
    input("Press Enter to stop the bots...\n")
    stop_bots(loop)

loop = asyncio.get_event_loop()

thread = threading.Thread(target=wait_for_enter, args=(loop,))
thread.start()

loop.run_until_complete(run_bots())
