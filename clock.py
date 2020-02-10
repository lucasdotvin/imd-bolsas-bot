import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=2)
def main():
    print('[!] Starting crawling.')
    subprocess.run(['python -m scrapy crawl imdnews'])
    print('[!] Ending crawling.')

    print('[!] Sending messages.')
    subprocess.run(['python script.py'])
    print('[!] Messages sended.')

sched.start()
