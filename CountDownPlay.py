import time as t
import playsound as ps
from config import config

class countdown:
    def __init__(self, time):
        self.time = time
    def play(self, path):
        ps.playsound(path)
    def countdown(self):
        while self.time:
            mins, sec = divmod(self.time, 60)
            timer = '{:02d}:{:02d}'.format(mins, sec)
            print(timer, end='\r')
            t.sleep(1)
            self.time -= 1
        print("BOOOOOOM!!!!!!!!")

time = int(input("Enter the time in seconds: "))
a = countdown(time)
a.countdown()
a.play(config["path"])
