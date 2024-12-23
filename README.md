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

12.API reference -> ApI kets -> create new secret keys
![image](https://github.com/user-attachments/assets/c5ec4095-2066-4de9-997e-74baa350bf0e)

13.default project 선택 후 key 복사

![image](https://github.com/user-attachments/assets/d873e652-ed81-43fc-baf0-62861a93e0bf)

![image](https://github.com/user-attachments/assets/ff4d5fd9-6b5d-4a18-86b2-6744b946f56f)

14.소스 코드 폴더에 ".env"라는 텍스트 파일 생성 후 해당 파일에 다음과 같이 작성

![image](https://github.com/user-attachments/assets/1dacac1c-a5eb-4c14-8eac-12e51f3d990c)
![image](https://github.com/user-attachments/assets/4d91d9a3-bbfc-4499-8f72-ac85676ce4be)

15.소스 파일 폴더에서 cmd 실행 후 아래 코드 입력
```
pip install -r requirments.txt
```
 
16. 아래 코드 입력 시 챗봇 실행
```
python main.py
```


## 🛠 실행 결과

![image](https://github.com/user-attachments/assets/6463d3c8-6551-407d-9701-65bec884a85b)

<br>   


 </div>
    <div style="text-align: left;">
    <h2 style="border-bottom: 1px solid #21262d; color: #c9d1d9;"> 🧑‍💻 Contact me or bug report </h2> <br> 
    <div style="text-align: left;"> <a href=https://www.instagram.com/j_ch3873/> <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=Instagram&logoColor=white&link=https://www.instagram.com/j_ch3873/"> </a>
         <a href=mailto:jangdoll7438@gmail.com> <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=Gmail&logoColor=white&link=mailto:jangdoll7438@gmail.com"> </a>
    


