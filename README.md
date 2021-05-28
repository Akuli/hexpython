# hexpython
This HexChat plugin runs Python code and sends the result to the current channel.
To use it, type `>>> print(1+2)` to a channel,
and it will automatically appear as if you also typed `3` after that.

![screenshot](screenshot.png)

Try without installing:
1. Download `hexpython.py` to your computer. There are several ways to do this (choose one):
    - **Likely easiest way:** Make a new file in a text editor (e.g. Windows notepad), and copy/paste the content there
    - Terminal (not for Windows): `wget https://raw.githubusercontent.com/Akuli/hexpython/main/hexpython.py`
    - Terminal (if you have installed git): `git clone https://github.com/Akuli/hexpython`
    - Click green "Code" button on GitHub, click "Download ZIP", then extract the zip
2. In HexChat, type `/load` and then path to the file. For example, `/load /home/akuli/hexpython/hexpython.py`.

To install so that it auto-loads when HexChat starts, copy `hexpython.py` to HexChat's plugin folder:
- Windows: open "Run" prompt from start menu, type `%appdata%\HexChat\Addons`, drag and drop `hexpython.py` there
- Linux: run `cp path/to/hexpython.py ~/.config/hexchat/addons/`
- MacOS: I have no idea. Please ask help in [GitHub issues](https://github.com/Akuli/hexpython/issues).
