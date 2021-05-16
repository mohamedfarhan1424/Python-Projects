from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

top = Tk()
top.geometry('500x400')
top.title("Farhan Youtube Video Downloader")
top.resizable(0, 0)
top.columnconfigure(0, weight=1)
top.configure(bg="cyan")
Label(top, text="Video Downloader", font="Broadway 25 bold", fg="lightgreen", bg="black").grid()
link = StringVar()
folder_name = ""
location = Entry(top, width=40)
location.grid()


def openLocation():
    global folder_name
    global location
    folder_name = filedialog.askdirectory()
    location.insert(0, "")
    location.insert(0, folder_name)


Label(top, text="Select the Folder to save:", font="rockwell 15", fg="blue", bg="yellow").grid()
Button(top, text="Browse", font="rockwell 10", command=openLocation, fg="black", bg="white").grid()
Label(top, text="Paste the link here", font="rockwell 20 bold", fg="blue", bg="yellow").grid()
link_enter = Entry(top, width=70, textvariable=link)
link_enter.grid()

choices = ['720p', '480p', '360p', '240p', '144p', 'mp3']
Label(top, text="Select Quality", font="rockwell 15 bold", fg="skyblue", bg="black").grid()
ytdchoice = ttk.Combobox(top, values=choices)
ytdchoice.grid()

label1 = Label(top, text="")
label2 = Label(top, text="")
label3 = Label(top, text="")


def downloader():
    global label1, label2, label3
    global video
    global folder_name
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label1 = Label(top, text="")
    label2 = Label(top, text="")
    label3 = Label(top, text="")
    try:
        choice = ytdchoice.get()
        if choice == choices[0]:
            a = []
            url = YouTube(str(link.get()))
            for i in url.streams.filter(progressive=True):
                a.append(str(i.resolution))
            video = url.streams.filter(progressive=True).get_by_resolution('720p')
            if video is not None:
                if folder_name == "":
                    label1.config(text="Please Select Correct location", font="rockwell 15", fg="yellow",
                                  bg="black")
                    label1.grid()
                else:
                    video.download(output_path=folder_name)
                    label1.config(text="DOWNLOADED", font="rockwell 15", fg="green", bg="lightgreen")
                    label1.grid()
            else:
                label1.config(text="Please select different quality", font="rockwell 15", fg="yellow", bg="black")
                label1.grid()
                label2.config(text="Available resolutions:", font="rockwell 15", fg="blue", bg="black")
                label2.grid()
                label3.config(text=a, font="rockwell 10", fg="yellow", bg="black")
                label3.grid()
        elif choice == choices[1]:
            a = []
            url = YouTube(str(link.get()))
            for i in url.streams.filter(progressive=True):
                a.append(str(i.resolution))
            video = url.streams.filter(progressive=True, file_extension='mp4').get_by_resolution('480p')
            if video is not None:
                if folder_name == "":
                    label1.config(text="Please Select the Storing location", font="rockwell 15", fg="yellow",
                                  bg="black")
                    label1.grid()
                else:
                    video.download(output_path=folder_name)
                    label1.config(text="DOWNLOADED", font="rockwell 15", fg="green", bg="lightgreen")
                    label1.grid()
            else:
                label1.config(text="Please select different quality", font="rockwell 15", fg="yellow", bg="black")
                label1.grid()
                label2.config(text="Available resolutions:", font="rockwell 15", fg="blue", bg="black")
                label2.grid()
                label3.config(text=a, font="rockwell 10", fg="yellow", bg="black")
                label3.grid()
        elif choice == choices[2]:
            a = []
            url = YouTube(str(link.get()))
            for i in url.streams.filter(progressive=True):
                a.append(str(i.resolution))
            video = url.streams.filter(progressive=True, file_extension='mp4').get_by_resolution('360p')
            if video is not None:
                if folder_name == "":
                    label1.config(text="Please Select the Storing location", font="rockwell 15", fg="yellow",
                                  bg="black")
                    label1.grid()
                else:
                    video.download(output_path=folder_name)
                    label1.config(text="DOWNLOADED", font="rockwell 15", fg="green", bg="lightgreen")
                    label1.grid()
            else:
                label1.config(text="Please select different quality", font="rockwell 15", fg="yellow", bg="black")
                label1.grid()
                label2.config(text="Available resolutions:", font="rockwell 15", fg="blue", bg="black")
                label2.grid()
                label3.config(text=a, font="rockwell 10", fg="yellow", bg="black")
                label3.grid()
        elif choice == choices[3]:
            a = []
            url = YouTube(str(link.get()))
            for i in url.streams.filter(progressive=True):
                a.append(str(i.resolution))
            video = url.streams.filter(progressive=True, file_extension='mp4').get_by_resolution('240p')
            if video is not None:
                if folder_name == "":
                    label1.config(text="Please Select the Storing location", font="rockwell 15", fg="yellow",
                                  bg="black")
                    label1.grid()
                else:
                    video.download(output_path=folder_name)
                    label1.config(text="DOWNLOADED", font="rockwell 15", fg="green", bg="lightgreen")
                    label1.grid()
            else:
                label1.config(text="Please select different quality", font="rockwell 15", fg="yellow", bg="black")
                label1.grid()
                label2.config(text="Available resolutions:", font="rockwell 15", fg="blue", bg="black")
                label2.grid()
                label3.config(text=a, font="rockwell 10", fg="yellow", bg="black")
                label3.grid()
        elif choice == choices[4]:
            a = []
            url = YouTube(str(link.get()))
            for i in url.streams.filter(progressive=True):
                a.append(str(i.resolution))
            video = url.streams.filter(progressive=True, file_extension='mp4').get_by_resolution('144p')
            if video is not None:
                if folder_name == "":
                    label1.config(text="Please Select the Storing location", font="rockwell 15", fg="yellow",
                                  bg="black")
                    label1.grid()
                else:
                    video.download(output_path=folder_name)
                    label1.config(text="DOWNLOADED", font="rockwell 15", fg="green", bg="lightgreen")
                    label1.grid()
            else:
                label1.config(text="Please select different quality", font="rockwell 15", fg="yellow", bg="black")
                label1.grid()
                label2.config(text="Available resolutions:", font="rockwell 15", fg="blue", bg="black")
                label2.grid()
                label3.config(text=a, font="rockwell 10", fg="yellow", bg="black")
                label3.grid()

        elif choice == choices[5]:
            a = []
            url = YouTube(str(link.get()))
            for i in url.streams.filter(progressive=True):
                a.append(str(i.resolution))
            video = url.streams.filter(only_audio=True).first()
            if video is not None:
                if folder_name == "":
                    label1.config(text="Please Select the Storing location", font="rockwell 15", fg="yellow",
                                  bg="black")
                    label1.grid()
                else:
                    video.download(output_path=folder_name)
                    label1.config(text="DOWNLOADED", font="rockwell 15", fg="green", bg="lightgreen")
                    label1.grid()
            else:
                label1.config(text="Please select different quality", font="rockwell 15", fg="yellow", bg="black")
                label1.grid()
                label2.config(text="Available resolutions:", font="rockwell 15", fg="blue", bg="black")
                label2.grid()
                label3.config(text=a, font="rockwell 10", fg="yellow", bg="black")
                label3.grid()
        else:
            label1.config(text="Please Select the Quality", font="rockwell 15", fg="red", bg="black")
            label1.grid()
    except Exception as e:
        label1.config(text="Give Link Correctly", font="rockwell 15", fg="black", bg="red")
        label1.grid()
        print(e)


Button(top, text="DOWNLOAD", font="rockwell 20", bg="lightgreen", command=downloader, padx=2).grid()

top.mainloop()
