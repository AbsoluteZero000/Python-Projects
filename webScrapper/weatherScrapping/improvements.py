import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_cairo_weather():
    """
    Fetches weather data for Cairo from Time and Date website and returns a DataFrame.
    """
    try:
        response = requests.get("https://www.timeanddate.com/weather/egypt/cairo/ext", timeout=(10,10))
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find(attrs={'class': 'zebra'})

        # Extract data into a list of dictionaries
        weather_data = []
        for row in table.tbody.find_all("tr"):
            day = row.th.span.text
            date = row.th.text.strip()
            temp = int(row.find_all("td")[1].text.split()[0])  # Extract numerical temperature
            weather_data.append({'Day': day, 'Date': date, 'Temperature (°C)': temp})

        # Create a pandas DataFrame
        df = pd.DataFrame(weather_data)
        return df

    except (AttributeError, requests.exceptions.RequestException) as e:
        print(f"Error: {e}")
        return None

# Example usage
weather_df = get_cairo_weather()
if weather_df is not None:
    print(weather_df.to_string())
