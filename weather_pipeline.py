import requests as re
import pandas as pd
from datetime import datetime
import os

#.url & cities
url = "https://api.open-meteo.com/v1/forecast"
cities = {
    "Johannesburg": (-26.2, 28.04),
    "Cape Town": (-33.92, 18.42),
    "Durban": (-29.86, 31.02),
    "Pretoria": (-25.75, 28.19),
    "Gqeberha": (-33.96, 25.60),
}

# 3. functionss (definitions only)
def fetch_city(name, lat, lon):
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    try:
        response = re.get(url, params=params, timeout=10.0)
        if response.status_code != 200:
            print("failed:", name)
            return None
        weather = response.json()["current_weather"]
        return {
            "city": name,
            "temperature": weather["temperature"],
            "observed_at": weather["time"],
            "windspeed": weather["windspeed"],
        }
    except re.exceptions.RequestException:
        print("failed:", name)
        return None

def fetch_all(cities):
    results = []
    for name, (lat, lon) in cities.items():
        result = fetch_city(name, lat, lon)
        if result is not None:
            results.append(result)
    return results

def shape_data(results):
    df = pd.DataFrame(results)
    df["fetched_at"] = datetime.now()
    return df

def save_data(df):
    file_exists = os.path.exists("weather.csv")
    df.to_csv("weather.csv", mode="a", header=not file_exists, index=False)

# 4. Main block
results = fetch_all(cities)
if not results:
    print("empty: nothing saved")
else:
    df = shape_data(results)
    save_data(df)

print(os.getcwd())
print(pd.read_csv("weather.csv").shape)