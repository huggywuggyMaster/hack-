import webbrowser
import time
runV = True

def runIt():
    link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    while True:
        webbrowser.open_new_tab(link)
        time.sleep(1)  # Wartezeit in Sekunden, bevor der Link erneut geöffnet wird

runIt()
