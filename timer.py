import time

def timer(seconds):
    for i in range(seconds):
        t = i // 60     # minutes
        s = i % 60      # seconds
        print(f"{t} minutes and {s} seconds")
        time.sleep(1)

timer(90)