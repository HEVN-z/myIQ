import signal
import sys

def signal_handler(signal, frame):
    print ('You pressed Ctrl+C - or killed me with -2')
    #.... Put your logic here .....
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)