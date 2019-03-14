# ftp_client
Simple implementation of an ftp client

______How to use:___________________

use python ftpclient.py -h for help and commands
use python ftpclient.py -l to list files
typical usage:
python ftp_client -s server -c username -p password -d -f 100MB.zip 10MB.zip 50MB.zip -o /path/to/downloads

______Features:_____________________

-download files form an ftp server
-upload files to an ftp server
-work with Linux
-work with Windows
-download multiple files sequentially if use pass multiple files name as arguments
-download multiple files concurrently if you use multiple call to ftp_client.py
-upload multiple files sequentially if use pass multiple files name as arguments
-upload multiple files concurrently if you use multiple call to ftp_client.py
-upload and download in the same time with multiple calls (concurrently not implemented yet)
-log:
    downloaded file
    file size
    date
    duration
