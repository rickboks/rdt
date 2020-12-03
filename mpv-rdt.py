import mpv
from shutil import copy
import sys
import os

path=sys.argv[1]
download_dir=sys.argv[2]

player= mpv.MPV(input_default_bindings=True, 
        input_vo_keyboard=True, 
        image_display_duration="inf", 
        loop_file="inf", 
        fullscreen=True, 
        osc=True,
        shuffle=True)

files=os.listdir(path)
titlefile=open(path + "/titles.dat")
titles={}

def read_titles():
    for line in titlefile:
        vid=line.split(';')[0]
        title="".join(line.split(';')[1:])
        titles[vid]=title

@player.on_key_press('s')
def save_file():
    if not os.path.exists(download_dir) or not os.path.isdir(download_dir):
        show_text("Invalid directory: {}".format(download_dir), 1)
        return
    copy(player.playlist_filenames[player.playlist_pos], download_dir)
    show_text("Saved file to {}".format(download_dir), 1)

@player.on_key_press('j')
def player_next():
    try:
        player.playlist_next()
        show_text("", 1)
    except:
        show_text("Press n to go to next page", 1)

@player.on_key_press('k')
def player_prev():
    try:
        player.playlist_prev()
        show_text("", 1)
    except:
        show_text("Reached first post", 1)

@player.on_key_press('n')
def next_page():
    close()
    print("next")

@player.on_key_press('p')
def prev_page():
    close()
    print("prev")

@player.on_key_press('q')
def _quit():
    close()
    print("quit")

def close():
    player.quit()

def show_text(text, duration):
    player.command("show-text", text, duration*1000)

@player.on_key_press('t')
def display_title():
    current_filename=player.playlist_filenames[player.playlist_pos]
    current_id=current_filename.split("/")[-1].split(".")[0]
    show_text(titles[current_id], 5)

read_titles()
for f in files:
    if f != "titles.dat":
        player.playlist_append("{}/{}".format(path,f))

player.playlist_pos=0
while len(player.playlist) != 0 and player.playlist_pos != None:
    player.wait_for_playback()
player.terminate()
