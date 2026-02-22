
import argparse, os
from dotenv import load_dotenv
from bot.client import BinanceClient
from bot.validators import validate_order
from bot.logging_config import setup_logging

load_dotenv()
setup_logging()

parser = argparse.ArgumentParser(description="Premium Trading Bot")
parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True, help="MARKET, LIMIT, STOP")
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")
parser.add_argument("--stopPrice")

args = parser.parse_args()

validate_order(args.type, args.price)

client = BinanceClient(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_API_SECRET")
)

result = client.place_order(
    args.symbol, args.side, args.type, args.quantity, args.price, args.stopPrice
)

print("\nOrder Result:")
print(result)
