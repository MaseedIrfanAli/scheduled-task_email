import requests
from twilio.rest import Client
import os
# from twilio.http.http_client import TwilioHttpClient


api_key=os.getenv("API_KEY")
auth_key=os.getenv("AUTH_TOKEN")
account_sid = auth_key=os.getenv(
url="https://api.openweathermap.org/data/2.5/forecast"
parameters={"lat" : 17.395098,
            "lon" : 78.383877,
            "appid" : api_key,
            "cnt": 4
        }

# https://api.openweathermap.org/data/2.5/weather?lat=17.3951&lon=78.3742&appid=e71a065406c38c442c1cf15d8d96b9e1

response = requests.get(url,params=parameters)
response.raise_for_status()
weather_data = response.json()
import datetime
import pandas as pd
now = datetime.datetime.now()
hr=now.hour
time=now.time()
print(time, hr)
# for key,val in weather_data.items():
#     if key == "list":
#         for i in range(len(val)):
#                 print(val[i]["weather"][0]["id"])
#
# dict_weather_data = pd.json_normalize(weather_data)
# for i in range(len(dict_weather_data.list[0])):
#         if dict_weather_data.list[0][i]["weather"][0]["id"] > 700:
#             print("Bring an Umbrella")
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    account_sid = "ACc6735e0a9976acd0bfdf367f16f486b5"
    auth_token = auth_key
    client = Client(account_sid, auth_token)
    message = client.messages\
         .create(
            messaging_service_sid= "MG2932519c17503bd36165aeba90c251f1",
            body="Its going to rain today. Remember to bring an umbrella",
            to="+918328625700"
    )
    print(message.status)




# +18777804236
