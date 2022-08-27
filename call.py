import colorama
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say
from random import randrange
from colorama import Fore,Style,Back
from time import sleep 
from threading import Thread
import pygsheets
import time
import datetime
import os


isCalling = True

phone_cols = []
enable_Time_cols = []
expire_Time_cols = []

class selfPhoneData:
    def __init__(self, phoneNumber , enable_Time , expire_Time):
        self.phoneNumber = phoneNumber
        self.enable_Time = enable_Time
        self.expire_Time = expire_Time

def main():
    colormaInit()
    welcome()
    GetSheet()

    YELLOW = "\x1b[1;33;40m" 
    RED = "\x1b[1;31;40m"

    print(f"\n{RED}Enter the Phone Number : ", end='')
    To_input = input()

    #loop call
    if(checkPhoneInSheet(To_input)):
        NowTime = datetime.datetime.now()
        timeFormat = '{}/{}/{} {}'.format(NowTime.year,NowTime.month,NowTime.day,time.strftime('%X'))

        if(timeFormat >= TargetPhoneData.enable_Time) :   
            t1 = Thread(target=Listen_User_Stop)
            t1.start()
            t2 = Thread(target=Call_thread(To_input))
            t2.start()

            t1.join()
            t2.join()
        else:
            print('Not Calling Now...')
    else:
        print('Not match Phone...')
    

def Call_thread(To_input):   
    if isCalling :
        print('start to call ' + To_input + '...')
        
    while isCalling:
        Call(To_input)
        sleep(9.5) 

def Listen_User_Stop():
    while True:
        global isCalling
        
        NowTime = datetime.datetime.now()
        timeFormat = '{}/{}/{} {}'.format(NowTime.year,NowTime.month,NowTime.day,time.strftime('%X'))
        if (timeFormat >= TargetPhoneData.expire_Time) :
            isCalling = False
            print('Is PhoneCalling Expire...')
            break
        
def GetSheet():
    global phone_cols
    global enable_Time_cols
    global expire_Time_cols
    
    gc = pygsheets.authorize(service_file=os.getenv('PYGSHEETS_SERVICE_FILE_PATH'))
    sht = gc.open_by_url(os.getenv('PYGSHEETS_OPEN_URL'))
    wks = sht.worksheet_by_title("Phone")
    phone_cols = wks.get_col(1,returnas='cell' , include_tailing_empty=False)
    enable_Time_cols = wks.get_col(2,returnas='cell' , include_tailing_empty=False)
    expire_Time_cols = wks.get_col(4,returnas='cell' , include_tailing_empty=False)

                                            
def TwilioInit():
    accountSid = os.getenv('TWILIO_ACCOUNT_SID')
    authToken = os.getenv('TWILIO_AUTH_TOKEN')

    return Client(accountSid , authToken)

def colormaInit():   
    colorama.init()

def checkPhoneInSheet(To_input):
    global TargetPhoneData
    
    for i in range(1 , len(phone_cols)):
        if(To_input == phone_cols[i].value):
            TargetPhoneData = selfPhoneData(phone_cols[i].value ,enable_Time_cols[i].value  ,expire_Time_cols[i].value )
            return True

    return False

def Call(TargetPhone):
    client = TwilioInit()
        
    numbers = client.incoming_phone_numbers.list()
    randPhone = randrange(len(numbers))

    twiml = VoiceResponse()
    twiml.dial(TargetPhone)

    call = client.calls.create(
        from_=numbers[randPhone].phone_number,
        to=TargetPhone,
        timeout=8,
        twiml=str(twiml),
        time_limit=1    
        )
    
#welcome 
def welcome():
	wel =Fore.GREEN + """
        +==========================================+
        |..........   Crazy PhoneCall   ...........|
        +------------------------------------------+
        |             #Author: Jimmy               | 
        |	       Version 1.0                 |
        |                                          |
        |          You can call everyone           |
        |                 you hate                 |
        +==========================================+
        |..........   Crazy PhoneCall  ............|
        +------------------------------------------+\n\n
"""

	print(wel)
    
if __name__ == '__main__':
	main()
