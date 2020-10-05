#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds
from time import sleep


def job_schedulaer(f, time_in_milis):
    time_in_second = time_in_milis/1000
    sleep(time_in_second)
    return f()


def sample():
    print("Hello World")


job_schedulaer(sample, 10000)