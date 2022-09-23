# python-quick-network-tool
python-quick-network-tool
Author: DJENGINEER

![python quick network tool](https://github.com/djengineer/python-quick-network-tool/blob/main/screenshot.jpg?raw=true)



# Binaries
The tools are in the binaries folder. The windows binary may be flagged by anti-viruses as Trojan (AVG will do this). 

## Binaries MD5 Checksum
py-quick-network-tool-ubuntu-64.bin: 03d9ae83ba0d13b5e0bea862f0d32c01

py-quick-network-tool-win-64.exe: a4de21c89c964938c0dfd8df75f996f8


# Running as script Windows or Linux

Uncomment "build_for" when building for windows or linux.
The difference is windows will use the https://pypi.org/project/hdpitkinter/ for proper scaling to avoid blur text. PSUTIL list sequence is also different when listing network interfaces

```python
# create Python3 virtual environment first.
pip install -r requirements.txt
python app.py

```

# Building from source
```python
pip install -r requirements.txt
pyinstaller -F --noconsole app.py -n py-quick-network-tool

```



# DEV STATUS

Python script and binaries app.py works well in both windows and linux.




