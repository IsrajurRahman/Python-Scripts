import schedule
import time
import webbrowser

def job_that_executes():
	# For chrome browser in windows
    # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.youtube.com")

    webbrowser.open("https://www.youtube.com")
    print("Opening Website")

schedule.every().day.at('11:58').do(job_that_executes)

while True:
    schedule.run_pending()
    time.sleep(1)

