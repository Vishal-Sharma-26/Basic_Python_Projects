from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")
root.maxsize(900, 600)
root.minsize(900, 600)

# List of Image Path
image_paths = [
    r"E:\Python\Python project\Images\software.jpg",
    r"E:\Python\Python project\Images\about-bg.jpg",
    r"E:\Python\Python project\Images\admin-bg.jpg",
    r"E:\Python\Python project\Images\web.jpg",
    r"E:\Python\Python project\Images\robo.jpg",
    r"E:\Python\Python project\Images\home-bg.jpg",
    r"E:\Python\Python project\Images\game.jpg",
    r"E:\Python\Python project\Images\datas.jpg"
]

# Resize the images to 1080x1080
image_size = (700,600)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()