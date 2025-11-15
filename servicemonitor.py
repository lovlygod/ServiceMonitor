import asyncio
import subprocess
import sys
import os
import logging
import yaml
import time
import socket
from pathlib import Path
from datetime import datetime
from utils.notifier import TelegramNotifier

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/servicemonitor.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class ServiceMonitor:
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        self.config = self.load_config()
        telegram_token = self.config.get('telegram_token')
        telegram_chat_id = self.config.get('telegram_chat_id')
        
        if telegram_token and telegram_chat_id and telegram_token != "ВАШ_TOKEN" and telegram_chat_id != "ВАШ_CHAT_ID":
            self.notifier = TelegramNotifier(
                token=telegram_token,
                chat_id=telegram_chat_id
            )
            self.telegram_enabled = True
        else:
            self.telegram_enabled = False
            logger.warning("Telegram уведомления отключены - не указан токен или chat_id")
        self.previous_status = {}

    def load_config(self):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            logger.error(f"Файл конфигурации {self.config_path} не найден")
            sys.exit(1)
        except yaml.YAMLError as e:
            logger.error(f"Ошибка при чтении конфигурации: {e}")
            sys.exit(1)

    def check_service_status(self, service):
        try:
            result = subprocess.run(
                service['check_command'],
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if 'systemctl' in service['check_command']:
                return result.returncode == 0 and result.stdout.strip() == 'active'
            else:
                return result.returncode == 0
        except subprocess.TimeoutExpired:
            logger.error(f"Таймаут при проверке сервиса {service['name']}")
            return False
        except Exception as e:
            logger.error(f"Ошибка при проверке сервиса {service['name']}: {e}")
            return False

    async def check_all_services(self):
        """Проверяет статус всех сервисов из конфига"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"Начало проверки сервисов в {current_time}")
        
        for service in self.config['services']:
            name = service['name']
            is_running = self.check_service_status(service)
            
            if name in self.previous_status:
                if self.previous_status[name] and not is_running:
                    hostname = socket.gethostname()
                    message = f"⚠ Сервис {name} остановлен на сервере {hostname}"
                    logger.warning(message)
                    if self.telegram_enabled:
                        await self.notifier.send_message(message)
                elif not self.previous_status[name] and is_running:
                    hostname = socket.gethostname()
                    message = f"✅ Сервис {name} запущен на сервере {hostname}"
                    logger.info(message)
                    if self.telegram_enabled:
                        await self.notifier.send_message(message)
            else:
                logger.info(f"Сервис {name} {'работает' if is_running else 'не работает'}")
            
            self.previous_status[name] = is_running
        
        logger.info("Проверка сервисов завершена")

    def run(self):
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        interval = self.config.get('interval', 60)
        
        logger.info("Запуск ServiceMonitor")
        
        try:
            while True:
                asyncio.run(self.check_all_services())
                
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("ServiceMonitor остановлен пользователем")
        except Exception as e:
            logger.error(f"Ошибка в работе ServiceMonitor: {e}")
            sys.exit(1)

def main():
    monitor = ServiceMonitor()
    monitor.run()

if __name__ == "__main__":
    main()