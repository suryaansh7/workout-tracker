nutrition_apikey="nix_live_X1r8qf15gJ7HX99qinfZlkaWT9Hhra1j"
nutrition_apid="app_8826f20b3c564a15b40e22b5"
nutrition_endpoint="https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
import requests
s=input("enter activity")
headers={
    "x-app-id":nutrition_apid,
    "x-app-key":nutrition_apikey,
    "Content-Type":"application/json"
}
params={
    "query":s
}
response=requests.post(url=nutrition_endpoint,json=params,headers=headers)
import datetime
c=datetime.datetime.now()
k=c.strftime("%d/%m/%y")
print(k)
r=c.strftime("%H:%M:%S")
print(r)
v=response.json()
print(v)
s=v["exercises"][0]["name"]
p=v["exercises"][0]["duration_min"]
n=v["exercises"][0]["nf_calories"]
edit_endpoint="https://api.sheety.co/1029e78a646e8a35665f0aff42262924/myWorkouts/workouts"

params={
    "workout":{
        "date":k,
        "time":r,
        "exercise":s,
        "duration":p,
        "calories":n


    }
}

response1=requests.post(url=edit_endpoint,json=params)
print(response1.text)









