import time

def job_scheduler(f, n):
    # convert milliseconds to seconds
    time.sleep(n / 1000)
    f()

def f():
    print("Took long enough!")

job_scheduler(f, 2000)