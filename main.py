import requests
from twilio.rest import Client
import json

#   Input stock you would like to track
STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

#   Create a config.json with required values. API and keys info can be found in README
with open("./config.json") as config:
    keys = json.load(config)[0]

account_sid = keys['account_sid']
auth_token = keys['auth_token']

stock_api_key = keys['stock_api_key']
stock_api_endpoint = "https://www.alphavantage.co/query"
stock_parameters = {
    "apikey": stock_api_key,
    "function": "TIME_SERIES_DAILY",
    "outputsize": "compact",
    "symbol": "AAPL"
}

#   Sends get request to stock api and gathers yesterday's and day before yesterday's closing stock prices
stock_response = requests.get(url=stock_api_endpoint, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
daily_data = stock_data['Time Series (Daily)']
data_list = [value for (key, value) in daily_data.items()]
yesterday_data = data_list[0]
yesterday_close = yesterday_data['4. close']
day_before_yesterday_data = data_list[1]
day_before_yesterday_close = day_before_yesterday_data['4. close']


#   Gets the percent difference between closing price from yesterday and day before
def percent_difference(price1, price2):
    return abs((float(price1) - float(price2)) / ((float(price1) + float(price2)) / 2)) * 100


news_api_key = keys['news_api_key']
news_api_endpoint = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": "AAPL",
    "apiKey": news_api_key,
    "qInTitle": STOCK
}


#   Gathers 3 newest news articles related to stock and adds them to a list for formatting
def get_news():
    news_response = requests.get(url=news_api_endpoint, params=news_parameters)
    news_data = news_response.json()
    articles = news_data['articles']
    news = articles[:3]
    complete_list = [f"Headline {article['title']}. \nBrief: {article['description']}" for article in news]

    return complete_list


#   Checks if closing price from yesterday and day before are is an increased value or decreased value then associates the symbol
def inc_dec(yesterday_close, day_before_yesterday_close):
    if yesterday_close > day_before_yesterday_close:
        symbol = "🔺"
        return symbol
    else:
        symbol = "🔻"
        return symbol


#   Formats 3 articles, stock, increase/decrease symbol, and percent into clean text message format
def format_text(symbol, article, percent):
    text = (f"{STOCK}: {symbol}{percent}%\n"
            f"{article}")
    return text

#   Sends 3 texts with stock percent change and three articles that are potentially related to users phone number using twilio api
def main():
    percent = round(percent_difference(float(yesterday_close), float(day_before_yesterday_close)))
    if percent >= 5:
        complete_list = get_news()
        symbol = inc_dec(yesterday_close, day_before_yesterday_close)
        client = Client(account_sid, auth_token)
        for article in complete_list:
            text = format_text(symbol, article, percent)
            message = client.messages \
                .create(
                body=text,
                from_=keys['twilio_num'],
                to=keys['usr_num']
            )
        print(message.status)

if __name__ == "__main__":
    main()
