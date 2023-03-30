import os
import ctypes
import random

SPI_SETDESKWALLPAPER = 20
wallpaper_dir = "C:\puhau\PS4\SHARE\Screenshots\Miles_Morales"
wallpapers = os.listdir(wallpaper_dir)
random_wallpaper = os.path.join(wallpaper_dir, random.choice(wallpapers))
ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER, 0, os.path.abspath(random_wallpaper), 0)