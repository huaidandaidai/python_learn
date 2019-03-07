import time
import threading


def greet(index):
    print("Hello World-%d"%index)
    time.sleep(0.5)


def line_run():
    for x in range(5):
        greet(x)


def thread_run():
    for x in range(5):
        th = threading.Thread(target=greet, args=[x])
        th.start()


if __name__ == '__main__':
    # line_run()
    thread_run()