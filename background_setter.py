import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from apod_parser import apod_object_parser
import pathlib
import datetime
import ctypes
import time
import schedule
import urllib3

api_key = "NASA_APOD_API_KEY"
https = urllib3.PoolManager()

def internet_on():
    try:
        r = https.request('GET', 'https://google.com')
        return True
    except:
        print("Connection error, retrying...")
        return False

def get_response():    
    while not internet_on():
        time.sleep(1)
    response = apod_object_parser.get_data(api_key)
    if response['media_type'] == 'image':
        try:
            url = apod_object_parser.get_url(response)
            date = apod_object_parser.get_date(response)
            apod_object_parser.download_image(url, date)

            date = datetime.date.today()
            date_str = date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d")
            image_path = str(pathlib.Path().absolute()) + "/" + date_str + ".jpg"
            apod_object_parser.convert_image(image_path)
            
            print(image_path)

            with open('descriptions.txt', 'a+') as file:
                if date_str not in file.readlines():
                    file.write('\n')
                    file.write(date_str + '\n')
                    file.write(apod_object_parser.get_explaination(response))            

            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
        except:
            print("Error, probably because NASA image for current date doesn't exist yet.")
    else:
        print("APOD was not an image!")

schedule.every().day.at("01:00").do(get_response)

first_run = False

while True:
    if not first_run:
        schedule.run_all()
        first_run = True
    else:
        schedule.run_pending()
    print("Waiting another hour...")
    time.sleep(3600)    

