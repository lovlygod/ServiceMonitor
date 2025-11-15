import logging
import requests
from telegram import Bot
from telegram.error import TelegramError

class TelegramNotifier:
    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id
        self.bot = Bot(token=token)
        self.logger = logging.getLogger(__name__)

    async def send_message(self, message: str):
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message)
            self.logger.info(f"Сообщение отправлено в чат {self.chat_id}")
        except TelegramError as e:
            self.logger.error(f"Ошибка при отправке сообщения через Telegram: {e}")
        except Exception as e:
            self.logger.error(f"Неизвестная ошибка при отправке сообщения: {e}")

    def send_message_sync(self, message: str):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            'chat_id': self.chat_id,
            'text': message
        }
        
        try:
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                self.logger.info(f"Сообщение отправлено в чат {self.chat_id}")
            else:
                self.logger.error(f"Ошибка при отправке сообщения: {response.status_code}")
        except Exception as e:
            self.logger.error(f"Ошибка при отправке сообщения: {e}")