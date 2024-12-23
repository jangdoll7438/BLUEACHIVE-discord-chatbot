## 🙌 Blue Archive Discord Chat Bot
![dwdw](https://github.com/user-attachments/assets/12bce50b-a2c5-4199-856a-3124260ad9d2)   

## ❓ what is this?
- 넥슨의 게임 블루아카이브에 등장하는 카스미자와 미유라는 캐릭터를 디스코드 챗봇으로 제작하여 대화 할 수 있습니다.  
- Open Ai 챗봇을 기반으로 제작하여 사용자와 다양한 대화가 가능하고, 대답에 따라 사진이 변경됩니다.
- 사용을 위해 아래의 세팅 설명을 따라 주세요. 

## 🙋‍♀️ Setting 
1. https://discord.com/developers/docs/intro 디스코드 개발자 포털 접속 후 Applications 클릭.
![1](https://github.com/user-attachments/assets/b033133d-2a37-4cbd-b85b-b58fcdd0e3e4)


2. New Applications 클릭 후 이름 설정

![3](https://github.com/user-attachments/assets/d8fcbf62-3f91-43fd-92ad-afe03e3974c9)   

3. 프로필 사진 설정과 설명 작성

![image](https://github.com/user-attachments/assets/ecbdde16-e8bc-4c3e-9909-5e401767aefa) 
4. OAuth2 탭에서 bot 체크 후 Send Message 체크

![image](https://github.com/user-attachments/assets/199eda7f-3fc0-4719-9d81-3ad139dd3de2)   
![image](https://github.com/user-attachments/assets/4c04be7b-3edd-4b7e-ae58-44ece852c5bf)
5. 아래의 URL을 통해 접속 후 원하는 디스코드 서버에 미유 봇을 초대한다.

![image](https://github.com/user-attachments/assets/ad68be53-f173-40ad-9599-17b7b30a66bb)
![image](https://github.com/user-attachments/assets/46a32245-0c0d-4385-96fa-1d35d75fb96b)

6.Bot 탭에서 Reset 토큰 클릭 후 토큰을 복사 후 다른 곳에 저장해 놓는다. (한번만 보여주기 때문, 추후에 사용해야 함.)
![image](https://github.com/user-attachments/assets/d5caf40d-7092-47e3-8cd8-f115e8faee99)
![image](https://github.com/user-attachments/assets/8fa6d17b-0a45-400d-baaf-6ed964e666cb)

7.Open Ai Playground 접속 (https://platform.openai.com/playground/chat?models=gpt-4o)
Assistant에서 finish account set up 클릭 후 소액 결제하여 챗봇 활성화.
![image](https://github.com/user-attachments/assets/9e18ea76-0a6b-4dfa-a53e-5e6309af916b)



8.Assistant로 돌아와 create 후 코드 복사
![image](https://github.com/user-attachments/assets/24e355c7-fd7b-4e49-a5f9-4a4115bef9ae)

9.system instructons에 prompt.txt에 있는 텍스트를 붙여넣는다.
![image](https://github.com/user-attachments/assets/c75ae407-d2e0-4706-a9d0-aba89db16175)

10. file search를 활성화하고 miyu.txt를 드래그 앤 드롭
![image](https://github.com/user-attachments/assets/fcabfe57-573b-4136-a34c-2d1a374c3f1c)

11. discord 개발자 모드 활성화 후  챗봇과 대화하고자하는 채널의 채널 id 복사
![image](https://github.com/user-attachments/assets/d347a94e-3605-4b36-8771-658e6768a44b)
![image](https://github.com/user-attachments/assets/985c0b00-723e-41ad-a209-28950b23db58)

## 🛠 기능 엿보기   

1. [❓ EASYME.md가 뭐예요?  ](#-easymemd가-뭐예요)
2. [🙋‍♀️ 좀 더 구체적으로 가르쳐주세요!](#-좀-더-구체적으로-가르쳐주세요)
3. [🛠 기능 엿보기](#-기능-엿보기)
    - [Header](#header)   
    - [Text Style1](#text-style1)   
    - [Text Stlye2](#text-style2)   
    - [List](#list)      
    - [Link](#link)   
    - [Code Block](#code-block)   
    - [Table](#table)   
   
## Header
- # H1 Header   
- ## H2 Header   
- ### H3 Header   
- #### H4 Header   
- ##### H5 Header   
- ###### H6 Header   

<br>   

## Text Style1
- **진하게** (`Ctrl(Command) + B`)   
- *기울이기* (`Ctrl(Command) + I`)   
- <s>취소선</s> (`Ctrl(Command) + D`)   
- <u>밑줄</u> (`Ctrl(Command) + U`)   

<br>   
   
## Text Style2

>인용문   
   
<details><summary>접고 펴는 기능
</summary>

*Write here!*
</details>

- EASYME.md를 드래그하고 상단에 `Aa` 아이콘을 누르면? 👉 Easyme.md   
- EASYME.md를 드래그하고 상단에 `A` 아이콘을 누르면? 👉 EASYME.MD   
- EASYME.md를 드래그하고 상단에 `a` 아이콘을 누르면? 👉 easyme.md   
   
<br>   
   
## List   
### Table of contents
1. [title1](#write-title-here!)   
2. [title2](#only-lowercase)   
3. [title3](#use"-"instead-of-spacing-words)   
4. [title4](#example)   
    - [❓ EASYME.md가 뭐예요?](#-easymemd가-뭐예요)   
    - [🛠 기능 엿보기](#-기능-엿보기)
   
### Unordered list   
- unordered list1   
- unordered list2   
- unordered list3   
- unordered list4   
   
### Ordered list   
1. ordered list1   
2. ordered list2   
3. ordered list3   
4. ordered list4   
   
<br>   
   
## Link   
### General link
- [🚗 Visit EASYME.md's Repo](https://github.com/EASYME-md/client)   
- [🙋‍♂️ Visit ONE:A's Github](https://github.com/onealog)

### Image link
![onealog](/assets/readme/easyme.png)   
   
<br>   
   
## Code Block   
### Code inline
- `console.log('Hello EASYME.md!');`   
   
### Code block
```js
function makeDeveloper(name, language) {
  if (name === 'ONE:A' && language === 'JavaScript') {
    return 'perfect!';
  }

  return false;
}

makeDeveloper('ONE:A', 'JavaScript');
```

<br>   
   
## Table   


| title1 | title2 | title3 |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |


<br>   

