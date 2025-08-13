#!/usr/bin/env python3
"""Simple Binance trading bot.

DISCLAIMER:
- Cryptocurrency trading involves significant risk.
- Use this script for learning purposes only.
- Test thoroughly (preferably on Binance testnet) before real trades.
"""

import getpass
from binance.client import Client
from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_MARKET


def create_client() -> Client:
    """Prompt for API credentials and create a Binance Client."""
    api_key = input("Enter Binance API Key: ").strip()
    api_secret = getpass.getpass("Enter Binance API Secret: ").strip()
    if not api_key or not api_secret:
        raise ValueError("Both API key and secret are required.")
    return Client(api_key, api_secret)


def place_market_order(client: Client, symbol: str, side: str, quantity: float):
    """Place a market order via Binance API."""
    side_enum = SIDE_BUY if side.lower() == "buy" else SIDE_SELL
    order = client.create_order(
        symbol=symbol.upper(),
        side=side_enum,
        type=ORDER_TYPE_MARKET,
        quantity=quantity,
    )
    return order


def main() -> None:
    """Run the bot once: prompt for order details and execute."""
    client = create_client()
    symbol = input("Symbol (e.g., BTCUSDT): ").strip()
    side = input("Side (buy/sell): ").strip().lower()
    quantity = float(input("Quantity: "))
    order = place_market_order(client, symbol, side, quantity)
    print("Order executed:", order)


if __name__ == "__main__":
    main()
