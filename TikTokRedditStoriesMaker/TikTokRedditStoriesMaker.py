from time import thread_time_ns
from moviepy.editor import *
from colorama import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import pyttsx3
import random
import pyfiglet
import os.path

init()
print("\nTikTok Reddit video maker by")
print(Fore.YELLOW + pyfiglet.figlet_format("BakyJelou"))
tts_engine = "none";
if input("Do you want to use in-built TTS engine? (Y/N): ") == "Y":
    tts_engine = "inbuilt"
else:
    tts_engine = "custom"
print(Style.RESET_ALL + "\nTrying to find visuals...")
if os.path.isfile("assets/background.mp4"):
    background = VideoFileClip("assets/background.mp4")
    print("background.mp4 [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
else:
    print("background.mp4 [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add background.mp4 to the folder")
    exit()

if os.path.isfile("assets/title.jpg"):
    title = ImageClip("assets/title.jpg")
    print("title.jpg [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
else:
    print("title.jpg [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add title.jpg to the folder")
    exit()

if os.path.isfile("assets/text.jpg"):
    text = ImageClip("assets/text.jpg")
    print("text.jpg [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
else:
    print("text.jpg [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add text.jpg to the folder")
    exit()

print(Style.RESET_ALL + "\nTrying to find Text-To-Speech...")
if tts_engine == "inbuilt":
    if os.path.isfile("assets/txt_title.txt"):
        txt_title = open("assets/txt_title.txt",'r',encoding="utf-8").read()
        print("txt_title.txt [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
    else:
        print("txt_title.txt [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add txt_title.txt to the folder")
        exit()

    if os.path.isfile("assets/txt_text.txt"):
        txt_text = open("assets/txt_text.txt",'r',encoding="utf-8").read()
        print("txt_text.txt [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
    else:
        print("txt_text.txt [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add txt_text.txt to the folder")
        exit()
else:
    if os.path.isfile("assets/tts_title.mp3"):
        tts_title = AudioFileClip('assets/tts_title.mp3')
        print("tts_title.mp3 [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
    else:
        print("tts_title.mp3 [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add tts_title.mp3 to the folder")
        exit()

    if os.path.isfile("assets/tts_text.mp3"):
        tts_text = AudioFileClip('assets/tts_text.mp3')
        print("tts_text.mp3 [" + Fore.GREEN + "✔️" + Style.RESET_ALL +"]")
    else:
        print("tts_text.mp3 [" + Fore.RED + "❌" + Style.RESET_ALL +"]" + " not found, please add tts_text.mp3 to the folder")
        exit()


if tts_engine == "inbuilt":
    print("\nProcessing Text-To-Speech...")
    engine = pyttsx3.init()
    rate = engine.getProperty('rate') 
    engine.setProperty('rate', rate-70)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(txt_title,'assets/temp/tts_title.wav')
    engine.runAndWait()
    engine.save_to_file(txt_text,'assets/temp/tts_text.wav')
    engine.runAndWait()

    ffmpeg_extract_audio('assets/temp/tts_title.wav','assets/tts_title.mp3')
    ffmpeg_extract_audio('assets/temp/tts_text.wav','assets/tts_text.mp3')

    tts_title = AudioFileClip('assets/tts_title.mp3')
    tts_text = AudioFileClip('assets/tts_text.mp3')

print("Processing data...")
totallength = tts_title.duration + 1 + tts_text.duration

subclip_starttime = random.uniform(0,background.duration - totallength)

backgroundclip = background.subclip(subclip_starttime,subclip_starttime + totallength)

print("Processing audio...")

audio_output = CompositeAudioClip([tts_title.set_start(0),tts_text.set_start(tts_title.duration + 1)])

print("Processing video...,\n")
title = title.resize(0.95)
title = title.set_start(0)
title = title.set_end(tts_title.duration)
text = text.resize(0.80)
text = text.set_start(tts_title.duration)
video_output = CompositeVideoClip([backgroundclip,title.set_position("center"),text.set_position("center")])
video_output.audio = audio_output
video_output.duration = totallength
print("Length of your video will be: ",totallength," seconds")
print("Do you want to render the video? (ENTER)")
input()

video_output.write_videofile("video.mp4",)



