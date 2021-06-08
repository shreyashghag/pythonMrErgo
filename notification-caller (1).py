import schedule
import time
import notify as n

def job():
    try:
        n.notification()
    except KeyboardInterrupt:
        exit()
schedule.every(5).seconds.do(job) #calls the notification every 5 seconds

while 1:
    schedule.run_pending()
    time.sleep(1)