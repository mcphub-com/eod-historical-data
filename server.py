import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/eod-historical-data-eod-historical-data-default/api/eod-historical-data'

mcp = FastMCP('eod-historical-data')

@mcp.tool()
def options_data_api(_from: Annotated[Union[str, datetime, None], Field(description='Filters OPTIONS by Expiration Date. Default value: today.')] = None,
                     to: Annotated[Union[str, datetime, None], Field(description="Filters OPTIONS by Expiration Date. Default value: '2100-01-01'.")] = None,
                     trade_date_from: Annotated[Union[str, datetime, None], Field(description='Filters OPTIONS by Last Trade Date Time. Default value: NONE.')] = None,
                     contract_name: Annotated[Union[str, None], Field(description='Returns only the data for particular contract.')] = None,
                     trade_date_to: Annotated[Union[str, datetime, None], Field(description='Filters OPTIONS by Last Trade Date Time. Default value: NONE.')] = None) -> dict: 
    '''We provide stock options data for top US stocks from NYSE and NASDAQ, the data for Options starts with April 2018. Options data is updated on a daily basis, however, we do not provide a history for options contracts’ prices or other data. That means: for each contract, there is only the current price, bid/ask, etc. For example, for AAPL today (May 7th, 2021) we have 2439 PUT and CALL option contracts in our database.'''
    url = 'https://eod-historical-data.p.rapidapi.com/options/AAPL.US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from': _from,
        'to': to,
        'trade_date_from': trade_date_from,
        'contract_name': contract_name,
        'trade_date_to': trade_date_to,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def technical_indicator_api(function: Annotated[str, Field(description='Technical Indicator Functions For all functions you can use the following parameters: to, from, order and fmt. In addition, you should use function parameter, we described the specific usage for each function here. Split Adjusted Data - splitadjusted Average Volume - avgvol Average Volume by Price - avgvolccy SMA - sma EMA - ema WMA - wma Volatility - volatility Stochastic Technical Indicator - stochastic Relative Strength Index - rsi Standard Deviation - stddev Stochastic Relative Strength Index - stochrsi Slope (Linear Regression) - slope Directional Movement Index - dmi Average Directional Movement Index - adx Moving Average Convergence/Divergence - macd Average True Range - atr Commodity Channel Index - cci Parabolic SAR - sar Bollinger Bands - bbands Amibroker File format - format_amibroker')],
                            period: Annotated[Union[int, float, None], Field(description='The number of data points used to calculate each moving average value. Valid range from 2 to 100000 with the default value – 50. Default: 50')] = None,
                            _from: Annotated[Union[str, datetime, None], Field(description='You can use this parameter with format ‘YYYY-MM-DD’.')] = None,
                            to: Annotated[Union[str, datetime, None], Field(description='You can use this parameter with format ‘YYYY-MM-DD’.')] = None,
                            order: Annotated[Union[str, None], Field(description='Use ‘a’ for ascending dates (from old to new) and ‘d’ for descending dates (from new to old). By default, dates are shown in ascending order.')] = None,
                            filter: Annotated[Union[str, None], Field(description='We also support the ability to get only the last value.')] = None,
                            fmt: Annotated[Union[str, None], Field(description='The output format, could be ‘json’ for JSON and ‘csv’ for CSV output. The default value is ‘json’.')] = None,
                            splitadjusted_only: Annotated[Union[int, float, None], Field(description='Default value is ‘0’. By default, we calculate data for some functions by closes adjusted with splits and dividends. If you need to calculate the data by closes adjusted only with splits, set this parameter to ‘1’. Works with the following functions: sma, ema, wma, volatility, rsi, slope, and macd. Default: 0')] = None,
                            agg_period: Annotated[Union[str, None], Field(description='Aggregation period. Default value – ‘d’. Possible values: d – daily, w – weekly, m – monthly. (for Split Adjusted Data)')] = None,
                            fast_kperiod: Annotated[Union[int, float, None], Field(description='Fast K-period, the default value is 14. Valid range from 2 to 100000. (for Stochastic Technical Indicator, Stochastic Relative Strength Index) Default: 0')] = None,
                            slow_kperiod: Annotated[Union[int, float, None], Field(description='Slow K-period, the default value is 3. Valid range from 2 to 100000. (for Stochastic Technical Indicator) Default: 0')] = None,
                            slow_dperiod: Annotated[Union[int, float, None], Field(description='Slow D-period, the default value is 3. Valid range from 2 to 100000. (for Stochastic Technical Indicator) Default: 0')] = None,
                            fast_dperiod: Annotated[Union[int, float, None], Field(description='Fast D-period, the default value is 14. Valid range from 2 to 100000. (for Stochastic Relative Strength Index) Default: 0')] = None,
                            fast_period: Annotated[Union[int, float, None], Field(description='For Moving Average Convergence/Divergence Default: 0')] = None,
                            slow_period: Annotated[Union[int, float, None], Field(description='For Moving Average Convergence/Divergence Default: 0')] = None,
                            signal_period: Annotated[Union[int, float, None], Field(description='For Moving Average Convergence/Divergence Default: 0')] = None,
                            acceleration: Annotated[Union[int, float, None], Field(description='Acceleration Factor used up to the Maximum value. Default value – 0.02. (for Parabolic SAR) Default: 0')] = None,
                            maximum: Annotated[Union[int, float, None], Field(description='Acceleration Factor Maximum value. Default value – 0.20. (for Parabolic SAR) Default: 0')] = None) -> dict: 
    '''The Technical Indicator API is available under ‘All World Extended’ and ‘All-In-One’ data packages. Each Technical API request consumes 5 API calls.'''
    url = 'https://eod-historical-data.p.rapidapi.com/technical/AAPL.US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'function': function,
        'period': period,
        'from': _from,
        'to': to,
        'order': order,
        'filter': filter,
        'fmt': fmt,
        'splitadjusted_only': splitadjusted_only,
        'agg_period': agg_period,
        'fast_kperiod': fast_kperiod,
        'slow_kperiod': slow_kperiod,
        'slow_dperiod': slow_dperiod,
        'fast_dperiod': fast_dperiod,
        'fast_period': fast_period,
        'slow_period': slow_period,
        'signal_period': signal_period,
        'acceleration': acceleration,
        'maximum': maximum,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def intraday_historical_data_api(interval: Annotated[Union[str, None], Field(description='The possible intervals: ‘5m’ for 5-minutes, ‘1h’ for 1 hour, and ‘1m’ for 1-minute intervals. Default value is ‘5m’.')] = None,
                                 fmt: Annotated[Union[str, None], Field(description='Use this parameter to get the data in a different format. Possible values are ‘json’ for JSON and ‘csv’ for CSV. By default, the data is provided in CSV format.')] = None,
                                 _from: Annotated[Union[int, float, None], Field(description='Use these parameters to filter data by datetime. Parameters should be passed in UNIX time with UTC timezone, for example, these values are correct: “from=1564752900&to=1564753200” and correspond to ‘ 2019-08-02 13:35:00 ‘ and ‘ 2019-08-02 13:40:00 ‘. The maximum periods between ‘from’ and ‘to’ are 120 days for 1-minute interval, 600 days for 5-minute interval and 7200 days for 1 hour interval. Default value is the maximum period till now. Default: 1564752900')] = None,
                                 to: Annotated[Union[int, float, None], Field(description='Use these parameter to filter data by datetime. Parameters should be passed in UNIX time with UTC timezone, for example, these values are correct: “from=1564752900\\\\\\\\\\\\\\" \\\\\\\\\\\\\\"to=1564753200” and correspond to ‘ 2019-08-02 13:35:00 ‘ and ‘ 2019-08-02 13:40:00 ‘. The maximum periods between ‘from’ and ‘to’ are 120 days for 1-minute interval, 600 days for 5-minute interval and 7200 days for 1 hour interval. Default value is closest to now. Default: 1564753200')] = None) -> dict: 
    '''The Intraday Data API is available under ‘All World Extended’ and ‘All-In-One’ data packages. We support intraday historical data for major exchanges all around the world. - We have 1-minute intervals for US (NYSE and NASDAQ), including pre-market (premarket) and after-hours (afterhours) trading data from 2004, more than 15 years of the data. And 5-minute, 1-hour intervals from October 2020. - For Forex, Cryptocurrencies and MOEX tickers we have 1-minute intervals trading data from 2009, more than 12 years of the data. And 5-minute, 1-hour intervals from October 2020. - For other tickers. 5-minute, 1-hour intervals and only from October 2020. The data is updated 2-3 hours after market closing. For the US market, only NYSE and NASDAQ tickers are supported.'''
    url = 'https://eod-historical-data.p.rapidapi.com/intraday/AAPL.US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'interval': interval,
        'fmt': fmt,
        'from': _from,
        'to': to,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def historical_splits_api(_from: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                          to: Annotated[Union[str, datetime, None], Field(description='Date to. Default value is the closest available date to now.')] = None,
                          fmt: Annotated[Union[str, None], Field(description='Use this parameter to get the data in a different format. Possible values are ‘json’ for JSON and ‘csv’ for CSV. By default, the data is provided in CSV format.')] = None) -> dict: 
    '''To get splits for any tickers.'''
    url = 'https://eod-historical-data.p.rapidapi.com/splits/AAPL.US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from': _from,
        'to': to,
        'fmt': fmt,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def historical_dividends_api(_from: Annotated[Union[str, datetime, None], Field(description='Date from. Default value is the earliest available date.')] = None,
                             to: Annotated[Union[str, datetime, None], Field(description='Date to. Default value is the closest available date to now.')] = None,
                             fmt: Annotated[Union[str, None], Field(description='Use this parameter to get the data in a different format. Possible values are ‘json’ for JSON and ‘csv’ for CSV. By default, the data is provided in CSV format. Please note, that the extended format with declaration date, record date, and the payment date is available only for major US tickers and only in JSON format.')] = None) -> dict: 
    '''Get dividends for any ticker.'''
    url = 'https://eod-historical-data.p.rapidapi.com/div/AAPL.US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from': _from,
        'to': to,
        'fmt': fmt,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_list_of_tickers(fmt: Annotated[Union[str, None], Field(description='The output format. Possible values are ‘csv’ for CSV output and ‘json’ for JSON output. Default value: ‘csv’.')] = None) -> dict: 
    '''We support more than 60 exchanges all around the world. All US exchanges are combined into one virtual exchange ‘US,’ which includes NYSE, NASDAQ, NYSE ARCA, and OTC/PINK tickers. All indices and commodities are in virtual exchanges INDX and COMM, respectively. To get the full list of supported exchanges with names, codes, operating MICs, country, and currency, you can use the ‘exchanges-list’ endpoint'''
    url = 'https://eod-historical-data.p.rapidapi.com/exchange-symbol-list/US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fmt': fmt,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def financial_news_api(s: Annotated[Union[str, None], Field(description='REQUIRED if parameter ‘t’ not set. The ticker code to get news for.')] = None,
                       t: Annotated[Union[str, None], Field(description='REQUIRED if parameter ‘s’ not set. The tag to get news on a given topic.')] = None,
                       _from: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                       to: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
                       limit: Annotated[Union[int, float, None], Field(description='The number of results should be returned with the query. Default value: 50, minimum value: 1, maximum value: 1000. Default: 50')] = None,
                       offset: Annotated[Union[int, float, None], Field(description='The offset of the data. Default value: 0, minimum value: 0. For example, to get 100 symbols starting from 200 you should use limit=100 and offset=200. Default: 0')] = None) -> dict: 
    '''The Financial News API is available under all subscriptions. Each Financial News API request consumes 5 API calls. The Financial News API is a powerful tool that helps you get company news and filter out them by date, type of news and certain tickers with the given parameters.'''
    url = 'https://eod-historical-data.p.rapidapi.com/news'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        's': s,
        't': t,
        'from': _from,
        'to': to,
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_market_screener_api(filters: Annotated[Union[str, None], Field(description='Filtering data with Fields You can use fields to filter the data. Fields have two types: Strings and Numbers. For strings should be used String Operations and for Numbers should be used Numeric Operations (see the chapter “List of Operations” in this documentation). For example, you can filter all companies with Market Capitalization above 1 billion, have only positive EPS within the ‘Personal Products’ industry, and with name started with the letter ‘B’. Usage: filters=[[“field1”, “operation1”, value1],[“field2”, “operation2”, value2] , … ]. Filters out tickers by different fields. List of Supported Fields code: String. Filters by the ticker code. name: String. Filters by the ticker name. exchange: String. Filters by the exchange code. The list of all exchange codes is here. sector: String. Filters by sector. The list of sectors and industries is here. industry: String. Filters by industry. The list of sectors and industries is here. market_capitalization: Number. Filters by Market Capitalization, the latest value. Please note, that input for market_capitalization in USD. earnings_share: Number. Filters by Earnings-per-share (EPS), the latest value. dividend_yield: Number. Filters by Dividend yield, the latest value. refund_1d_p: Number. The last day gain/loss in percent. Useful to get top gainers, losers for the past day. refund_5d_p: Number. The last 5 days gain/loss in percent. Useful to get top gainers, losers for the past week.')] = None,
                              signals: Annotated[Union[str, None], Field(description='Filtering Data with Signals You can use signals to filter tickers by different calculated fields. All signals are pre-calculated on our side. For example, if you need only tickers that have new lows for the past 200 days and the Book Value is negative, you can use the parameter ‘signal’ with the following value, to get all tickers with the criteria: signals=bookvalue_neg,200d_new_lo List of supported Signals 50d_new_lo, 50d_new_hi, 200d_new_lo, 200d_new_hi – filters tickers that have new 50/200 days lows or new 50/200 days highs. bookvalue_neg, bookvalue_pos – filters tickers with positive Book Value or with Negative Book Value. wallstreet_lo, wallstreet_hi – filters tickers that have a price lower or higher than expected by Wall Street analysts.')] = None,
                              sort: Annotated[Union[str, None], Field(description='Usage: field_name.(asc|desc). Sorts all fields with type ‘Number’ in ascending/descending order.')] = None,
                              limit: Annotated[Union[int, float, None], Field(description='The number of results should be returned with the query. Default value: 50, minimum value: 1, maximum value: 100. Default: 50')] = None,
                              offset: Annotated[Union[int, float, None], Field(description='The offset of the data. Default value: 0, minimum value: 0, maximum value: 1000. For example, to get 100 symbols starting from 200 you should use limit=100 and offset=200. Default: 0')] = None) -> dict: 
    '''The Screener API is available under ‘All World Extended’ and ‘All-In-One’ data packages. Each Screener API request consumes 5 API calls. The Screener API is a powerful tool that helps you filter out tickers with the given parameters. The example of URL for the Screener API: > https://eodhistoricaldata.com/api/screener?api_token=YOUR_API_TOKEN&sort=market_capitalization.desc&filters=[["market_capitalization",">",1000],["name","match","apple"],["code","=","AAPL"],["exchange","=","us"],["sector","=","Technology"]]&limit=10&offset=0 **filters**: String. OPTIONAL. Usage: filters=[[“field1”, “operation1”, value1],[“field2”, “operation2”, value2] , … ]. Filters out tickers by different fields. **signals**: String. OPTIONAL. Usage: signals=signal1,signal2,…,signalN. Filter out tickers by signals, the calculated fields. **sort**: String. OPTIONAL. Usage: sort=field_name.(asc|desc). Sorts all fields with type ‘Number’ in ascending/descending order. **api_token**: String. REQUIRED. Your api_token to access the API. You will get it after registration. **limit**: Number. OPTIONAL. The number of results should be returned with the query. Default value: 50, minimum value: 1, maximum value: 100. **offset**: Number. OPTIONAL. The offset of the data. Default value: 0, minimum value: 0, maximum value: 1000. For example, to get 100 symbols starting from 200 you should use limit=100 and offset=200. ### List of Operations String operations are supported for all fields with type ‘String’. Numeric Operations are supported for all fields with type ‘NUMBER’: String Operations: [‘=’, ‘match’]. Numeric Operations: [‘=’, ‘>’, ‘<‘, ‘>=’, ‘<=’, ‘!=’]. Please note that each API request for Screener API consumes 5 API calls.'''
    url = 'https://eod-historical-data.p.rapidapi.com/screener'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'filters': filters,
        'signals': signals,
        'sort': sort,
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_list_of_exchanges(fmt: Annotated[Union[str, None], Field(description='The output format. Possible values are ‘csv’ for CSV output and ‘json’ for JSON output. Default value: ‘json’.')] = None) -> dict: 
    '''We support more than 60 exchanges all around the world. All US exchanges are combined into one virtual exchange ‘US,’ which includes NYSE, NASDAQ, NYSE ARCA, and OTC/PINK tickers. All indices and commodities are in virtual exchanges INDX and COMM, respectively.'''
    url = 'https://eod-historical-data.p.rapidapi.com/exchanges-list/'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fmt': fmt,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_exchange_details(_from: Annotated[Union[str, datetime, None], Field(description='The default value is 6 months before the current date.')] = None,
                         to: Annotated[Union[str, datetime, None], Field(description='The default value is 6 months after the current date.')] = None) -> dict: 
    '''With this API endpoint you will get detailed information about each exchange we do support, including: - Timezone – the timezone of exchange - isOpen – boolean value which indicates if exchange open right now or closed. - Trading hours and working days – open hours with working days for each exchange in the exchange timezone. This field could include also lunch hours if the exchange has it. - ActiveTickers – tickers with any activity for the past two months. - UpdatedTickers – tickers updated for the current day.'''
    url = 'https://eod-historical-data.p.rapidapi.com/exchange-details/US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from': _from,
        'to': to,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_api(limit: Annotated[Union[int, float, None], Field(description='The number of results should be returned with the query. Default value: 15. If the limit is higher than 50, it will be automatically reset to 50. Default: 15')] = None,
               bonds_only: Annotated[Union[int, float, None], Field(description='The default value is 0 and search returns only tickers, ETFs, and funds. To get bonds in result use value 1. Default: 0')] = None,
               exchange: Annotated[Union[str, None], Field(description='Filters output by exchange. Allowed input is the exchange code, for example: US, PA, CC, FOREX and others. In addition, it’s possible to use ‘NYSE’ and ‘NASDAQ’ exchange codes to filter out only tickers from these exchanges.')] = None,
               type: Annotated[Union[str, None], Field(description='The default value is ‘all’. You can specify the type of asset you search for. Possible values: all, stock, etf, fund, bonds, index, commodity, crypto. Please note: with the value ‘all’ bonds will not be displayed, you should explicitly request bonds.')] = None) -> dict: 
    '''Our Search API for Stocks, ETFs, Mutual Funds, and Indices is one of the best ways to quickly search assets either by code or by company or asset name. The search engine automatically understands if there asset name or code or even ISIN and prioritizes the search fields accordingly. The search engine has several parameters for result ordering. We take into account not only search queries but also market capitalization and the average trading volume for the past period.'''
    url = 'https://eod-historical-data.p.rapidapi.com/search/AAPL'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'bonds_only': bonds_only,
        'exchange': exchange,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bulk_api_for_eod_splits_and_dividends(type: Annotated[Union[str, None], Field(description='General bulk (batch) API for EOD, Splits, and Dividends')] = None,
                                          date: Annotated[Union[str, datetime, None], Field(description='By default, the data for last trading day will be downloaded, but if you need any specific date, add ‘date’ parameter to the URL, in the following example we used September 21, 2017')] = None,
                                          symbols: Annotated[Union[str, None], Field(description='To download last day data for several symbols, for example, for MSFT and AAPL, you can add the ‘symbols’ parameter. For non-US tickers, you should use the exchange code, for example, BMW.XETRA or SAP.F')] = None,
                                          filter: Annotated[Union[str, None], Field(description='If you need more data, like company name, you can use this parameter and get an extended dataset, which includes company name, EMA 50 and EMA 200 and average volumes for 14, 50 and 200 days.')] = None,
                                          fmt: Annotated[Union[str, None], Field(description='The output format. Possible values are ‘csv’ for CSV output and ‘json’ for JSON output. Default value: ‘csv’.')] = None) -> dict: 
    '''This API allows to easily download the data for the **entire exchange** for a particular day. It works for end-of-day historical data feed as well as for splits and dividends data. For US tickers you can also use NYSE, NASDAQ, BATS, or AMEX as exchange symbols to get data only for NYSE or only for NASDAQ exchange. With this entire stock market API endpoint, you need not perform thousands and thousands of API requests per day. It’s not necessary anymore. We developed a bulk download API endpoint, and it’s easy to **download historical data for any day in bulk**.'''
    url = 'https://eod-historical-data.p.rapidapi.com/eod-bulk-last-day/US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'date': date,
        'symbols': symbols,
        'filter': filter,
        'fmt': fmt,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_price_data_api(fmt: Annotated[Union[str, None], Field(description='The output format. Possible values are ‘csv’ for CSV output and ‘json’ for JSON output. Default value: ‘csv’.')] = None,
                         period: Annotated[Union[str, None], Field(description='Use ‘d’ for daily, ‘w’ for weekly, ‘m’ for monthly prices. By default, daily prices will be shown.')] = None,
                         order: Annotated[Union[str, None], Field(description='Use ‘a’ for ascending dates (from old to new), ‘d’ for descending dates (from new to old). By default, dates are shown in ascending order.')] = None,
                         _from: Annotated[Union[str, datetime, None], Field(description='Date from.')] = None,
                         to: Annotated[Union[str, datetime, None], Field(description='Date to.')] = None) -> dict: 
    '''With End-of-Day data API, we have data for more than 150 000 tickers all around the world. We cover all US stocks, ETFs, and Mutual Funds (more than 51 000 in total) **from the beginning**, for example, the Ford Motors data is from Jun 1972 and so on. And non-US stock exchanges we cover mostly from Jan 3, 2000. We do provide daily, weekly and monthly data raw and adjusted to splits and dividends.'''
    url = 'https://eod-historical-data.p.rapidapi.com/eod/MCD.US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fmt': fmt,
        'period': period,
        'order': order,
        'from': _from,
        'to': to,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def live_stock_prices_api(fmt: Annotated[Union[str, None], Field(description='The output format. Possible values are ‘csv’ for CSV output and ‘json’ for JSON output. Default value: ‘csv’.')] = None,
                          s: Annotated[Union[str, None], Field(description='With this parameter you will be able to get data for multiple tickers at one request, all tickers should be separated with a comma. We do not recommend using more than 15-20 tickers per request.')] = None,
                          filter: Annotated[Union[str, None], Field(description='If you need only one field, just use this parameter. For examples, if you use the following filter=close then only one number will be returned: 172.5. Which is very useful for Excel WEBSERVICE function like this: =WEBSERVICE(\\"https://eodhistoricaldata.com/api/real-time/AAPL.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&fmt=json&filter=close\\")')] = None) -> dict: 
    '''We provide live (delayed) stock prices API for all subscribers of ‘All-World’, ‘All World Extended’, and ‘ALL-IN-ONE’ plans. With this API endpoint, you are able to get delayed (15-20 minutes) information about almost all stocks on the market. ### Major features - We support **almost all symbols** and exchanges all around the world. - Prices are provided with **15-20 minutes delay**. - We provide only a **1-minute interval** within this API, then you will get prices only with 1-minute frequency. - **Multiple tickers** with one request. - **Supports Excel WEBSERVICE**.'''
    url = 'https://eod-historical-data.p.rapidapi.com/real-time/AAPL.US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fmt': fmt,
        's': s,
        'filter': filter,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def fundamental_data_api(filter: Annotated[Union[str, None], Field(description='The API supports field filtering with this parameter. We support multi-layer filtering. It’s also possible to use several, comma-separated, filters. For example: General::Code,General,Earnings ')] = None) -> dict: 
    '''Simple access to fundamental data API for stocks, ETFs, Mutual Funds, and Indices from different exchanges and countries. Almost all major US, UK, EU, India, and Asia exchanges. Stocks, ETFs, Mutual Funds fundamental data Major US companies supported from 1985, more than 30 years and non-US symbols supported from 2000, it’s more than 21 years of the financial data. Symbols from major US exchanges (around 11000 tickers in total from NYSE, NASDAQ, and ARCA) 20 years both yearly and quarterly. For minor companies, we have data for the last 6 years and the previous 20 quarters. And the data is continually growing. We support more than 20.000 US Funds. Our database has equity funds as well as balanced and bond-based mutual funds. We also support details for more than 10,000 ETFs from different exchanges and countries. We provide Index Constituents (or Index Components) data for all major indices all around the world. Please note, not all companies report the whole financial data, then we can not guarantee that each company will have all data endpoints we do support. Due to a very complex data structure, we support fundamental data feeds only in JSON format.'''
    url = 'https://eod-historical-data.p.rapidapi.com/fundamentals/AAPL.US'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'filter': filter,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def calendar_upcoming_earnings_trends_ipos_and_splits(_from: Annotated[Union[str, datetime, None], Field(description='The start date for earnings data, if not provided, today will be used.')] = None,
                                                      to: Annotated[Union[str, datetime, None], Field(description='The end date for earnings data, if not provided, today + 7 days will be used.')] = None,
                                                      symbols: Annotated[Union[str, None], Field(description='You can request specific symbols to get historical and upcoming data. If ‘symbols’ used, then ‘from’ and ‘to’ parameters will be ignored. You can use one symbol: ‘AAPL.US’ or several symbols separated by a comma: ‘AAPL.US, MS’. REQUIRED for Earnings Trends.')] = None,
                                                      fmt: Annotated[Union[str, None], Field(description='Output format, possible values: ‘csv’ – for CSV output and ‘json’ – for JSON output. The data for trends is available only in JSON format due to a complex data structure. Default value is ‘csv’ for others.')] = None) -> dict: 
    '''With our Financial Calendar data feed, we provide data about upcoming earnings, IPOs, and splits. If you are looking for an economic calendar, which includes an earnings calendar and IPOs calendar, this API is for you. To get access to Calendar API you should be subscribed either to Calendar API or to the ‘All-In-One’ data package, which includes all possible data feeds we have. More information with prices you can get on our main page. For IPOs we have dated from January 2015 and up to 2-3 weeks in the future. For splits, we have data from January 2015 up to several months in the future and full historical data is provided under our Splits and Dividends API. And for earnings, we have data from the beginning and up to several months in the future.'''
    url = 'https://eod-historical-data.p.rapidapi.com/calendar/earnings'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from': _from,
        'to': to,
        'symbols': symbols,
        'fmt': fmt,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bonds_fundamentals_and_historical_api(CUSIP_or_ISIN: Annotated[str, Field(description='CUSIP of a particular bond, it’s also could be an ISIN. Other IDs are not supported at the moment.')]) -> dict: 
    '''We support US corporate bonds and Government Bonds in our database (for government bonds, see [Economic Data API](https://eodhistoricaldata.com/financial-apis/economic-data-api/)). There are always new corporate bonds on the market, if you didn’t find any particular bond, please contact us and we will add the data within 24 hours. Bonds fundamentals and historical data could be accessed either via ISIN or via CUSIP IDs. Other IDs are not supported at the moment.'''
    url = 'https://eod-historical-data.p.rapidapi.com/bond-fundamentals/910047AG4'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'CUSIP_or_ISIN': CUSIP_or_ISIN,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def macroeconomics_data_and_macro_indicators_api(indicator: Annotated[Union[str, None], Field(description='Defines which macroeconomics data indicator will be shown. See the list of possible indicators here.')] = None,
                                                 fmt: Annotated[Union[str, None], Field(description='The output format could be ‘json’ for JSON and ‘csv’ for CSV output. The default value is ‘json’.')] = None) -> dict: 
    '''Macroeconomics is a part of economics dealing with the performance, structure, behavior, and decision-making of an economy as a whole. Our Macroeconomics Data API includes regional, national, and global economies. We provide the data for more than 30 macro indicators such as GDP, unemployment rates, national income, price indices, inflation rates, consumption, international trades, and many other significant indicators. The Macroeconomics Data API is a part of Fundamental API and accessible under Fundamental subscription. Each Macroeconomics API request consumes 1 API call. To get macroeconomics indicators use the following URL: > https://eodhistoricaldata.com/api/macro-indicator/COUNTRY?api_token=YOUR_API_TOKEN&fmt=json&indicator=inflation_consumer_prices_annual **COUNTRY**: String. REQUIRED. Defines the country for which the indicator will be shown. The country should be defined in the Alpha-3 ISO format. Possible values: USA, FRA, DEU… **api_ token**: String. REQUIRED. Your api_token to access the API. You will get it after registration. **indicator**: String. OPTIONAL. Defines which macroeconomics data indicator will be shown. See the list of possible indicators below. The default value is ‘gdp_current_usd‘. **fmt**: String. OPTIONAL. The output format could be ‘json’ for JSON and ‘csv’ for CSV output. The default value is ‘json’.'''
    url = 'https://eod-historical-data.p.rapidapi.com/macro-indicator/FRA'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'indicator': indicator,
        'fmt': fmt,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def insider_transactions_api(limit: Annotated[Union[int, float, None], Field(description='The limit for entries per result, from 1 to 1000. Default value: 100. Default: 0')] = None,
                             _from: Annotated[Union[str, datetime, None], Field(description='Date from. Default value – one year ago.')] = None,
                             to: Annotated[Union[str, datetime, None], Field(description='Date to. Default value – the current date.')] = None,
                             code: Annotated[Union[str, None], Field(description='To get the data only for Apple Inc (AAPL), use AAPL.US or AAPL ticker code. By default, all possible symbols will be displayed.')] = None) -> dict: 
    '''The insider transactions API data is available for all US companies that report Form 4 to SEC. Insider trading involves trading in a public company’s stock by someone who has non-public, material information about that stock for any reason. In some cases, insider transactions could be very useful for making investment decisions. The Insider Transactions Data API is a part of Fundamental API and accessible under Fundamental subscription. Each Insider Transactions API request consumes 1 API call.'''
    url = 'https://eod-historical-data.p.rapidapi.com/insider-transactions'
    headers = {'x-rapidapi-host': 'eod-historical-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'from': _from,
        'to': to,
        'code': code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
