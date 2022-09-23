# python-quick-network-tool
python-quick-network-tool

# Windows or Linux

Uncomment "build_for" when building for windows or linux.
The difference is windows will use the https://pypi.org/project/hdpitkinter/ for proper scaling to avoid blur text.

# Building

pyinstaller -F --noconsole app.py -n py-quick-network-tool

# DEV STATUS

Python script app.py works well in both windows and linux.

Binary works well with linux. Not working properly in windows.

Change from Tkinter to QTPY next...

# Binaries MD5 Checksum
py-quick-network-tool-ubuntu-64.bin: 6b6a8335e54ebba519a63142d2c38539

# installation

https://www.geeksforgeeks.org/how-to-install-tkinter-in-windows/

for windows

```python
pip install tk

```

```linux
sudo apt install python3-tk

```


on click event

https://stackoverflow.com/questions/61639278/to-detect-button-press-in-python-tkinter-module

```python
def when_clicked():
    #code you want here
    print("Clicked")

button = Button(window,command=when_clicked)

```

# shut down hhtp server

https://stackoverflow.com/questions/12647196/how-do-i-shut-down-a-python-simplehttpserver



threading http server

https://www.reddit.com/r/learnpython/comments/prn3m1/simple_nonblocking_http_server_in_python_3_to/



```python
import threading

from http.server import ThreadingHTTPServer

server = ThreadingHTTPServer(("127.0.0.1", 8000), MyRequestHandler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

```

https://stackoverflow.com/questions/63928479/unable-to-run-python-http-server-in-background-with-threading

```python
import threading
import http.server
import socket 
from http.server import HTTPServer, SimpleHTTPRequestHandler

debug = True
server = http.server.ThreadingHTTPServer((socket.gethostname(), 6666), SimpleHTTPRequestHandler)
if debug:
    print("Starting Server in background")
    thread = threading.Thread(target = server.serve_forever)
    thread.daemon = True
    thread.start()
else:
    print("Starting Server")
    print('Starting server at http://{}:{}'.format(socket.gethostname(), 6666))
    server.serve_forever()

```

Using processes instead of threading

https://superfastpython.com/multiprocessing-in-python/

https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/

```python

# Python program killing
# a thread using multiprocessing
# module
 
import multiprocessing
import time
 
def func(number):
    for i in range(1, 10):
        time.sleep(0.01)
        print('Processing ' + str(number) + ': prints ' + str(number*i))
 
# list of all processes, so that they can be killed afterwards
all_processes = []
 
for i in range(0, 3):
    process = multiprocessing.Process(target=func, args=(i,))
    process.start()
    all_processes.append(process)
 
# kill all processes after 0.03s
time.sleep(0.03)
for process in all_processes:
    process.terminate()
```


threading ftp server

https://pyftpdlib.readthedocs.io/en/latest/tutorial.html#changing-the-concurrency-model

https://groups.google.com/g/pyftpdlib/c/M-inwEcLbWY

https://code.google.com/p/pyftpdlib/source/browse/tags/release-0.7.0/test/test_ftpd.py#184

https://chromium.googlesource.com/external/pyftpdlib/+/96ffe07c853f1b18a431c1fccb93ff599951dd5f/test/test_ftpd.py



Tkinter pass variable to command button

```python
https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter

```

# application path

pyisntaller official get path method

https://stackoverflow.com/questions/404744/determining-application-path-in-a-python-exe-generated-by-pyinstaller

https://pyinstaller.org/en/stable/runtime-information.html

```python
#!/usr/bin/python3
import sys, os
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

```

change simple http server directory

https://stackoverflow.com/questions/31251524/python-simplehttpserver-change-service-directory

```python
import http.server
import socketserver

PORT = 8000
DIRECTORY = "web"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
```