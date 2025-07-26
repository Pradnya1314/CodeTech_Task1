import requests
import matplotlib.pyplot as plt


API_KEY = 'bc3a25a6057852f94ddd94c0d946dc68'  
CITY = 'Mumbai'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'


response = requests.get(URL)
data = response.json()


if response.status_code != 200:
    print("Failed to retrieve data:", data.get("message", "Unknown error"))
    exit()


temperatures = []
timestamps = []

for forecast in data['list'][:8]:  # Get next 8 timestamps (24 hours)
    temp = forecast['main']['temp']
    time = forecast['dt_txt']
    temperatures.append(temp)
    timestamps.append(time.split(" ")[1][:5])  # Extract hour:min


plt.figure(figsize=(10,5))
plt.plot(timestamps, temperatures, marker='o', color='skyblue', linestyle='-')
plt.title(f"24-Hour Forecast Temperature in {CITY}")
plt.xlabel("Time (HH:MM)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
