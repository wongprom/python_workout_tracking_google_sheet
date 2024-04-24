import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()
# https://docs.google.com/spreadsheets/d/1mlCjblBAzZNhTFuDTrTuSEDjN3AqovwUEtEEBAZlXog/edit#gid=0
# https://dashboard.sheety.co/

NUTRITION_APPLICATION_ID = os.getenv("NUTRITION_APPLICATION_ID")
NUTRITION_APPLICATION_KEY = os.getenv("NUTRITION_APPLICATION_KEY")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PROJECT_NAME = os.getenv("SHEETY_PROJECT_NAME")
SHEETY_SHEET_NAME = os.getenv("SHEETY_SHEET_NAME")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")


GENDER = "MALE"
WEIGHT_KG = "85"
HEIGHT_CM = "182"
AGE = 42

APP_ID = NUTRITION_APPLICATION_ID
API_KEY = NUTRITION_APPLICATION_KEY

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_TOKEN}"

}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# Get my Sheety workout
# SHEETY_ENDPOINT = "https://api.sheety.co"
# response = requests.get(f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}")
# result = response.json()
# print(result)

# Add row to my Sheet workout
SHEETY_ENDPOINT = "https://api.sheety.co"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    exercise_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}", json=exercise_inputs, headers=headers)
    print(sheet_response.text)