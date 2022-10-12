# Change Log

v1.2.3
- Rearranged HTTP and FTP buttons

v1.2.2
- FTP server is now enabled with TLS. Certificate used is from https://github.com/giampaolo/pyftpdlib/blob/master/demo/keycert.pem given by the official pyftpd documentation https://pyftpdlib.readthedocs.io/en/latest/tutorial.html#ftps-ftp-over-tls-ssl-server
- HTTPS server option is now available.
- PyOpenssl 22.0.0 is installed with pip for SFTP. 22.1.0(current latest) will result in an error.
- HTTP and FTP server status color coded.
- Changed the pyinstaller command. Previous binaries were not packed due to wrong command in README.

v1.2.1
- script will detect if operating is windows or linux. Do not have to manually specify the os when creating the binary with pyinstaller.
- Tkinter window height changed to 500px so that windows can display all items without scrolling.