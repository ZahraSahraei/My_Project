from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube,request
from tkinter import messagebox
from tkinter.ttk import Progressbar
import sys
import time


def open_location():
    global folder_location
    folder_location = filedialog.askdirectory()
    if len(folder_location) > 1:
        lbl_location.config(text=folder_location, fg='green')
    else:
        lbl_location.config(text='please choose folder!', fg='red')

def download_video():

    global file_size,filesize_MB,stream,downloaded,chunk
    global video_type
    global folder_location
    downloaded=0

    btn_download['state'] = 'disabled'

    try:
        choice = cb.get()
        url = entry_url.get()

        if len(url) > 1:
            lbl_error.config(text='')
           # print(url, "at", folder_location)

            yt_url = YouTube(url)
            yt_url.register_on_progress_callback(progress)

            # print("Video Name is:\n",yt_url.title)
            lbl_title.config(text="Video Name is: %s"%(yt_url.title))

            #720p Video file downloading...
            if choice == choices[0]:
                video_type = yt_url.streams.filter(progressive=True).first()

            #144p video file downloading...
            elif choice == choices[1]:
                video_type = yt_url.streams.filter(progressive=True, file_extension='mp4').last()

            # audio file downloading...
            elif choice == choices[2]:
                video_type = yt_url.streams.filter(only_audio=True).first()

            file_size = video_type.filesize
            filesize_MB = file_size / 1024000

            stream = request.stream(video_type.url)  # get an iterable stream

            chunk = next(stream, None)  # get next chunk of video

        else:
            lbl_error.config(text='please paste link!', fg='red')

        # now Download ------->
        video_type.download(folder_location)

    except Exception as e:
        print(e)
        btn_download['state'] = 'normal'
        entry_url.delete(0, 'end')
        lbl_location.config(text='')
     

previousprogress = 0
def progress(stream, chunk, bytes_remaining):

    lbl_loading.config(text='Downloading ...')

    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    percent_count = (int)(bytes_downloaded / total_size * 100)
    lbl_percent.config(text=str(percent_count) + '%')

    downloaded_MB = int(bytes_downloaded / 1024000)
    lbl_filesize.config(text="{:00.00f} MB / {:00.00f} MB".format(downloaded_MB, filesize_MB))

    if percent_count > previousprogress:
        previousprogress = percent_count
        time.sleep(0.02)
        pb['value'] =percent_count
        pb.update()
        # win.update_idletasks()

    if percent_count==100:
        complete()

def complete():
    btn_download['state'] = 'normal'
    messagebox.showinfo('info', 'download completed!')

    pb.stop()
    pb.grid_forget()
    lbl_percent.config(text='')
    lbl_loading.config(text='')
    lbl_title.config(text='')
    lbl_filesize.config(text='')
    entry_url.delete(0,'end')
    lbl_location.config(text='')
    cb.config(state='readonly')

win = Tk()
win.title("Youtube Downloader")
win.geometry("360x550")
win.resizable(False, False)
win.iconbitmap("Youtube.ico")

win.columnconfigure(0, weight=1)  # set all content in center

# create link label
lb_url = Label(win, text="Enter the URL of the Video:")
lb_url.pack()
lb_url.config(font=('mitra', 10, 'bold'), fg='blue')
lb_url.config(justify='center', pady=20)

# entry for url
entry_url_var = StringVar()
entry_url = Entry(win, width=45, textvariable=entry_url_var)
entry_url.pack()

# error message
lbl_error = Label(win, font=('mitra', 10))
lbl_error.config(justify='center', pady=8)
lbl_error.pack()

# Asking save file label
save_label = Label(win, text="Save the Video File:")
save_label.pack()
save_label.config(font=('mitra', 10, 'bold'), fg='blue', pady=10)

# btn of choose path for save file
btn_save = Button(win, text='Choose Path')
btn_save.config(width=15, height=2, bg='#ffb3fe', fg='blue', command=open_location)
btn_save.pack(padx=7, pady=7)

# Error Message Location
lbl_location = Label(win, text='', fg='red', font=('mitra', 10))
lbl_location.config(justify='center', pady=11)
lbl_location.pack()

# Download Quality
lbl_quality = Label(win, text='Select Quality:', font=('mitra', 8))
lbl_quality.pack()
lbl_quality.config(font=('mitra', 10, 'bold'), fg='blue', pady=15)

# Combo Box
n = StringVar()
cb = ttk.Combobox(win, width=22, textvariable=n)
choices = ['MP4_720p', 'Mp4_144p', 'Song_MP3']
cb = ttk.Combobox(win, values=choices)
cb.config(state='readonly')
# or :

# Adding combobox drop down list
# cb['values'] = ('720p','128p','only audio')
# cb.config(state='readonly')
cb.pack()

# download Button
btn_download = Button(win, text='Download')
btn_download.config(width=18, height=2, bg='#ffb3fe', fg='blue', justify='center', command=download_video)
# btn_download.bind("<Button-2>",download_video)
btn_download.pack(padx=25, pady=25)

lbl_loading = Label(win, text="", font=("mitra", 10), fg='green',justify='center')
lbl_loading.pack()

pb = Progressbar(win, orient='horizontal', length=300, mode='determinate')
pb.config(maximum=100)
pb.pack()

lbl_percent = Label(win, fg='green', font=('mitra', 10))
lbl_percent.pack()

lbl_title= Label(win, text="",fg='blue', font=('mitra', 10))
lbl_title.pack()

lbl_filesize=Label(win, text="",fg='blue', font=('mitra', 10))
lbl_filesize.pack()

win.mainloop()
