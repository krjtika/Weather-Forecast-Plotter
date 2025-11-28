import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "ea6aab7908753d8368046d3b6b7c5777"

city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print("Error:", e)
    exit()

dates = []
temps = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temps.append(entry['main']['temp'])

plt.figure(figsize=(18, 7))
sns.lineplot(x=dates, y=temps, marker="o")
plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {city}")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
