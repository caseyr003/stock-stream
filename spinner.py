import itertools
import threading
import time
import sys

#Spinning dots animation
dots = [
    "⠸",
    "⠼",
    "⠴",
    "⠦",
    "⠧",
    "⠇",
    "⠏",
    "⠋",
    "⠙",
    "⠹"
]

#Clock animation
clock = [
    "🕐 ",
    "🕑 ",
    "🕒 ",
    "🕓 ",
    "🕔 ",
    "🕕 ",
    "🕖 ",
    "🕗 ",
    "🕘 ",
    "🕙 ",
    "🕚 "
]

class LoadingAnimation():
    def __init__(self, style='dots'):
        self.style = style
        self.complete = False
        self.animation = dots
        if style == 'clock':
            self.animation = clock

    def animate(self):
        for i in itertools.cycle(self.animation):
            sys.stdout.write('\r' + i)
            sys.stdout.flush()
            time.sleep(0.2)
            if self.complete:
                break
        sys.stdout.write('\rComplete')

    def start(self):
        threading.Thread(target=self.animate).start()

    def stop(self):
        self.complete = True
