import pandas as pd 
from datetime import date
import plotly.express as px
import requests

API_RT = "https://api.tomorrow.io/v4/weather/realtime"
API_TL= "https://api.tomorrow.io/v4/timelines"
API_HEADER = {"Accept": "application/json"}
API_KEY = "n9yNm2ORrLLkeJrdYrVmw90lWuIc0nIL"
LOCATIONS = ["blatenská praha"]  # Replace with actual locations

TL_FROM = "nowMinus1d"
TL_TO = "now"

TODAY = date.today().strftime("%Y-%m-%d")
CSV_FILE = f"teploty_{TODAY}.txt"

def call_api_rt(location):
    params = {
        "location": location,
        "apikey": API_KEY
    }
    response = requests.get(API_RT, headers=API_HEADER, params=params)
    return response.json()

def call_api_tl(lat, long):
    params = {
        "apikey": API_KEY
    }

    data_tl = {
        "location": f"{lat},{long}",
        "fields": ["temperature"],
        "units": f"metric",
        "timesteps": ["1h"],
        "startTime": TL_FROM,
        "endTime": TL_TO,
        "dailyStartHour": 6
    }
    response = requests.post(API_TL, headers=API_HEADER, params=params, json=data_tl)
    return response.json()   
    
def get_latlong(rt_data):
    lat = rt_data.get("location", {}).get("lat")
    long = rt_data.get("location", {}).get("lon")
    return lat, long
        
def plot_data(tl_data, location):
    # Extracting data for plotting
    timestamps = []
    temperatures = []
    
    for timeline in tl_data.get("data", {}).get("timelines", []):
        for interval in timeline.get("intervals", []):
            timestamps.append(interval.get("startTime"))
            temperatures.append(interval.get("values", {}).get("temperature"))
    
    fig = px.line(x=timestamps, y=temperatures, title=f"Temperature Over Time for Location: {location}")
    fig.show()
    

def save_to_csv(tl_data, location):
    timestamps = []
    temperatures = []
    
    for timeline in tl_data.get("data", {}).get("timelines", []):
        for interval in timeline.get("intervals", []):
            timestamps.append(interval.get("startTime"))
            temperatures.append(interval.get("values", {}).get("temperature"))
    
    df = pd.DataFrame({
        "timestamp": timestamps,
        "temperature": temperatures
    })
    
    df.to_csv(CSV_FILE, index=False)
    print(f"Data saved to {CSV_FILE}") 
    
    
def main():
    for location in LOCATIONS:
        rt_data = call_api_rt(location)
        lat, long = get_latlong(rt_data)
        tl_data = call_api_tl(lat,long)
        print(f"Real-time data for {location}: {rt_data}")
        print(f"Latitude: {lat}, Longitude: {long}")
        print(f"Timeline data for {location}: {tl_data}")
        plot_data(tl_data, location)
        save_to_csv(tl_data, location)

if __name__ == "__main__":
    main()