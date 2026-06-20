from flask import Flask, render_template, request
import requests
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

API_KEY = os.environ.get("WEATHER_API_KEY", "0eb0eb97f76f4bbe891163315261806")
CSV_FILE = "weather_data.csv"


def save_search(city, temp):
    df = pd.DataFrame({
        "Date": [datetime.now()],
        "City": [city],
        "Temperature": [temp]
    })

    if os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(CSV_FILE, index=False)


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":

        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."

        else:
            try:
                url = (
                    f"https://api.weatherapi.com/v1/forecast.json"
                    f"?key={API_KEY}"
                    f"&q={city}"
                    f"&days=7"
                    f"&aqi=yes"
                    f"&alerts=yes"
                )

                response = requests.get(url, timeout=10)
                response.raise_for_status()

                weather = response.json()

                save_search(
                    city,
                    weather["current"]["temp_c"]
                )

            except requests.exceptions.RequestException:
                error = "Unable to fetch weather data."

            except Exception as e:
                error = str(e)

    return render_template(
        "index.html",
        weather=weather,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)