from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

# file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")
    else:
        locationError.config(text="Please choose a folder", fg="red")

# download video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if (len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if (choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif (choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension="mp4").last()
        elif (choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Past Link again", fg="red")

    # download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed")

root = Tk()
root.title("YT DOWNLOADER")
root.geometry("500x500")
root.columnconfigure(0, weight=1)  # set all content in center

# Link label
ytdLabel = Label(root, text="Enter the URLof the Video", font=("jost", 15))
ytdLabel.grid()

# Entry box for link
ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar)
ytdEntry.grid()

# Error Message
ytdError = Label(root, text="Error Message", fg="red", font=("jost", 10))
ytdError.grid()

# Asking save file label
saveLabel = Label(root, text="Save the Video File", font=("jost", 15, "bold"))
saveLabel.grid()

# btn of save file
saveEntry = Button(root, width=10, bg="red", fg="white", text="Choose path", command=openLocation)
saveEntry.grid()

# Error Msg location
locationError = Label(root, text="Error Msg of Path", fg="red", font=("jost", 10))
locationError.grid()

# Download
choices = ["720p", "144p", "Only Audio"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid()

# download btn
downloadbtn = Button(root, text="Download", width=10, bg="red", fg="white", command=DownloadVideo)
downloadbtn.grid()

# developer Label
developerLabel = Label(root, text="Dream Developers", font=("jost", 15))
developerLabel.grid()


root.mainloop()
