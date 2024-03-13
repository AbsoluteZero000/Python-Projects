import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.timeanddate.com/weather/egypt/cairo/ext", timeout=(10,10))

soup = BeautifulSoup(response.content, "html.parser")
tableOfWeatherStuff = soup.find_all(attrs={'class':'zebra'})
weatherElements = tableOfWeatherStuff[0].tbody.find_all("tr")
for weatherElement in weatherElements:
    day = weatherElement.th.span.text
    date = weatherElement.th.text
    temp = weatherElement.find_all("td")[1].text
    print("the temp is " + temp," on the day", day, date)
