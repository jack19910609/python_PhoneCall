# python_PhoneCall

Table of Contents
===

<!--ts-->
   * [BackGround](#background)
   * [Installation](#installation)
   * [Requirement](#requirement)
   * [Usage](#usage)
   * [Maintainers](#maintainers)
<!--te-->

BackGround
===
使用Python串接TWILIO API實現網路撥打電話,傳送SMS

Installation
===
你可以使用以下方法安裝python_PhoneCall

1. From Http https://github.com/jack19910609/python_PhoneCall.git
2. From SSH git@github.com:jack19910609/python_PhoneCall.git

* You can cloan this projet useing any svn Tool or github Tool  

Requirement
===
Python : 3.10.5

Twilio : 7.11.0

Pygsheets : 2.0.5

Usage
===

* ## TWILIO
#### 1. [Sign up the Twilio Account](https://www.twilio.com/)
#### 2. [Setting up Account](https://www.twilio.com/blog/make-phone-call-python-twilio-programmable-voice)
#### 3. Settint Environment Variables 
* #### Stpe1 - Click Environment Variables
   ![image](https://user-images.githubusercontent.com/7847128/187018994-4a0b7560-903a-4a1b-b1e6-81c0a89f1da4.png)
* #### Stpe2 - Click Add
   ![image](https://user-images.githubusercontent.com/7847128/187019025-d4a9cf65-ea9d-4ca8-a897-66964d249ae4.png)
* #### Stpe3 - Input Variable Name and Value
   ![image](https://user-images.githubusercontent.com/7847128/187019170-1f1ad8ae-d8bf-4785-8603-42acd527710a.png)
   > Variable Name Set as "TWILIO_ACCOUNT_SID" & "TWILIO_AUTH_TOKEN"
   
   > Value  Set by Twilio Consol Page 
   
   ![image](https://user-images.githubusercontent.com/7847128/187019507-b7d53c18-a6c5-4d2a-9855-591ee6f10fe4.png)
   
* ## Pygsheets
#### 1. [Login on Google Cloud Platform](https://console.cloud.google.com/getting-started?hl=zh-TW&pli=1)
#### 2. Setting Google Sheets API
* #### Step1 - Create New Project
  ![image](https://user-images.githubusercontent.com/7847128/187019746-8015f52c-e084-4a76-86b4-3bb7b09e19f0.png)
* #### Step2 - Choose a Projec
  ![image](https://user-images.githubusercontent.com/7847128/187019791-d7004a71-1dad-47a6-973c-9f3630a1def4.png)
* #### Step3 - Enable Google Sheets API
  ![image](https://user-images.githubusercontent.com/7847128/187019909-f4c19e8f-febc-4c83-8e0c-e9bb1e753777.png)
* #### Step4 - Create credentials
  ![image](https://user-images.githubusercontent.com/7847128/187020002-4c2ec2f7-b9dd-409b-b40d-2a135d42125e.png)
* #### Step5 - 在 Google Sheet 裡面，授權給剛剛在 GCP 申請的服務帳號 ID
  ![image](https://user-images.githubusercontent.com/7847128/187020085-25fc5ffe-5046-49f4-8eab-53727b1dc52a.png)

  ![image](https://user-images.githubusercontent.com/7847128/187020092-7ff988d0-8db9-4959-ac39-fffc61809837.png)

3. Settint Environment Variables
 * #### Step1 - Input Variable Name and Value
 
   ![image](https://user-images.githubusercontent.com/7847128/187019170-1f1ad8ae-d8bf-4785-8603-42acd527710a.png)
   > Variable Name Set as "PYGSHEETS_SERVICE_FILE_PATH" & "PYGSHEETS_OPEN_URL"
   
   > "PYGSHEETS_SERVICE_FILE_PATH" Value Set as 金鑰json檔儲存位置
   
      ![image](https://user-images.githubusercontent.com/7847128/187020366-37f0f57f-61a7-4d8a-9f24-f8e1db043b30.png)
      
   > "PYGSHEETS_OPEN_URL" Value Set as Google sheet URL
   
      ![image](https://user-images.githubusercontent.com/7847128/187020409-3f70bd06-35ca-4304-8068-ea95d7778573.png)

* ## 建立批次檔 
  > @echo off
  
  > start cmd /k "e: &&cd gitProject &&cd phone-call &&venv\Scripts\activate &&python call.py"
  
  ![image](https://user-images.githubusercontent.com/7847128/187020502-15cc2359-68af-46d1-aab8-99ed482ef4a4.png)  








Maintainers
===
[@Jimmy](https://github.com/jack19910609).

