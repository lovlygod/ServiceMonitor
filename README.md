<div align="center">
  <h1 style="margin-top: 24px;">💎 ServiceMonitor by @lovlydev</h1>

  <p style="font-size: 18px; margin-bottom: 24px;">
    <b>Python script for monitoring system services with Telegram notifications</b>
  </p>

[Report Bug](https://github.com/lovlygod/ServiceMonitor/issues) · [Request Feature](https://github.com/lovlygod/ServiceMonitor/issues)

</div>

---

## ✨ Features

- 🔍 **Service Status Checking** - Monitor system services using subprocess
- 📱 **Telegram Notifications** - Get alerts when services fail
- 📝 **Logging to File** - Keep track of service status with timestamps
- ⚙️ **Configuration via File** - Easy setup through config.yaml
- 🐧 **Linux System Support** - Optimized for Linux environments
- 🧪 **Test Mode** - Ability to run without Telegram token for testing
- 🚀 **Multiple Services** - Support for monitoring a large number of system services

## 🚀 Quick Start

### 1. Installation

```bash
git clone https://github.com/lovlygod/ServiceMonitor.git
cd ServiceMonitor
pip install -r requirements.txt
```

### 2. Configuration

Copy example configuration and edit:

```bash
cp config.yaml config.yaml
```

Edit `config.yaml` file:

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

### 3. Usage

Run the script:

```bash
python servicemonitor.py
```

## Supported Services

ServiceMonitor can monitor the status of a large number of system services, including:

| Category | Services |
|----------|----------|
| **Web Servers** | nginx, apache2 |
| **Databases** | mysql, postgresql, mongodb |
| **System Services** | ssh, cron, rsyslog |
| **Network Services** | bind9 (DNS), postfix (mail) |
| **Security Services** | fail2ban, ufw, apparmor |
| **Other Services** | docker, redis, elasticsearch, rabbitmq-server |

## Requirements

- Python >= 3.11
- Libraries: python-telegram-bot, PyYAML, subprocess, logging

## License
[MIT](LICENSE)

<div align="center">

### Made with ❤️ by [@lovly](https://t.me/lovlyswag)

**Star ⭐ this repo if you found it useful!**

</div>