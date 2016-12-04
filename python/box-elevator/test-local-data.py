#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import time
import sys

thread_local = threading.local()


class MyThread(threading.Thread):

    def __init__(self, inc=1):
        self.inc = inc
        super(MyThread, self).__init__()
        self.local = thread_local

    def run(self):
        for x in range(0, 10 * self.inc, self.inc):
            time.sleep(1)
            self.local.thread_var = str(x)
            sys.stdout.write(threading.current_thread().name +
                             " => thread_var=" + self.local.thread_var + "\n")

if __name__ == "__main__":
    a = MyThread(1)
    a.start()

    b = MyThread(10)
    b.start()

    try:
        while True:
            time.sleep(0.1)
            if not (a.is_alive() and b.is_alive()):
                break
    except KeyboardInterrupt:
        sys.stdout.write("Exited")