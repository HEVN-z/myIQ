import threading
import time

def doit():
    s = threading.currentThread()
    while getattr(s, "run", True):
        print("Working 1 ")
        time.sleep(.1)
    print("Worker 1 Stopped")

def doit2():
    s = threading.currentThread()
    while getattr(s, "run", True):
        print("Working ---- 2")
        time.sleep(.2)
    print("Worker 2 Stopped")


def main():
    t = threading.Thread(target=doit)
    t.start()
    t2 = threading.Thread(target=doit2)
    t2.start()
    i = 0
    while i < 10:
        print("_____________________________looping")
        print(i)
        i=i+1
        time.sleep(.15)
    time.sleep(5)
    t.run = False
    t2.run = False
 



    

if __name__ == "__main__":
    main()

