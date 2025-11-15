<div align="center">
  <h1 style="margin-top: 24px;">💎 ServiceMonitor от @lovlydev</h1>

  <p style="font-size: 18px; margin-bottom: 24px;">
    <b>Python-скрипт для мониторинга системных сервисов с уведомлениями через Telegram</b>
  </p>

[Сообщить об ошибке](https://github.com/lovlygod/ServiceMonitor/issues) · [Предложить функцию](https://github.com/lovlygod/ServiceMonitor/issues)

</div>

---

## ✨ Особенности

- 🔍 **Проверка статуса сервисов** - Мониторинг системных сервисов с использованием subprocess
- 📱 **Уведомления через Telegram** - Получайте оповещения при сбоях сервисов
- 📝 **Логирование в файл** - Отслеживайте статус сервисов с отметками времени
- ⚙️ **Настройка через файл** - Простая настройка через config.yaml
- 🐧 **Поддержка Linux** - Оптимизировано для Linux-систем
- 🧪 **Тестовый режим** - Возможность запуска без токена Telegram для тестирования
- 🚀 **Несколько сервисов** - Поддержка мониторинга большого количества системных сервисов

## 🚀 Быстрый старт

### 1. Установка

```bash
git clone https://github.com/lovlygod/ServiceMonitor.git
cd ServiceMonitor
pip install -r requirements.txt
```

### 2. Настройка

Скопируйте пример конфигурации и отредактируйте:

```bash
cp config.yaml config.yaml
```

Отредактируйте файл `config.yaml`:

```yaml
services:
  - name: nginx
    check_command: systemctl is-active nginx
  - name: mysql
    check_command: systemctl is-active mysql
  - name: docker
    check_command: systemctl is-active docker
  - name: apache2
    check_command: systemctl is-active apache2
  - name: postgresql
    check_command: systemctl is-active postgresql
  - name: redis
    check_command: systemctl is-active redis
  - name: mongodb
    check_command: systemctl is-active mongodb
  - name: ssh
    check_command: systemctl is-active ssh
  - name: fail2ban
    check_command: systemctl is-active fail2ban
 - name: cron
    check_command: systemctl is-active cron
  - name: ufw
    check_command: systemctl is-active ufw
  - name: rsyslog
    check_command: systemctl is-active rsyslog
  - name: nginx-mainline
    check_command: systemctl is-active nginx-mainline
  - name: php-fpm
    check_command: systemctl is-active php-fpm
  - name: memcached
    check_command: systemctl is-active memcached
  - name: elasticsearch
    check_command: systemctl is-active elasticsearch
  - name: rabbitmq-server
    check_command: systemctl is-active rabbitmq-server
  - name: supervisor
    check_command: systemctl is-active supervisor
  - name: logrotate
    check_command: systemctl is-active logrotate
  - name: unattended-upgrades
    check_command: systemctl is-active unattended-upgrades
  - name: apparmor
    check_command: systemctl is-active apparmor
  - name: postfix
    check_command: systemctl is-active postfix
  - name: vsftpd
    check_command: systemctl is-active vsftpd
  - name: bind9
    check_command: systemctl is-active bind9
  - name: ntp
    check_command: systemctl is-active ntp
telegram_token: "ВАШ_TOKEN"
telegram_chat_id: "ВАШ_CHAT_ID"
interval: 60  # проверка каждые 60 секунд
```

### 3. Использование

Запустите скрипт:

```bash
python servicemonitor.py
```

## Поддерживаемые сервисы

ServiceMonitor может отслеживать статус большого количества системных сервисов, включая:

| Категория | Сервисы |
|----------|----------|
| **Веб-серверы** | nginx, apache2 |
| **Базы данных** | mysql, postgresql, mongodb |
| **Системные службы** | ssh, cron, rsyslog |
| **Сетевые службы** | bind9 (DNS), postfix (почта) |
| **Службы безопасности** | fail2ban, ufw, apparmor |
| **Другие службы** | docker, redis, elasticsearch, rabbitmq-server |

## Требования

- Python >= 3.11
- Библиотеки: python-telegram-bot, PyYAML, subprocess, logging

## Лицензия
[MIT](LICENSE)

<div align="center">

### Сделано с ❤️ от [@lovly](https://t.me/lovlyswag)

**Поставьте ⭐ этому репозиторию, если он оказался полезным!**

</div>