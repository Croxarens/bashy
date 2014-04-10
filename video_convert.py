#!/usr/bin/env python
import argparse
import os
import time
import subprocess
import psutil	# sudo pip install psutil OR sudo apt-get install python-psutil
# http://stackoverflow.com/questions/20027440/psutil-module-not-fully-working-on-debian-7

def listFile(root, ext):
# It returns all the files found which has the -f value as extension.
# The returned value is an array.

	ext = "." + ext
	fileList = []
	for root, dirs, files in os.walk(root):
		for file in files:
			if file.endswith(ext):
				#print os.path.abspath(os.path.join(root, file))
				fileList.append({
					#"source" : os.path.abspath(os.path.join(root, file)),
					#"output" : os.path.splitext(file)[0],
					"fileName" : os.path.splitext(file)[0],
					"filePath" : os.path.abspath(root)
				})
	print fileList
	return fileList

def routine(fileList):
# It repeats the actions until all the list items are not done

	index		=	0				# List pointer
	endIndex	=	len(fileList)	# End of the list
	
	while index < endIndex :
		''' The number of PIDs (items) is the number of process running/active.
			This number must be less then the number of CPUs
		'''
		if len(PIDs) < cpu :
			run(fileList[index])
			index += 1
		checkProcesses()
		time.sleep(2)


def run(var) :
# Create and run the command in a new shell
# The process ID (PID) will be added to the PIDs array

	sor	=	var['filePath'] + "/" + var['fileName'] + "." + extFrom
	out	=	var['filePath'] + "/" + var['fileName'] + "." + extTo
	cmd	=	'ffmpeg -v quiet -i "' + sor + '" "' + out + '" && rm "' + sor + '" && exit'
	if v : print cmd
	pid	= subprocess.Popen(cmd, shell=True).pid
	PIDs.append(pid)


def checkProcesses() :
# Check if the processes in PIDs array are active.
# If the process is a ZOMBIE, kill it and remove it from the PIDs array.
# If the process is NOT FOUND, remove it from the PIDs array.

	for process in PIDs :
		theProcess	=	isProcessAlive(process)
		if v : print("The process " + str(process) + " is : " + theProcess)
		if theProcess == psutil.STATUS_ZOMBIE :
			if v : print "Zombie found, we are going to kill PID " + str(process)
			psutil.Process(process).kill()
			PIDs.remove(process)
		elif theProcess == 'PROCESS NOT FOUND' :
			if v : print "Process not FOUND. It will be removed from the list"
			PIDs.remove(process)

		
def isProcessAlive(pid):
# Check the status of the process passed

	if v : print 'Is the process ' + str(pid) + ' exist? ' + str(psutil.pid_exists(pid))
	if psutil.pid_exists(pid) :	# http://stackoverflow.com/questions/568271/how-to-check-if-there-exists-a-process-with-a-given-pid
		p = psutil.Process(pid)
		if v : print str(pid) + " : " + p.status()
		return p.status()
	else :
		return 'PROCESS NOT FOUND'
	


def main():
# Check value passed and run the routine if everything is OK

	parser = argparse.ArgumentParser(
		prog='Video Converter',
		description='It use the ffmpeg program.',
		epilog="Epilog")
	
	parser.add_argument("-v", "--verbose", help="verbose", action='store_true')
	parser.add_argument("-f", metavar='FILE-EXT', help="the source extension files.", required=True)
	parser.add_argument("-t", metavar='FILE-EXT', help="the output extension files.", required=True)
	parser.add_argument("-F", "--folder", metavar='FOLDER', help="the folder where the file.", nargs='?', default=None, const='.')
	parser.add_argument("-cpu", help="number of CPU used. By default, all the CPU are used, so there will be a process of each CPU.", type=int)
	
	args = parser.parse_args()
	
	''' Instantiate Global Variables '''
	
	global v, cpu, folder, extFrom, extTo, PIDs
	
	v		=	args.verbose	# If the execution is verbose or not (bool)
	extFrom	=	args.f			# Extension to find/source (str)
	extTo	=	args.t			# Extension to convert/output (str)
	PIDs	=	[]				# Processes List active (array)
	
	if v : print(args)
	if v : print("CPU(s) avaible : " + str(cpuN))
	if args.cpu :
		if v : print("User want use " + str(args.cpu) + " CPU(s)")
		if args.cpu > cpuN or args.cpu < 0:
			print('\033[31m\033[1mError : The -cpu parameter is too high or too low for this system.\033[0m')
			quit()
		else :
			cpu = args.cpu
	else :
		cpu = cpuN
	if v : print("The program is going to use " + str(cpu) + " CPU(s)")
	
	if args.folder :
		folder = args.folder
	else :
		folder = "."
		
	
	if v : print 'The script PID is ' + str(os.getpid())	# ps --ppid PID-NUMBER
	
	'''	Run the program '''
	routine( listFile(folder, extFrom) )
	
	
if __name__ == '__main__':
	if os.name != 'posix':
		print('\033[31m\033[1mError : The system in use is not supported.\033[0m')
		quit()
	
	global cpuN
	cpuN = int(os.sysconf('SC_NPROCESSORS_ONLN'))
	if cpuN == 0:
		print('\033[31m\033[1mError : Impossible reading CPU info.\033[0m')
		quit()
	
	main()
	
	'''
	# http://stackoverflow.com/a/3964691
	for root, dirs, files in os.walk("."):
		for file in files:
			if file.endswith(".txt"):
				print os.path.abspath(os.path.join(root, file))
	# Execute bash
	# http://linux.byexamples.com/archives/366/python-how-to-run-a-command-line-within-python/
	# http://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
	'''
	
	'''
	Check if the number of CPU the user want to use is less then the
	number of CPU of the system.
	'''


'''
FIXME:
ffmpeg -v quiet -i "/home/luigitaccetta/tmp/convert/Business/Building an Integrated Online Marketing Plan/4. The Four Parts of a Successful Online Marketing Strategy Social Sharing/126059_MM30_04_01_FaceBook.mp4" "/home/luigitaccetta/tmp/convert/Business/Building an Integrated Online Marketing Plan/4. The Four Parts of a Successful Online Marketing Strategy Social Sharing/126059_MM30_04_01_FaceBook.webm" && rm "/home/luigitaccetta/tmp/convert/Business/Building an Integrated Online Marketing Plan/4. The Four Parts of a Successful Online Marketing Strategy Social Sharing/126059_MM30_04_01_FaceBook.mp4" && exit
Traceback (most recent call last):
  File "names.py", line 115, in <module>
    main()
  File "names.py", line 100, in main
    routine( listFile(folder, extFrom) )
  File "names.py", line 32, in routine
    checkProcesses()
  File "names.py", line 45, in checkProcesses
    if isProcessAlive(process) == psutil.STATUS_ZOMBIE :
  File "names.py", line 51, in isProcessAlive
    p = psutil.Process(pid)
  File "/usr/local/lib/python2.7/dist-packages/psutil/__init__.py", line 296, in __init__
    self._init(pid)
  File "/usr/local/lib/python2.7/dist-packages/psutil/__init__.py", line 331, in _init
    raise NoSuchProcess(pid, None, msg)
psutil.NoSuchProcess: no process found with pid 12507
luigitaccetta@crunchbang:~/tmp/convert$ Stream mapping:
  Stream #0.0 -> #0.0
  Stream #0.1 -> #0.1
Press ctrl-c to stop encoding
frame= 9814 fps= 11 q=0.0 Lsize=    8902kB time=392.56 bitrate= 185.8kbits/s    
video:4757kB audio:3872kB global headers:4kB muxing overhead 3.121127%
frame=11170 fps= 10 q=0.0 Lsize=   10956kB time=446.80 bitrate= 200.9kbits/s    
video:6275kB audio:4374kB global headers:4kB muxing overhead 2.846288%
frame=13513 fps= 16 q=0.0 Lsize=   15140kB time=540.52 bitrate= 229.5kbits/s    
video:9295kB audio:5460kB global headers:4kB muxing overhead 2.590892%
'''
