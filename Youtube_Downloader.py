# Must instal pytube by typling "pip3 install pytube" into terminal to run

from pytube import YouTube
from sys import argv

link = argv[1] # Inserts youtube linnk into the comand line / position [1] bc [0] will be occupied by project name 
yt = YouTube(link) #

print("Title: ", yt.title) # Displays title of Video
print("View: ", yt.views) # Displays views of Video

yd = yt.streams.get_highest_resolution() # Retrives the highest quality of video

yd.download(r'[FILE LINK GOES HERE') # Downloads into file in bracket

# To download Youtube Video
# - In the terminal type [python Youtube_Downloader.py "(inset link here)"]