import subprocess
import youtube_dl
import clearScreen as c

def fbVideoDownloard(link):
    c.clear_screen()
    print("Is it a public video? ")
    print("1. Yes")
    print("2. No")
    res = input()

    try:
        c.clear_screen()
        if res == '1':
            print("Downloading ...")
            with youtube_dl.YoutubeDL({}) as y:
                y.download([link])
            print("Download Complete!")

        else:
            print("Private video can't download in this version")

    except:
        print("There is an error. Please Run again")

