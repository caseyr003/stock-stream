import time
import cx_Oracle
from stock_api import StockAPI
from spinner import LoadingAnimation

# Add stock symbols of the companies you want to monitor
stocks=['ORCL', 'TSLA', 'AAPL', 'MSFT', 'ROKU']

# Update with connection string to your database
conn_string='user/password@host:1521/service_name'

# Initialize stock api to get stock data
api = StockAPI()

# Initialize loading tool with bar animation
spinner=LoadingAnimation('clock')

# Create connection to database
connection = cx_Oracle.connect(conn_string)
cursor = connection.cursor()

def save_price(stock_symbol, day, price, stock_name):
    cursor.execute("insert into stock_history (s_id,  price, read_time, stock_name, " \
                   "stock_symbol) values (stock_history_id_sequence.nextval, %f, '%s', " \
                   "'%s', '%s')" % (price, day, stock_name, stock_symbol))

def save_history(stock_symbol):
    history = api.get_history(stock_symbol, '1m')
    company = api.get_name(stock_symbol)
    for day in history:
        save_price(stock_symbol, day['date'], day['close'], company)

# Start loading animation on the command line
spinner.start()

#Read and write stock history to database
for stock in stocks:
    save_history(stock)
connection.commit()
spinner.stop()
