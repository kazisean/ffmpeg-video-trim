import random
import string
from contextlib import redirect_stdout

file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
times_in = ("Enter the start time of where you want the video to be start from. Example: 03:10:00 ")
times_out = (" Enter the end time of where you want the video to be cut out. Example: 03:20:59")
video_name = ("ENTER NAME OF THE VIDEO FILE YOU WANT TO TRIM with the file extention (eample : testvideo.mp4)")

w = open("Enter the file where you want your ffmpeg code to be written it must be a .bat file. Make sure to edit the file with first and start it with @echo off. Example: D:\Vod Review\Reviews\commands.bat", "a")  # append mode
w.write("\n")
w.write("ffmpeg -i " + video_name + " -ss: " + times_in + " -to " + times_out + " -c:v copy -c:a copy " + file_name +".mp4")
w.close()
    
