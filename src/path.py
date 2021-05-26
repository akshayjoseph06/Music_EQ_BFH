import os
from os import path
#print(os.name)

temp=str(path.exists("test.mp3"))
#print(temp)
if bool(str(path.exists("test.mp3")))==True:
	print("Success")


