import threading
import time


def doit(arg):
    s = threading.currentThread()
    while getattr(s, "run", True):
        print ("working on %s" % arg)
        time.sleep(.1)
    print("Thread stopped")


def main():
    t = threading.Thread(target=doit, args=("job",))
    t.start()
    time.sleep(1)
    t.run = False
    

if __name__ == "__main__":
    main()