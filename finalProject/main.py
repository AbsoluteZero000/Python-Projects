import requests
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from bs4 import BeautifulSoup

def getLocation():
    location = locationInput.get()
    url = f"http://api.weatherapi.com/v1/current.xml?key=7cc12b0e84a4469a8eb154005242503&q={location}"

    response = requests.request("GET", url, headers={}, data={}, timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")
    temperature = soup.current.temp_c.text
    windSpeed = soup.current.wind_kph.text
    pressure = soup.current.pressure_mb.text
    humidity = soup.current.humidity.text
    precipitation = soup.current.precip_mm.text
    weather_info = f"\nWeather for {location}:\n"
    weather_info += f"Temperature: {temperature}°C\n"
    weather_info += f"Wind Speed: {windSpeed} kph\n"
    weather_info += f"Pressure: {pressure} mb\n"
    weather_info += f"Humidity: {humidity}%\n"
    weather_info += f"Precipitation: {precipitation} mm\n"

    weatherLabel.config(text=weather_info, anchor="w")

window = tk.Tk()
window.title("Weather Scraper")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
locationInput = tk.Entry(window, width=20)
locationLabel = tk.Label(window, text = 'location: ', font=('calibre',10, 'bold'))
locationSubmit = tk.Button(window, text="Submit", command=getLocation)
weatherLabel = tk.Label(window, text="", font=("calibre", 12))

locationLabel.grid(row=0, column=0, sticky="w")
locationInput.grid(row=0, column=1, padx=5)
locationSubmit.grid(row=0, column=2, padx=5)
weatherLabel.grid(row=1, columnspan=3, padx=10, pady=5, sticky="w")

window.mainloop()
