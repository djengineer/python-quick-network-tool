# python-quick-network-tool
python-quick-network-tool

Author: DJENGINEER

For when you need quick **HTTP** and **FTP** servers for file transfers. HTTP and FTP data transfers are not encrypted. Do not use if you require encryption.

The IP address in the second section may differ due to different number of network adapters or adapter names. If you are using for local network, then use your local network ip address, which may start with 192.168.\*\*\*.\*\*\*

Non-standard ports are used so that we do not need administrative permissions to run the binaries.

![python quick network tool](https://github.com/djengineer/python-quick-network-tool/blob/main/screenshot.jpg?raw=true)



# Binaries
The tools are in the binaries folder. The windows binary may be flagged by anti-viruses as Trojan (AVG will do this). 

## Binaries MD5 Checksum
py-quick-network-tool-ubuntu-64.bin: a9e0c14d3d18aae5ec148908b1e28cb0

py-quick-network-tool-win-64.exe: 75899def3fcd9eb78dc0903aa76d3840


# Running as script Windows or Linux

From v1.2.1, the script will detect if the OS is posix(for linux) or nt(for windows). Look at os.name here https://docs.python.org/3/library/os.html.
The difference in implementation is because Windows will use the https://pypi.org/project/hdpitkinter/ for proper scaling to avoid blur text. PSUTIL list sequence is also different when listing network interfaces

```python
# create Python3 virtual environment first.
pip install -r requirements.txt
python app.py

```

# Building from source
```python
pip install -r requirements.txt
pyinstaller -F --noconsole app.py -n py-quick-network-tool
pyinstaller -F --noconsole app.py --upx-dir=./upx-3.96-win64/upx.exe -n py-quick-network-tool
pyinstaller -F --noconsole app.py --upx-dir=./upx-3.96-amd64_linux/upx -n py-quick-network-tool

```



# DEV STATUS

Python script and binaries app.py works well in both windows and linux.




