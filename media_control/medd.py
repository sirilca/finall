import webbrowser

# Replace "YOUR_YOUTUBE_LINK" with the actual YouTube link you want to open
youtube_link = "https://www.youtube.com/watch?v=yubzJw0uiE4"

# Open the link in a web browser like Chrome
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open(youtube_link)
