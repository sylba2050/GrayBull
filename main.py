from pytube import YouTube

yt = YouTube('https://youtu.be/-sUXMzkh-jI')

s = yt.streams.all()
for i in s:
    print (i)

yt.streams.first().download()
