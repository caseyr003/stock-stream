import time
import datetime
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

def save_price(stock_symbol, ts):
    info = api.get_stock_data(stock_symbol)
    cursor.execute("insert into stock (s_id,  price, read_time, stock_name, " \
                   "stock_symbol) values (stock_id_sequence.nextval, %f, '%s', " \
                   "'%s', '%s')" % (info[0], ts, info[1], stock_symbol))

# Start loading animation on the command line
spinner.start()

#Continuously read and write sensor readings to database
while True:
    ts = datetime.datetime.now()
    for stock in stocks:
        save_price(stock, ts)
    connection.commit()
    time.sleep(3)
