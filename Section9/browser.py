import webbrowser

# webbrowser.open("https://www.python.org", new=1)
#
# help(webbrowser)

# for i in range(10):
# #     print(1,2,3,4,5,6,7,8,9, sep =";", end ="")

# chrome = webbrowser.get('/usr/bin/google-chrome %s').open_new_tab("https://www.python.org/")
# chrome.open_new("https://www.python.org/")


url = 'http://docs.python.org/'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

# Open URL in new window, raising the window if possible.
# webbrowser.open_new(url)