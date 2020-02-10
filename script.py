import os
import configs

from lib.imdnewsbot import IMDNewsBot


def main():
    bot = IMDNewsBot(
        channel_id=os.getenv('TELEGRAM_CHANNEL_ID'),
        telegram_token=os.getenv('TELEGRAM_BOT_TOKEN')
    )

    bot.run()


if __name__ == '__main__':
    main()
