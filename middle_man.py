import py_compile
import time
while True:
    py_compile.compile('receive_socket.py')
    time.sleep(0.4)