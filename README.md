
# Premium Binance Futures Testnet Trading Bot

## Features

- MARKET, LIMIT, STOP orders
- CLI interface
- .env support
- Validation
- Structured logging

## Setup

Copy .env.example to .env and add keys

Install:

pip install -r requirements.txt

## Run Examples

MARKET:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT:

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 20000

STOP:

python cli.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.001 --price 20000 --stopPrice 21000

## Logs

logs/bot.log

