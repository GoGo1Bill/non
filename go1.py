import datetime
import time
import pyupbit
import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2609205237909-2597943438071-4QQ4lYIiivGmlBisb24UwgMv"

def get_start_time(KRWDOGE):
    df = pyupbit.get_ohlcv("KRW-DOGE", interval="day", count=1)
    start_time = df.index[0]
    return start_time

while True:
     try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-DOGE")
        end_time = start_time + datetime.timedelta(days=1)

        df1 = pyupbit.get_ohlcv("KRW-DOGE", interval="minute5", count=3)
        target = df1.iloc[0]['close'] - df1.iloc[-1]['open']
        
        df2 = pyupbit.get_ohlcv("KRW-DOGE", interval="minute1", count=1)
        current = df2.iloc[0]['close']

        if start_time < now < end_time:
            if target >= 3 or target <= -3 :

                 post_message(myToken,"#test", "price : " + str(current))
                 print(current)
                 time.sleep(30)
        
            else :
                 keep = 3 < target < -3
                 print(keep)
                 print(target)
                 print(current)
                 time.sleep(30)
                 
                          
     except Exception as e:
        print(e)
        time.sleep(30)
