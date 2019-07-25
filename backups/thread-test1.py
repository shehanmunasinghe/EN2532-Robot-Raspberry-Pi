import threading
import time

def loop1_10():
    for i in range(1, 11):
        time.sleep(0.5)
        print(i)

threading.Thread(target=loop1_10).start()

for a in ['a','b','c','d','e']:
        time.sleep(1)
        print(a)