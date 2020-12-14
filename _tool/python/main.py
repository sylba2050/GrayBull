from pytube import YouTube

yt = YouTube('https://youtu.be/-sUXMzkh-jI')

s = yt.streams.all()
for i in s:
    print(i)

itag = int(input("ダウンロードしたい動画のタグ:"))
yt.streams.get_by_itag(itag).download()
