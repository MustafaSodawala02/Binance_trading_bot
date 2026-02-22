# Binance Futures Testnet Trading Bot

Professional Python trading bot developed for Binance USDT-M Futures Testnet with CLI interface, logging, and error handling.

---

## Live Features

* Execute MARKET orders
* Execute LIMIT orders
* Execute STOP orders (Bonus Feature)
* Supports BUY and SELL
* Command Line Interface (CLI)
* Structured logging system
* Exception handling and validation
* Testnet-safe trading

---

## Tech Stack

* Python 3.10+
* Binance Futures REST API
* Requests
* Python-Dotenv
* Logging module

---

## Project Structure

```
bot/
client.py
validators.py
logging_config.py

cli.py
requirements.txt
logs/bot.log
```

---

## Setup Instructions

Clone repository

```
git clone https://github.com/yourusername/binance-futures-trading-bot.git
```

Install dependencies

```
pip install -r requirements.txt
```

Create .env file

```
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
```

---

## Usage

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 50000
```

### STOP Order

```
python cli.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.002 --price 50000 --stopPrice 51000
```

---

## Logs

Logs are stored in:

```
logs/bot.log
```

Includes:

* Request details
* Response details
* Error handling

---

## Testnet

Connected to Binance Futures Testnet:

https://testnet.binancefuture.com

No real money involved.

---

## Assignment Submission

Developed as part of Python Developer Internship Assignment.

---

## Author

Mustafa

GitHub: https://github.com/MustafaSodawala02

LinkedIn: https://linkedin.com/in/mustafa-sodawala-9b928337b/

---

## License
MIT License

---
MIT License

---
