# times.py
import requests
from datetime import datetime


def iss_passes(lat: float, lon: float, alt: float = 0, days: int = 5, min_visibility: int = 50, api_key: str = ""):
    
    # Returns a list of strings with start and end times of visible ISS passes.

    url = f"https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/{lat}/{lon}/{alt}/{days}/{min_visibility}&apiKey=33Q884-HFUV8K-SCS3LG-55CU"
    response = requests.get(url)
    data = response.json()

    passes = data.get("passes", [])
    results = []

    for p in passes:
        start_time = datetime.fromtimestamp(p["startUTC"]).strftime("%Y-%m-%d %H:%M:%S")
        end_time = datetime.fromtimestamp(p["endUTC"]).strftime("%Y-%m-%d %H:%M:%S")
        results.append(f"{start_time} → {end_time}")

    return results
