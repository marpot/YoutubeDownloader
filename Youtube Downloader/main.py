from pytube import YouTube
import vlc
import pafy

url = 'https://www.youtube.com/watch?v=7BXJIjfJCsA'
my_video = YouTube(url)

#creating pafy object of the video
video = pafy.new(url)

#getting best stream
best = video.getbest()

#creating vlc media player object
media = vlc.MediaPlayer(best.url)

#start playing video
media.play()

print('***************Video Title***********')

print(my_video.title)