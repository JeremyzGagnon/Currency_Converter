import requests

# Currency of the user
currencyCode = input().upper()
# Cache dict
exchangeRatesCache = dict()

ratesUrl = f"http://www.floatrates.com/daily/{currencyCode}.json"

# Make a GET request to a URL
response = requests.get(ratesUrl)

# Check the response status code
if response.status_code == 200:
    # Request was successful
    data = response.json()  # Parse the response as JSON
    if data.get("usd"):
        exchangeRatesCache["USD"] = data.get("usd").get("rate")
    if data.get("eur"):
        exchangeRatesCache["EUR"] = data.get("eur").get("rate")
else:
    # Request failed
    print('Request failed with status code:', response.status_code)


exchangeCode = input().upper()
while(len(exchangeCode) != 0):
    # # # Currency that the user want to convert to
    # # # Amount of money that the user have in its currency
    moneyAmount = float(input())
    print("Checking the cache...")
    if exchangeRatesCache.__contains__(exchangeCode):
        print("Oh! It is in the cache!")
        exchangeResult = round(moneyAmount * exchangeRatesCache.get(exchangeCode), 2)
        print(f"You received {exchangeResult} {exchangeCode}.")
    else:
        print("Sorry, but it is not in the cache!")
        # Adding the new rate to the cache
        exchangeRatesCache[exchangeCode] =  data.get(exchangeCode.lower()).get("rate")
        exchangeResult = round(moneyAmount * exchangeRatesCache.get(exchangeCode), 2)
        print(f"You received {exchangeResult} {exchangeCode}.")
    exchangeCode = input().upper()















# OLD Stage
# # Get the number of conicoins from user
# coniCoinAmount = float(input(""))
#
# # Dictionary of currency and their exchange rate for 1 conicoin
# currencyRate = {
#     "RUB": 2.98,
#     "ARS": 0.82,
#     "HNL": 0.17,
#     "AUD": 1.9622,
#     "MAD": 0.208,
# }
#
# for i, key in enumerate(currencyRate):
#     print(f"I will get {round(currencyRate.get(key) * coniCoinAmount, 2)} {key} from the sale of {coniCoinAmount} conicoins.")
#
