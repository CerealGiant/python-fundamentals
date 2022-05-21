# File Access modes in python

# Read Only ('r') : The file is opened for reading and the handle is positioned at the beginning of the file. If the file does not exists, raises and I/O error. (DEFAULT MODE)

# Read and Write ('r+') : Opens the file for reading and writing and the handle is positioned at the beginning of the file. If the file does not exists, raises and I/O error. 

# Write Only ('w'): Opens the file for writing. For existing file, the data is truncated and over-written.The handle is positioned at the beginning of the file. File is created if it dosent exist.

#Write and Read('w+'): Open the file for reading and writing.  For existing file, the data is truncated and over-written.The handle is positioned at the beginning of the file. File is created if it dosent exist.

#Append Only ('a'): Opens the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. Data written will be inserted at the end, after the existing data.

#Append and Read('a+'): Opens the file for reading and writing. The file is created if it dosent exist. The handle is positioned at the end of the file. Data written will be inserted at the end, after the existing data.


