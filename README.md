# stock-news-alert

## Overview

StockAlert is a Python-based application designed to keep users informed about significant changes in stock prices. The app monitors user-specified stocks and sends text message alerts when a stock experiences a notable increase or decrease of 5% or more in the closing price over the last two consecutive days. Alongside price alerts, StockAlert enriches the user experience by providing three curated news articles related to the monitored stock.

## Prerequisites

Before running this application, you will need to obtain API keys from Twilio, Alpha Vantage, and News API. Follow the instructions below to obtain the necessary credentials.

## Getting API Keys

### Twilio

1. Go to the [Twilio Console](https://www.twilio.com/console).
2. Sign in or create a new account.
3. Obtain your `account_sid` and `auth_token` from the Twilio Dashboard.

### Alpha Vantage

1. Go to the [Alpha Vantage API](https://www.alphavantage.co/support/#api-key) page.
2. Sign up or log in to your Alpha Vantage account.
3. Obtain your `stock_api_key` from the API Key section.

### News API

1. Go to [newsapi.org](https://newsapi.org).
2. Sign up or log in to your News API account.
3. Obtain your `news_api_key` from the API Key section.


## Configuring Your Application

1. Clone this repository to your local machine.
2. Navigate to the root directory of the project.
3. Create a file named `config.json`.
4. Copy the following sample configuration into `config.json`:

```json
[
    {
        "account_sid": "YourTwilioAccountSID",
        "auth_token": "YourTwilioAuthToken",
        "stock_api_key": "YourAlphaVantageAPIKey",
        "news_api_key": "YourNewsAPIKey",
        "twilio_num": "+YourTwilioPhoneNumber",
        "usr_num": "+UserPhoneNumber"
    }
]
