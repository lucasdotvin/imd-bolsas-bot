import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', hours=2)
def main():
    print('[!] Starting crawling.')
    os.system('python -m scrapy crawl imdnews')
    print('[!] Ending crawling.')

    print('[!] Sending messages.')
    os.system('python app.py')
    print('[!] Messages sended.')

sched.start()
