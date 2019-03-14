import sys
import ftplib
import argparse
import sys
import datetime
import time
import os
import ntpath
#Upload directory on the server
u_path = "/maps/"
#download directory on the server
d_path = "/maps/"

def logger(operation, duration, name, size, time):
	log = open("logs.txt", "a+")
        log.write(operation+"\n")
	log.write("Filename: "+ name +"\n")
	log.write("Size: "+ str(size)+" Bytes\n")
        log.write("Date: "+ str(time)+"\n")
	log.write("Duration: "+ str(duration)+" Second\n")
        log.write("\n")
	
def download(file_name, ftp, output, download_path):
	TempFile = open(output+'/'+file_name, "wb") 
	ftp.cwd(download_path)
	start = time.time()
	ftp.retrbinary('RETR '+ file_name, TempFile.write)
	end = time.time()
	TempFile.close()
        logger("*****Download operation*****", end-start,file_name, ftp.size(file_name), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	print file_name+" is downloaded!"

def upload(file_name, ftp, upload_path):
	ftp.cwd(upload_path)
        print upload_path
        #the path format of the file to download must be like this path/file.pdf
	#if we use /path/file.pdf we get an error 
	#so in any case addind "./" will solve the problem any way
	file_name = file_name
	TempFile = open(file_name,"rb")
	#extract the file name from the path, 
	#in anonymous mode the server prevent creating directories in upload just files   
        start = time.time()
	print ntpath.basename(file_name)
	ftp.storbinary("STOR "+ntpath.basename(file_name),TempFile)
        end = time.time()
	logger("*****Upload operation*****", end-start,ntpath.basename(file_name), os.stat(file_name).st_size, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	TempFile.close()
	print ntpath.basename(file_name) + " is uploaded!"



def main(args):
	
	#handle the argument passed on the command line
	parser = argparse.ArgumentParser(description='FTP client for download and upload')

	parser.add_argument('-f', '--name',  type=str, nargs='+', help="file_name")
	parser.add_argument('-s', '--server',default="localhost", type=str,help='host_server')
        parser.add_argument('-c', '--username',default="anonymous", type=str,help='username')
	parser.add_argument('-p', '--password',default="anonymous", type=str,help='password')
        parser.add_argument('-o', '--output',default='.', type=str, help="destination")
	parser.add_argument('-d', '--down', action='store_true', help="download mode")
	parser.add_argument('-u', '--upload', action='store_true', help="upload mode")
        parser.add_argument('-l', '--listing', action='store_true', help="listing files")
        

	args = parser.parse_args()
	# create an ftp object
	ftp = ftplib.FTP(args.server)
	#login with anonymous mode
	ftp.login()
	#get files in the download directory
	files = ftp.nlst(d_path)
        #printing files in the download directory
        if args.listing:
		print "Listing Files:"
                for f in files:
			print f
	#download mode        
	if args.down:
		files = ftp.nlst(d_path)
		for f in args.name:
			#check if the file exist in the download directory
			if d_path+f in files :
				download(f, ftp,args.output,d_path)
			else:
				print f+" doesn't exist "
				print "use python -B ftp_client -l to list files"
	#upload mode
        if args.upload:
		for f in args.name: 
			upload(f, ftp,u_path)
	#close the ftp connection object       
	ftp.quit()

if __name__ == '__main__':
    from sys import argv

    try:
        main(argv)
    #Control-C to exist
    except KeyboardInterrupt:
        pass
    sys.exit()