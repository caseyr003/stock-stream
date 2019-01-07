# Stock Stream

This project pushes real time stock data into a database for stream analytics.

## Built With

* [Python 3](https://www.python.org/)
* [Oracle Database 18c](https://www.oracle.com/technetwork/database/enterprise-edition/downloads/index.html)

## Prerequisites

You will need the following things properly installed on your computer:

* [Git](http://git-scm.com/)
* [Oracle Instant Client](https://www.oracle.com/technetwork/database/database-technologies/instant-client/overview/index.html)

## Installation

* run `git clone https://github.com/caseyr003/stock-stream.git`

## Setup

* use the sql commands in `stock.sql` to set up the table in your Oracle database
* update the `stock_stream.py` file with your Oracle database connection string
* update the stocks in `stock_stream.py`

## Running

To run the project locally follow the following steps:

* change into the project directory
* `python stock_stream.py`
note: this will run a continuous loop until quit

## Credits

Stock data is provided for free from the [IEX Developer Platform](https://iextrading.com/developer/)