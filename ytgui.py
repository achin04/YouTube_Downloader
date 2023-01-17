import tkinter as tk
from tkinter import ttk
from pytube import YouTube

class YouTubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader")
        self.geometry("400x150")

        self.label = ttk.Label(self, text="Enter YouTube URL:")
        self.label.pack(pady=10)

        self.url_entry = ttk.Entry(self)
        self.url_entry.pack()

        self.download_button = ttk.Button(self, text="Download", command=self.download)
        self.download_button.pack(pady=10)

    def download(self):
        url = self.url_entry.get()
        try:
            yt = YouTube(url)
            yd = yt.streams.get_highest_resolution()          # Retrives the highest quality of video
            yd.download(r'C:\Saved_YTvideos')      # Downloads into file in bracket
            ttk.Label(self, text="Download complete!").pack()
        except:
            ttk.Label(self, text="Invalid URL or Error Occured").pack()

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()