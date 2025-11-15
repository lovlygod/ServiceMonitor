# ServiceMonitor

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Python-скрипт для мониторинга системных сервисов с уведомлениями через Telegram.

## Описание

ServiceMonitor - это утилита для мониторинга системных сервисов, которая периодически проверяет, работают ли указанные сервисы (например, nginx, mysql, docker) на сервере. Если сервис падает или перестаёт отвечать, скрипт отправляет уведомление через Telegram.

Это полезно для DevOps и системных администраторов, а также для проектов с собственными серверами.

## Особенности

- Проверка статуса сервисов с использованием subprocess
- Уведомления через Telegram
- Логирование в файл с отметкой времени
- Возможность настройки через конфигурационный файл
- Поддержка Linux систем
- Возможность запуска без токена Telegram (для тестирования)
- Поддержка большого количества системных сервисов

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/lovlygod/ServiceMonitor.git
cd ServiceMonitor
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте конфигурационный файл config.yaml:
   - Укажите сервисы для мониторинга
   - Добавьте токен Telegram бота
   - Укажите ID чата для уведомлений
   - Настройте интервал проверки

## Использование

Запустите скрипт:
```bash
python servicemonitor.py
```

## Конфигурация

Пример файла config.yaml:
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

## Поддерживаемые сервисы

ServiceMonitor может отслеживать статус большого количества системных сервисов, включая:

- Веб-серверы: nginx, apache2
- Базы данных: mysql, postgresql, mongodb
- Системные службы: ssh, cron, rsyslog
- Сетевые службы: bind9 (DNS), postfix (почта)
- Службы безопасности: fail2ban, ufw, apparmor
- И другие популярные сервисы

## Стек технологий

- Python 3.11+
- Библиотеки: python-telegram-bot, PyYAML, subprocess, logging

## Лицензия

Этот проект лицензирован под MIT License - смотрите файл [LICENSE](LICENSE) для подробностей.

## Вклад в проект

Если вы хотите внести свой вклад в проект, пожалуйста, сначала обсудите изменения, которые вы хотите внести, через issue или email.

## Автор

lovlygod

## Поддержка

Если у вас есть какие-либо вопросы или проблемы, пожалуйста, создайте issue в репозитории.