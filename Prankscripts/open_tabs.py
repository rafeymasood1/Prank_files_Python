# opens 15 sites in full speed

import random
import webbrowser
import time


for i in range(15):
    site = random.choice(['google.com'])
    visit = f"https://{site}"
    webbrowser.open(visit)
    time.sleep(0.1)   # change this to add delay between opening tab
