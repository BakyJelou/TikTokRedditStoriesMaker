from moviepy.editor import *
from colorama import *
import random
import pyfiglet
import os.path

init()
print("\nTikTok Reddit video maker by")
print(Fore.YELLOW + pyfiglet.figlet_format("BakyJelou"))
print(Style.RESET_ALL + "\nTrying to find visuals...")
if os.path.isfile("assets/background.mp4"):
    background = VideoFileClip("assets/background.mp4")
    print("background.mp4 [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
else:
    print("background.mp4 [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add background.mp4 to the folder")
    exit()

if os.path.isfile("assets/title.png"):
    title = ImageClip("assets/title.png")
    print("title.png [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
else:
    print("title.png [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add title.png to the folder")
    exit()

if os.path.isfile("assets/text.png"):
    text = ImageClip("assets/text.png")
    print("text.png [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
else:
    print("text.png [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add text.png to the folder")
    exit()

print(Style.RESET_ALL + "\nTrying to find Text-To-Speech...")
if os.path.isfile("assets/tts_title.mp3"):
    tts_title = AudioFileClip("assets/tts_title.mp3")
    print("tts_title.mp3 [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
else:
    print("tts_title.mp3 [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add tts_title.mp3 to the folder")
    exit()

if os.path.isfile("assets/tts_text.mp3"):
    tts_text = AudioFileClip("assets/tts_text.mp3")
    print("tts_text.mp3 [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
else:
    print("tts_text.mp3 [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add tts_text.mp3 to the folder")
    exit()

print("\nProcessing data...")
totallength = tts_title.duration + 1 + tts_text.duration

subclip_starttime = random.uniform(0,background.duration - totallength)

backgroundclip = background.subclip(subclip_starttime,subclip_starttime + totallength)

print("Processing audio...")
audio_output = CompositeAudioClip([tts_title.set_start(0),tts_text.set_start(tts_title.duration + 1)])

print("Processing video...,\n")
title = title.set_start(0)
title = title.set_end(tts_title.duration)
text = text.set_start(tts_title.duration)
video_output = CompositeVideoClip([backgroundclip,title.set_position("center"),text.set_position("center")])
video_output.audio = audio_output
video_output.duration = totallength
print("Length of your video will be: ",totallength," seconds")
print("Do you want to render the video? (ENTER)")
input()

video_output.write_videofile("video.mp4",)



