# ftp_client
Simple implementation of an ftp client
______What is this:___________________

this is a basic ftp client in python 
works with python 2.7 
using ftplib, standard access with 
anonymous user, simple upload/download functions
exceptions and errors are not handled here
multi threading capabilities not implemented

if you use windows just make sure to add python 
to PATH, or just modify the Downloads and Logs folder paths

lib just contains used functions
in order to make the program more flexible for edition
______How to use:___________________

use python ftpclient.py -h for help and commands
use python ftpclient.py -l to list files
use -u for upload 
use -d for download
use python -B ftp_client to avoid Bytecode generating

typical usage:

python -B ftp_client -d -f 100MB.zip 10MB.zip 50MB.zip -o /path/to/downloads
python -B ftp_client -u -f /path/to/file1.ex  /path/to//file2.pdf


______Features:_____________________

-download files form an ftp server
-upload files to an ftp server
-work with Linux
-work with Windows

-download multiple files sequentially if use pass multiple files name as arguments
 exp: python -B ftp_client -d -f  f1.ext f2.txt f3.mp4

-download multiple files concurrently if you use multiple call to ftp_client.py
exp: terminal1:python -B ftp_client -d -f  f1.ext 
     terminal2:python -B ftp_client -d -f  f2.txt
     terminal3:python -B ftp_client -d -f  f3.mp4
     multi threading downloading not implemented yet


-upload multiple files sequentially if use pass multiple files name as arguments
 exp: python -B ftp_client -u -f  f1.doc f2.mkv f3.pdf

-upload multiple files concurrently if you use multiple call to ftp_client.py
exp: terminal1:python -B ftp_client -u -f  f1.doc 
     terminal2:python -B ftp_client -u -f  f2.mkv
     terminal3:python -B ftp_client -u -f  f3.pdf
     multi-threading uploading not implemented yet

-upload and download in the same time with multiple calls (concurrently not implemented yet)

-log:
    downloaded file
    file size
    date
    duration
