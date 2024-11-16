import os
import sys
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL, CoInitialize
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pygame
import tkinter as tk
from PIL import Image, ImageTk
import threading

def get_resource_path(relative_path):
    try:
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    except Exception as e:
        print(f"Error in get_resource_path: {e}")
        return relative_path

def set_volume_at_level(level, sound_path):
    CoInitialize()

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    is_muted = volume.GetMute()
    if is_muted:
        volume.SetMute(0, None)

    volume.SetMasterVolumeLevel(0.0, None)

    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()

def display_photo(photo_path):
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    root.attributes("-topmost", True)

    img = Image.open(photo_path)
    img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.pack(expand=True)

    root.bind("<Button-1>", lambda e: root.destroy())
    root.mainloop()

def main():
    sound_file_path = get_resource_path('soundfile.mp3')
    photo_file_path = get_resource_path('photo.jpg')     
    volume_level = 0.0

    sound_thread = threading.Thread(target=set_volume_at_level, args=(volume_level, sound_file_path))
    sound_thread.start()

    display_photo(photo_file_path)

if __name__ == "__main__":
    main()
