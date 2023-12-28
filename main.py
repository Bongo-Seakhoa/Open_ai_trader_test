import openai
import yfinance as yf
import pandas as pd

api_key = ''
openai.api_key = api_key
client = openai.OpenAI()

def fetch_historical_data(currency_pair, period='5d', interval='5m'):
    data = yf.download(currency_pair, period=period, interval=interval)
    if data is None or data.empty:
        raise ValueError("Failed to fetch historical data or empty dataset.")
    
    # Resize and format the data
    data = data.tail(49)
    data['date'] = data.index
    data.reset_index(inplace=True)
    price_data_dict = data[["date", "Open", "High", "Low", "Close"]].to_dict()
    return price_data_dict

def get_trading_recommendation(currency_pair, data_dict):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """ Your task is to provide a trading recommendation based on:
- **Signal:** Clear buy or sell signal.
- **Entry Price:** Suggested price to open the trade.
- **Take Profit:** Suggested price to close the trade if profitable.
- **Stop Loss:** Suggested price to close the trade if not profitable.
**Input:**
- Currency Pair: {currency_pair}
- Price Action Dictionary: {data_dict}
**Output:**
Complete the following dictionary with your trading recommendations:
{"signal": "", "entry price": "", "take profit": "", "stop loss": ""}
"""
            },
            {"role": "user", "content": f"Currency Pair: {currency_pair} and Dictionary: {data_dict}"}
        ]
    )
    return completion.choices[0].message.content

def main():
    currency_pair = 'EURUSD=X'
    
    try:
        price_data_dict = fetch_historical_data(currency_pair)
        trading_recommendation = get_trading_recommendation(currency_pair, price_data_dict)
        print(trading_recommendation)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
