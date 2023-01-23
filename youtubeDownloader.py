from pytube import YouTube

link= input("plz enter url of your video...")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()