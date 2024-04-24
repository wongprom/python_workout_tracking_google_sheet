import os
from dotenv import load_dotenv
import requests

load_dotenv()

NUTRITION_APPLICATION_ID = os.getenv("NUTRITION_APPLICATION_ID")
NUTRITION_APPLICATION_KEY = os.getenv("NUTRITION_APPLICATION_KEY")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PROJECT_NAME = os.getenv("SHEETY_PROJECT_NAME")
SHEETY_SHEET_NAME = os.getenv("SHEETY_SHEET_NAME")



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
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
# print(result)

# Get my Sheety workout
SHEETY_ENDPOINT = "https://api.sheety.co"
response = requests.get(f"{SHEETY_ENDPOINT}/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}")
result = response.json()
print(result)