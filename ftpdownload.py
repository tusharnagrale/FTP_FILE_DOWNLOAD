import ftplib

FTP_HOST = "localhost"
FTP_USER = "testuser1"
FTP_PASS = "testuser"

# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"

ftp.dir()

# the name of file you want to download from the FTP server
filename = input("\n enter the name of the file you want to download: \n")

with open(filename, "wb") as file:
    # use FTP's RETR command to download the file
    ftp.retrbinary(f"RETR {filename}", file.write)

    # quit and close the connection
    ftp.quit()