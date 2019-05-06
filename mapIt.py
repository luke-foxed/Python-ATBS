#!/usr/bin/python3

# mapIt.py - Launches a map in the browser using the address from the command line/clipboard

import webbrowser, sys, pyperclip
from selenium import webdriver
if len(sys.argv) > 1:
    # get the address from the command line 
    address = ' '.join(sys.argv[1:])
else:
    # get the address from the clipboard
    address = pyperclip.paste()

link = 'https://www.google.com/maps/place/' + address
webbrowser.open(link)

