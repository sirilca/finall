from selenium import webdriver
import time

# Replace the video_url with the link of the YouTube video you want to play
video_url = "https://www.youtube.com/watch?v=yubzJw0uiE4"

# Set up the web driver for Chrome
driver = webdriver.Chrome()

# Open the YouTube video
driver.get(video_url)

# Wait for the video to load
time.sleep(5)

# Click the play button


# Wait for the video to finish playing
time.sleep(600)

# Close the browser

# driver.quit()
