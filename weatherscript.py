import requests
import schedule
import time
import json 

def job():
    api_key = "ADD YOUR OPENWATHERMAP API KEY HERE"
    with open('weatherdata.txt', 'a') as f:
        ################### for Ann Arbor #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Ann%20Arbor&appid={api_key}')
        f.write(json.dumps(r.json()) + '\n')
        ################### for Detroit #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Detroit&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for Chicago #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Chicago&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for New York #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=New York&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for Boston #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Boston&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for Washington D.C. #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Washington D.C.&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for Atlanta #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Atlanta&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for Miami #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Miami&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for Austin #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Austin&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for Los Angeles #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Los Angeles&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for san francisco #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=san francisco&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for Seattle #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Seattle&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')
        ################### for vancouver #######################################################################################
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=vancouver&appid={api_key}')
        print(r.json(), '\n')
        f.write(json.dumps(r.json())+ '\n')

schedule.every().hour.do(job)

job() 
try:
    while True:
            schedule.run_pending()
            time.sleep(1)
except KeyboardInterrupt:
    print('While loop has ended')
