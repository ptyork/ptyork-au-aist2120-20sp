import argparse
import os
import subprocess
import time, datetime

# Just playing around with the time class here. A LOT
# LOT LOT more useful ways to leverage this in the book.
# start = time.time()      # just a float...seconds since 1/1/1970 12:00 AM
# print(start)
# time.sleep(1.5)          # just hang out for a sec (or 1.5 secs)
# stop = time.time()
# print(stop)
# elapsed = stop - start   # number of seconds since the start (way more on this in the book)
# print(elapsed)

# print(time.ctime())  # "nicely" formatted string for the current time

# Way more on formatting dates and times in the book, including the ability
# to make a time object for a specific date and time.


# argparse module -- super nice way of "interpreting" the arguments passed in
# to the Python script. Use to define a Command Line Interface (CLI) for your 
# script. Good article here: https://realpython.com/command-line-interfaces-python-argparse/

parser = argparse.ArgumentParser(
    prog = "428_unzip_dirs.py",
    description = "A simple script to traverse a directory and unzip all archives"
)

parser.add_argument(
    "path",
    type = str,
    help = "the root of the path to search for archives to extract from"
)

parser.add_argument(
    "--delete",
    "-d",
    help = "remove the archive file when finished extracting the contents",
    action = "store_true"
)

parser.add_argument(
    "--log",
    help = "output to the specified log file",
    type = str
)

args = parser.parse_args()  # this is the "magic" function that interprets all 
                            # of the arguments, including --help.

# just printing out the arguments for "debugging" purposes
print('PATH: ' + args.path)
print('DELETE: ' + str(args.delete))
print("LOG: " + args.log)

os.chdir(args.path)  # change the current working directory for this script to
                     # the argument that was passed in

log_it = len(args.log) > 0   # True if I passed in a log file as an argument

if log_it:
    log_file = open(args.log, 'a')

# for dir, subdirs, files in os.walk(args.path):
for dir, subdirs, files in os.walk('.'):   # "." is fine because we changed CWD above
    print(dir)
    os.chdir(dir)
    for file_name in files:
        print(' '*8 + file_name)
        if file_name.endswith('.zip'):
            if log_it:
                log_file.write(f"{time.ctime()}: Extracted {dir}{os.sep}{file_name}\n")
                # NOTE: os.sep is either "\" or "/" depending on your OS
            proc = subprocess.Popen(['7z.exe', 'x', '-y', file_name])  # launches a sub-process
            proc.wait()   # wait until the sub-process completes
            if args.delete == True:
                os.remove(file_name)
                if log_it:
                    log_file.write(f"{time.ctime()}: Deleted {dir}{os.sep}{file_name}\n")
    os.chdir(args.path)

if log_it:
    log_file.close()
