# Write a python program that takes 2 args as input (look that up how to do). The args should be file paths. 
# The program should emulate the cp command (without support for any flags). 
# That means that the program should copy the contents of the first input file over to the second if possible. 
# It should print an error if any of the arguments is missing or inaccessible.
# Command example
# python custom_copy.py /tmp/demo.txt ~/demo.txt
# Bear in mind the files can be large, or even binary. It should work with any file type. It should not exceed 512 MB of RAM
# This task may seem daunting, but it's not.
# The basic idea is to try to open the input file, read it in batches of a fixed buffer size, and 
# before reading the next batch, write it to the output file, while keeping both file descriptors open.
# The last requirement is simply to discourage you from trying to fully load the input file in memory
# Reading line by line may seem like a good idea, but non-text files  (photos, videos, programs, etc) usually don't have that. 
# Even text files offer no guarantees that the text isn't on one line.

import sys

print(f"Name of the script      : {sys.argv[0]=}")
arr = sys.argv[1:]
if len(arr) < 2:
    raise TypeError("Error, did not enter 2 arguments")

print(arr)
try:
    f_text_to_move = open(arr[0], "rb")
except:
  print("Something went wrong when opening the file to read")
try:
    f_combined_text = open(arr[1], "ab")
except:
  print("Something went wrong when opening the file to append")


chunk_size=1024   
while True:
    data = f_text_to_move.read(chunk_size)#.decode("utf-16-le")
    #data = data.decode("utf-16")
    #text = data.read().decode('utf-16-le')
    

    if not data:
        break
    f_combined_text.write(data)



