# Soundboard for Raspberry Pi
This project contains the source code and board designs for a soundboard for the Raspberry Pi.
I runs on a raspberry pi with multimediacenter Kodi/OSMC. On pressing a button it will pause the current song, play the sound for the button and resume the song from before.

## Structure
* `board-layouts` - Contains Layouts for boards created with the [fritzing App](http://fritzing.org/home/)
* `sounds` - Should contain the `.mp3` files (one for each push button). The files must be named like:
`0.mp3`, `1.mp3`, `2.mp3` and so on.
* `soundboard.py` - The Python source code for controlling the push buttons and playing the sounds

## Get started
* run `sudo python3 soundboard.py` from console