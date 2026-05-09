from collections import deque
from statistics import mean
from datetime import datetime

from app.services.telegram_bot import TelegramBot


class SimpleStrategy:

    def __init__(self, fast=5, slow=20):

        self.fast = fast
        self.slow = slow

        self.prices = deque(maxlen=slow)

        self.last_signal = None

        # Telegram Bot instance
        self.bot = TelegramBot()

    def check_signal(self, price):

        self.prices.append(price)

        if len(self.prices) < self.slow:
            return

        fast_ma = mean(list(self.prices)[-self.fast:])
        slow_ma = mean(self.prices)

        print(f"FAST MA: {fast_ma:.2f} | SLOW MA: {slow_ma:.2f}")

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ================= BUY =================
        if fast_ma > slow_ma and self.last_signal != "BUY":

            self.last_signal = "BUY"

            message = f"""
🚀 *BUY SIGNAL CONFIRMED*

━━━━━━━━━━━━━━
📊 Pair: *BTCUSDT*
💰 Price: `{price}`
⚡ Fast MA: `{fast_ma:.2f}`
🐢 Slow MA: `{slow_ma:.2f}`
━━━━━━━━━━━━━━
🕒 Time: `{time_now}`
📈 Action: *ENTER LONG*
━━━━━━━━━━━━━━
"""

            print(message)

            self.bot.send_message(message)

        # ================= SELL =================
        elif fast_ma < slow_ma and self.last_signal != "SELL":

            self.last_signal = "SELL"

            message = f"""
🔻 *SELL SIGNAL CONFIRMED*

━━━━━━━━━━━━━━
📊 Pair: *BTCUSDT*
💰 Price: `{price}`
⚡ Fast MA: `{fast_ma:.2f}`
🐢 Slow MA: `{slow_ma:.2f}`
━━━━━━━━━━━━━━
🕒 Time: `{time_now}`
📉 Action: *ENTER SHORT*
━━━━━━━━━━━━━━
"""

            print(message)

            self.bot.send_message(message)