import yt_dlp

def download_video(url):
    print("Downloading... Please wait")
    options = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
    print("Download Done!")

if __name__ == "__main__":
    print("=== YouTube Downloader ===")
    link = input("Paste YouTube link here: ")
    download_video(link)
