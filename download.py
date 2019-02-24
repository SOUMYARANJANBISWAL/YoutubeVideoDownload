
#importing the module 
from pytube import YouTube 
from tkinter import *
from tqdm import tqdm
import time
root=Tk()

inputUrl="Url"

def readInput():
	global inputUrl
	inputUrl=textBox.get("1.0","end-1c")

def percent():
	for x in tqdm(range(1000)):
		time.sleep(0.01)
		
def download(): 
	YouTube(inputUrl).streams.first().download('E:/')

def allFunction():
	readInput()
	download()
	percent()
	

root.title("DOWNLOAD")
textBox=Text(root, height=2, width= 50)
textBox.pack()
	
buttonCommit=Button(root, height=1, width=10,
 text="Download",command=lambda: allFunction())
buttonCommit.pack()

mainloop()
