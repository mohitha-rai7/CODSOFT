import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = entry_city.get()
    api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        messagebox.showinfo("Weather Forecast", f"Weather in {city}: {temperature}°C, {weather_desc}")
    else:
        messagebox.showerror("Error", f"Failed to fetch weather data for {city}")

root = tk.Tk()
root.title("Weather Forecast")

label_city = tk.Label(root, text="Enter City:")
label_city.pack(pady=5)

entry_city = tk.Entry(root)
entry_city.pack(pady=5)

button_get_weather = tk.Button(root, text="Get Weather", command=get_weather)
button_get_weather.pack(pady=5)

root.mainloop()
