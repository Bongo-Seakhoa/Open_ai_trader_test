# Trading Recommendation Script
This script utilizes the OpenAI GPT-3 model to generate trading recommendations based on historical price data obtained using the Yahoo Finance API (yfinance). The generated recommendations include signals for buy or sell, suggested entry prices, take-profit prices for profitable trades, and stop-loss prices for non-profitable trades.

## Prerequisites
-Python 3.x

### Required Python libraries:
- openai
- yfinance
- pandas
 
### Setup
Install the required libraries using pip:
`bash
pip install openai yfinance pandas`
Obtain an API key for OpenAI GPT-3 and assign it to the api_key variable in the script.

### Usage
The fetch_historical_data() function retrieves historical price data for a specified currency pair using the Yahoo Finance API.
The get_trading_recommendation() function utilizes the GPT-3 model to generate trading recommendations based on the historical price data.
Run the script by executing python script_name.py in the terminal.

### Example
`python
python main.py`

### Important Notes
Ensure the api_key variable is properly configured with a valid API key for OpenAI GPT-3.
Modify the currency_pair variable in the main() function to specify the desired currency pair for trading recommendations.

### Disclaimer
The trading recommendations provided by this script are generated based on historical data and AI-driven analysis. Use these recommendations cautiously and perform additional analysis before making any financial decisions. The script's output does not guarantee success in trading and should be used for informational purposes only.
