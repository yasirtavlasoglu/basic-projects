from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import time
from pytube import YouTube
from pytube import Playlist
from tkinter.ttk import Progressbar
from tkinter.scrolledtext import ScrolledText

class YoutubeDownloader():

    def select_v_path(self):
        self.location = askdirectory()

        if self.video_path.get() != "":
            self.video_path.delete(0, END)
            self.video_path.insert(END, self.location)
        else:
            self.video_path.insert(END, self.location)

    def select_p_path(self):
        self.location = askdirectory()

        if self.playlist_path.get() != "":
            self.playlist_path.delete(0, END)
            self.playlist_path.insert(END, self.location)
        else:
            self.playlist_path.insert(END, self.location)

    def download_video(self):
        if self.video_url.get() == "":
            messagebox.showerror("Hata", "Yanlış Video URL")
        elif 'https://' not in self.video_url.get():
            messagebox.showerror("Hata", "Yanlış Video URL")
        elif self.video_path.get() == "":
            messagebox.showerror("Hata", "Lütfen Yolu Belirtin")
        else:
            try:

                self.url = self.video_url.get()
                self.path = self.video_path.get()
                self.video = YouTube(self.url)
                self.stream = self.video.streams.filter(only_audio=False).first()
                print("indirme başladı", self.video.title)

                print("indirme tamamlandı", self.video.title)

                self.root = tk.Tk()
                self.root.geometry('300x150')
                self.root.maxsize(300, 150)
                self.root.minsize(300, 150)
                self.root.title('Video İndirme')
                self.root['bg'] = "white"

                self.start_downloading = Label(self.root, text="Video İndiriliyor...", fg="red",
                                               font=('verdana', 10, 'bold'), bg="white")
                self.start_downloading.place(x=40, y=10)

                self.stream.download(output_path=self.path, filename=None)

                self.progress = Progressbar(self.root, orient=HORIZONTAL, length=250, mode='determinate')
                self.progress['value'] = 20
                self.root.update_idletasks()
                self.progress['value'] = 40
                self.root.update_idletasks()
                self.progress['value'] = 60
                self.root.update_idletasks()
                self.progress['value'] = 80
                self.root.update_idletasks()
                self.progress['value'] = 100
                self.root.update_idletasks()
                self.progress.place(x=20, y=40)

                self.dow_details = ScrolledText(self.root, width=30, height=3, font=('verdana', 8, 'bold'))
                self.dow_details.place(x=20, y=70)
                self.dow_details.insert(END, f'{self.video_path.get()}\n {self.video.title}')

                self.dow_success = Label(self.root, text="Video Başarıyla İndirildi!", fg="red",
                                         font=('verdana', 10, 'bold'), bg="white")
                self.dow_success.place(x=10, y=120)

                self.root.mainloop()

            except:
                time.sleep(10)
                messagebox.showerror("Hata", "Video İndirilemiyor | Bir Şeyler Yanlış Gitti!")

    def download_playlist(self):
        if self.playlist_url.get() == "":
            messagebox.showerror("Hata", "Yanlış Video URL")
        elif 'https://' not in self.playlist_url.get():
            messagebox.showerror("Hata", "Yanlış Video URL")
        elif self.playlist_path.get() == "":
            messagebox.showerror("Hata", "Lütfen Yolu Belirtin")
        else:
            try:
                self.url = self.playlist_url.get()
                self.path = self.playlist_path.get()
                self.playlist = Playlist(self.url)

                self.root = tk.Tk()
                self.root.geometry('300x150')
                self.root.maxsize(300, 150)
                self.root.minsize(300, 150)
                self.root.title('Playlist İndiriliyor')
                self.root['bg'] = "white"

                self.start_downloading = Label(self.root, text="Playlist İndiriliyor...", fg="red",
                                               font=('verdana', 10, 'bold'), bg="white")
                self.start_downloading.place(x=40, y=10)

                for self.video in self.playlist:
                    self.video.streams.get_highest_resolution().download(output_path=self.path, filename=None)

                self.progress = Progressbar(self.root, orient=HORIZONTAL, length=250, mode='determinate')
                self.progress['value'] = 20
                self.root.update_idletasks()
                self.progress['value'] = 40
                self.root.update_idletasks()
                self.progress['value'] = 60
                self.root.update_idletasks()
                self.progress['value'] = 80
                self.root.update_idletasks()
                self.progress['value'] = 100
                self.root.update_idletasks()
                self.progress.place(x=20, y=40)

                self.dow_details = ScrolledText(self.root, width=30, height=3, font=('verdana', 8, 'bold'))
                self.dow_details.place(x=20, y=70)
                self.dow_details.insert(END, f'{self.playlist_path.get()}\n {self.video.title}')

                self.dow_success = Label(self.root, text="Playlist Başarıyla İndirildi!", fg="red",
                                         font=('verdana', 10, 'bold'), bg="white")
                self.dow_success.place(x=10, y=120)

                self.root.mainloop()

            except:
                time.sleep(10)
                messagebox.showerror("Hata", "Video İndirilemiyor | Bir Şeyler Yanlış Gitti!")

    def Clear(self):
        self.video_url.delete(0, END)
        self.video_path.delete(0, END)
        self.playlist_url.delete(0, END)
        self.playlist_path.delete(0, END)

    def Quit(self):
        self.root.destroy()

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x270')
        self.root.maxsize(500, 270)
        self.root.minsize(500, 270)
        self.root['bg'] = "white"
        self.root.title('>yasirtavlasoglu<')

        self.l1 = Label(self.root, text="Youtube İndiricisi", font=('verdana', 15, 'bold'), bg="white", fg="red")
        self.l1.place(x=130, y=5)

        self.design1 = Label(self.root, bg="red", width=20)
        self.design1.place(x=0, y=45)

        self.design2 = Label(self.root, bg="red", width=20)
        self.design2.place(x=360, y=45)

        self.design3 = Label(self.root, bg="red", width=50)
        self.design3.place(x=140, y=45)

        self.yt_icon = ImageTk.PhotoImage(Image.open('youtube.png'))
        self.logo = Label(self.root, image=self.yt_icon, bg="white")
        self.logo.place(x=220, y=100)

        self.frame1 = LabelFrame(self.root, text="Video", width=180, height=180, font=('verdana', 10, 'bold'),
                                 bg="white", fg="red", borderwidth=5, relief=SUNKEN, highlightcolor="red",
                                 highlightbackground="red")
        self.frame1.place(x=10, y=80)

        self.v_url = Label(self.frame1, text="URL", font=('verdana', 10, 'bold'), bg="white")
        self.v_url.place(x=20, y=2)

        self.video_url = Entry(self.frame1, width=24, relief=SUNKEN, borderwidth=2, bg="red", fg="white")
        self.video_url.place(x=10, y=30)

        self.v_path = Label(self.frame1, text="Yolu Seç", font=('verdana', 10, 'bold'), bg="white")
        self.v_path.place(x=10, y=60)

        self.video_path = Entry(self.frame1, width=15, relief=SUNKEN, borderwidth=2, bg="red", fg="white")
        self.video_path.place(x=10, y=90)

        self.file = Button(self.frame1, text="Tarayıcı", font=('verdana', 8, 'bold'), relief=RAISED, bg="pink",
                           command=self.select_v_path)
        self.file.place(x=105, y=88)

        self.download_video = Button(self.frame1, text="İndir", font=('verdana', 9, 'bold'), relief=RAISED,
                                     bg="yellow", borderwidth=4, command=self.download_video)
        self.download_video.place(x=40, y=125)

        self.frame2 = LabelFrame(self.root, text="Oynatma Listesi", width=180, height=180,
                                 font=('verdana', 10, 'bold'), bg="white", fg="red", borderwidth=5, relief=SUNKEN,
                                 highlightcolor="red", highlightbackground="red")
        self.frame2.place(x=310, y=80)

        self.p_url = Label(self.frame2, text="URL", font=('verdana', 10, 'bold'), bg="white")
        self.p_url.place(x=20, y=2)

        self.playlist_url = Entry(self.frame2, width=24, relief=SUNKEN, borderwidth=2, bg="red", fg="white")
        self.playlist_url.place(x=10, y=30)

        self.p_path = Label(self.frame2, text="Yolu Seç", font=('verdana', 10, 'bold'), bg="white")
        self.p_path.place(x=10, y=60)

        self.playlist_path = Entry(self.frame2, width=15, relief=SUNKEN, borderwidth=2, bg="red", fg="white")
        self.playlist_path.place(x=10, y=90)

        self.playlist_file = Button(self.frame2, text="Tarayıcı", font=('verdana', 8, 'bold'), relief=RAISED, bg="pink",
                                    command=self.select_p_path)
        self.playlist_file.place(x=105, y=88)

        self.download_playlist = Button(self.frame2, text="İndir", font=('verdana', 9, 'bold'), relief=RAISED,
                                        bg="yellow", borderwidth=4, command=self.download_playlist)
        self.download_playlist.place(x=40, y=125)

        self.clear = Button(self.root, text="Temizle", font=('verdana', 10, 'bold'), bg="red", fg="white", padx=10,
                            relief=RAISED, borderwidth=3, command=self.Clear)
        self.clear.place(x=205, y=195)

        self.quit = Button(self.root, text="Çıkış", font=('verdana', 10, 'bold'), bg="red", fg="white", padx=15,
                           relief=RAISED, borderwidth=3, command=self.Quit)
        self.quit.place(x=211, y=230)

        self.root.mainloop()

if __name__ == '__main__':
    YoutubeDownloader()

