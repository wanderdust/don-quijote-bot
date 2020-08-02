import telepot
from telepot.loop import MessageLoop
import time
from bot import start_text


def handle(msg):
    print(msg['text'])
    chat_id = msg['chat']['id']
    reply = start_text(msg['text'])

    bot.sendMessage(chat_id, reply)

bot = telepot.Bot('1279257134:AAFsWVHYth9xVKt-Pg5_NU4xs8-Dm4h9LW0')

MessageLoop(bot, handle).run_as_thread()
print( 'I am listening ...')

while 1:
    time.sleep(10)
