from pytube import YouTube

YouTube('https://youtu.be/-sUXMzkh-jI').streams.first().download()
