# rdt - browse Reddit media through mpv

rdt is a Bash script that downloads media from your favorite subreddits and lets you browse through them in the media player [mpv](https://mpv.io). You can very simply and quickly select what to view through [dmenu](https://tools.suckless.org/dmenu/).

## Dependencies
- [mpv](https://github.com/mpv-player/mpv)
- [dmenu](https://github.com/stilvoid/dmenu)
- [python-mpv](https://github.com/jaseg/python-mpv)
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [curl](https://github.com/curl/curl)
- [jq](https://github.com/stedolan/jq)

## Installation

You will have to register an app to be able to use Reddit's API [here](https://ssl.reddit.com/prefs/apps). No worries, the process is very quick.
Then, clone the repository:
```
git clone https://github.com/rickboks/rdt
```

You have to tell rdt where its files are located. Put this in your .bashrc (or .zshrc, or whatever).
```
export RDT_DIR=/path/to/rdt
```
You might also want to put rdt in your PATH. Now, fill in all the fields in the ```config``` file.
Once that's done, authenticate the script to use your Reddit account. This only needs to be done once.

```
./rdt auth
```
Now, you should be ready to use rdt. You can optionally add/remove entries in the ```subs``` file. This file contains the subreddits you can choose from. Simply run:

```
./rdt
```
... and dmenu shows you the subreddits you have specified in the ```subs``` file. It will additionally ask you how to sort the posts (hot, new, top, etc.).
The inital buffering may take a second, depending on the size of the media to be downloaded, but the following pages will always be downloaded in the background. The keybindings for the mpv viewer are:

Action | Key
-------|-----
next post | j
previous post | k
show post title | t
save media | s
next page | n
quit | q
