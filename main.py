import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "2631fe899efced49d84f92c52d44cfd7"
account_sid = "AC7d17d04a6d4e21103daa0048dd940c96"
auth_token = "d1971d3d4146b29625ab2b903eba83f1"
weather_params = {
    "lat":27.176670,   #12.882566,
    "lon":78.008072,   #77.617914,
    "appid": api_key,
    "cnt": 4,

}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+19293493873",
        to="+918123664898",
    )
    # message = client.messages.create(
    #     from_="+1 415-523-8886",
    #     body="It's going to rain today. Remember to bring an ☔",
    #     to="+918123664898"
    # )

    print(message.status)