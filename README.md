# python-quick-network-tool
python-quick-network-tool


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

threading ftp server

https://pyftpdlib.readthedocs.io/en/latest/tutorial.html#changing-the-concurrency-model

https://groups.google.com/g/pyftpdlib/c/M-inwEcLbWY

https://code.google.com/p/pyftpdlib/source/browse/tags/release-0.7.0/test/test_ftpd.py#184

https://chromium.googlesource.com/external/pyftpdlib/+/96ffe07c853f1b18a431c1fccb93ff599951dd5f/test/test_ftpd.py



Tkinter pass variable to command button

```python
https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter

```

