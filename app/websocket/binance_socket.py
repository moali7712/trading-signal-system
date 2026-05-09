import asyncio
import json
import websockets

from app.engine.strategy_engine import StrategyEngine
from app.strategies.simple_strategy import SimpleStrategy

BINANCE_WS_URL = (
    "wss://stream.binance.com:9443/ws/btcusdt@trade"
)

engine = StrategyEngine()

engine.add_strategy(
    SimpleStrategy(
        fast=5,
        slow=20
    )
)


async def run_socket():

    while True:

        try:

            async with websockets.connect(
                BINANCE_WS_URL
            ) as websocket:

                print("=" * 50)
                print("✅ CONNECTED TO BINANCE")
                print("=" * 50)

                while True:

                    response = await websocket.recv()

                    data = json.loads(response)

                    price = float(data['p'])

                    print(f"BTC PRICE => {price}")

                    engine.process(price)

        except Exception as error:

            print("=" * 50)
            print("❌ SOCKET ERROR")
            print(error)
            print("🔄 RECONNECTING IN 5 SECONDS...")
            print("=" * 50)

            await asyncio.sleep(5)