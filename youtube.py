from pytube import YouTube, Playlist
import clearScreen as c

def downloadPlaylist(link):
    c.clear_screen()
    try:
        playlist = Playlist(link)
        count = 0
        for video in playlist.videos:
            video_title = video.title
            count += 1
            video_title = f'''{count}. {video_title}.mp4'''
            print("Downloading... : " + video_title)
            video.streams.get_highest_resolution().download(filename=video_title)
            print("Download Completed!")

        print("DOWNLOADED THE FULL PLAYLIST!")
    except:
        print("There is an error. Please Run again")


def downloadVideo(link):
    c.clear_screen()
    try:
        video = YouTube(link)
        video_title = video.title
        print("Downloading... : " + video_title)
        video.streams.get_highest_resolution().download()
        print("Download Completed!")

    except:
        print("There is an error. Please Run again")


