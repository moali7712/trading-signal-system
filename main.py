import asyncio

from app.websocket.binance_socket import run_socket

if __name__ == "__main__":
    asyncio.run(run_socket())