import requests

initalCurrency = input("Enter the initial currency: ")
targetCurrency = input("Enter the target currency: ")

while True:
    try:
        amount = float(input("Enter the amount: "))
    except TypeError:
        print("Enter valid amount")
        continue
    if amount < 0:
        print("Enter valid amount")
        continue
    else:
        break


url = ("https://api.apilayer.com/fixer/convert?to="
        + targetCurrency + "&from=" + initalCurrency
        + "&amount=" + str(amount))

payload = {}
headers= {
  "apikey": "5OHVsiumDAU5foHbLGJuHazdme2SXheD"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if(status_code != 200):
    print("Sorry, there was a problem. Please try again later.")
    quit()

result = response.json()
coverted_amount = result['result']
print(f'{amount} {initalCurrency} = {result} {targetCurrency}')
