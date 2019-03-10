import time
import _thread as thread
def loop1():
    print(time.ctime())
    time.sleep(5)
    print(time.ctime())


if __name__ == '__main__':
    print(time.ctime())
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop1,())
    print(time.ctime())
