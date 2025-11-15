# ServiceMonitor

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Python script for monitoring system services with Telegram notifications.

## Description

ServiceMonitor is a utility for monitoring system services that periodically checks whether specified services (e.g., nginx, mysql, docker) are running on the server. If a service crashes or stops responding, the script sends a notification via Telegram.

This is useful for DevOps and system administrators, as well as for projects with their own servers.

## Features

- Service status checking using subprocess
- Telegram notifications
- Logging to file with timestamps
- Configuration via configuration file
- Linux system support
- Ability to run without Telegram token (for testing)
- Support for a large number of system services

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lovlygod/ServiceMonitor.git
cd ServiceMonitor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the config.yaml file:
   - Specify services to monitor
   - Add Telegram bot token
   - Specify chat ID for notifications
   - Set check interval

## Usage

Run the script:
```bash
python servicemonitor.py
```

## Configuration

Example config.yaml file:
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
telegram_token: "YOUR_TOKEN"
telegram_chat_id: "YOUR_CHAT_ID"
interval: 60  # check every 60 seconds
```

## Supported Services

ServiceMonitor can monitor the status of a large number of system services, including:

- Web servers: nginx, apache2
- Databases: mysql, postgresql, mongodb
- System services: ssh, cron, rsyslog
- Network services: bind9 (DNS), postfix (mail)
- Security services: fail2ban, ufw, apparmor
- And other popular services

## Technology Stack

- Python 3.11+
- Libraries: python-telegram-bot, PyYAML, subprocess, logging

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to the project, please discuss the changes you want to make via issue or email first.

## Author

lovlygod

## Support

If you have any questions or issues, please create an issue in the repository.