# 🤖 TrueSyncAI Telegram Support Bot

*A powerful, feature-rich Telegram bot that creates a warm, welcoming environment for your community while providing essential group management tools.*

[Features](#-features) • [Quick Start](#-quick-start) • [Configuration](#-configuration) • [Commands](#-commands) • [Documentation](#-documentation) • [Support](#-support)

---

## ✨ Features

### 🎯 Core Functionality
- **🎉 Smart Welcome System** - Automated, personalized greetings for new members
- **📋 Interactive Guidelines** - Easy-to-access group rules and community standards  
- **🤖 Intuitive Commands** - Comprehensive command system with inline keyboards
- **👑 Admin Dashboard** - Powerful administration panel for group management
- **📊 Advanced Logging** - Detailed activity monitoring and error tracking
- **💬 Message Customization** - Fully customizable welcome messages and responses
- **⌨️ Modern UI/UX** - Clean inline keyboards for seamless user interaction

### 🔧 Advanced Features
- **🌍 Multi-language Support** - Localization ready
- **⏰ Scheduled Messages** - Automated announcements and reminders
- **🛡️ Spam Protection** - Built-in anti-spam measures
- **📈 Analytics Dashboard** - Member growth and engagement metrics
- **🔄 Auto-moderation** - Automated content filtering
- **💾 Data Persistence** - SQLite database for storing user preferences
- **🎨 Theme Customization** - Multiple visual themes for bot responses

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- A Telegram account
- Basic knowledge of Telegram bots

### 1. Get Your Bot Token
1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the instructions
3. Copy your bot token (keep it secure!)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/sujalrajpoot/TrueSyncAI-Telegram-Support-Bot.git
cd TrueSyncAI-Telegram-Support-Bot

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
```bash
# Create environment file
cp .env.example .env

# Edit the configuration file
nano .env
```

Fill in your configuration:
```env
BOT_TOKEN=your_bot_token_here
BOT_USERNAME=your_bot_username
GROUP_ID=-1001234567890  # Optional: specific group ID
ADMIN_IDS=123456789,987654321  # Comma-separated admin user IDs
LOG_LEVEL=INFO
WELCOME_DELAY=2  # Delay in seconds before sending welcome message
```

### 4. Setup Your Group
1. Add your bot to your Telegram group
2. Promote the bot to administrator with these permissions:
   - ✅ Delete messages
   - ✅ Restrict members
   - ✅ Pin messages
   - ✅ Add new admins (optional)

### 5. Launch the Bot
```bash
python main.py
```

You should see:
```
2024-09-17 10:30:15 - INFO - Starting TrueSyncAI Telegram Bot...
2024-09-17 10:30:16 - INFO - Bot is running and ready to serve!
```

---

## ⚙️ Configuration

### Environment Variables
| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `BOT_TOKEN` | Your bot token from BotFather | ✅ | None |
| `BOT_USERNAME` | Your bot's username | ✅ | None |
| `GROUP_ID` | Specific group ID (optional) | ❌ | None |
| `ADMIN_IDS` | Comma-separated admin user IDs | ✅ | None |

| `LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | ❌ | `INFO` |
| `WELCOME_DELAY` | Delay before welcome message (seconds) | ❌ | `2` |
| `MAX_WELCOME_LENGTH` | Maximum welcome message length | ❌ | `1000` |

### Customization Files
- **`config/messages.py`** - Customize all bot messages and responses
- **`data/guidelines.txt`** - Define your group's rules and guidelines
- **`data/welcome_messages.json`** - Seasonal and themed welcome messages
- **`config/settings.py`** - Advanced bot settings and feature toggles

---

## 📝 Commands

### 👥 Public Commands
| Command | Description | Usage |
|---------|-------------|-------|
| `/start` | Initialize bot interaction | `/start` |
| `/help` | Show comprehensive help menu | `/help` |
| `/rules` | Display group guidelines | `/rules` |
| `/commands` | List all available commands | `/commands` |
| `/about` | Learn about the group/community | `/about` |
| `/contact` | Contact group administrators | `/contact` |
| `/stats` | Show group statistics | `/stats` |

### 👑 Admin Commands
| Command | Description | Usage |
|---------|-------------|-------|
| `/admin` | Open admin control panel | `/admin` |
| `/setwelcome` | Customize welcome message | `/setwelcome <message>` |
| `/togglewelcome` | Enable/disable welcome messages | `/togglewelcome` |
| `/addadmin` | Add new administrator | `/addadmin <user_id>` |
| `/removeadmin` | Remove administrator | `/removeadmin <user_id>` |
| `/broadcast` | Send message to all users | `/broadcast <message>` |
| `/backup` | Create data backup | `/backup` |

---

## 📁 Project Structure

```
TrueSyncAI-Telegram-Support-Bot/
├── 📄 main.py                    # Entry point
├── 📄 requirements.txt           # Dependencies
├── 📄 .env.example              # Environment template
├── 📄 README.md                 # This file
├── 📁 config/                   # Configuration files
│   ├── 📄 __init__.py
│   ├── 📄 settings.py           # Bot settings
│   └── 📄 messages.py           # Message templates
├── 📁 bot/                      # Core bot logic
│   ├── 📄 __init__.py
│   ├── 📁 handlers/             # Message handlers
│   │   ├── 📄 __init__.py
│   │   ├── 📄 welcome.py        # Welcome message logic
│   │   ├── 📄 commands.py       # Command handlers
│   │   └── 📄 admin.py          # Admin functionality
│   ├── 📁 utils/                # Utility functions
│   │   ├── 📄 __init__.py
│   │   ├── 📄 decorators.py     # Custom decorators
│   │   ├── 📄 helpers.py        # Helper functions
│   │   ├── 📄 logger.py         # Logging configuration
│   │   └── 📄 database.py       # Database operations
│   └── 📁 keyboards/            # Inline keyboards
│       ├── 📄 __init__.py
│       └── 📄 inline.py         # Keyboard layouts
├── 📁 data/                     # Data files
│   ├── 📄 guidelines.txt        # Group rules
│   ├── 📄 welcome_messages.json # Welcome message templates
│   └── 📄 bot_data.db          # SQLite database
└── 📁 logs/                     # Log files
    └── 📄 bot_YYYYMMDD.log     # Daily log files
```

---

## 🔧 Advanced Configuration

### Custom Welcome Messages
Edit `data/welcome_messages.json` to add seasonal or themed messages:

```json
{
  "default": "Welcome to our amazing community, {name}! 🎉",
  "seasonal": {
    "winter": "❄️ Winter greetings, {name}! Welcome to our cozy community!",
    "spring": "🌸 Spring has brought us {name}! Welcome!",
    "summer": "☀️ Summer vibes with {name}! Welcome aboard!",
    "autumn": "🍂 Autumn welcomes {name} to our community!"
  },
  "special": {
    "weekend": "🎊 Weekend warrior {name} has joined! Welcome!",
    "holiday": "🎈 Holiday spirit brings us {name}! Welcome!"
  }
}
```

### Database Schema
The bot uses SQLite with these main tables:
- `users` - User information and preferences
- `groups` - Group settings and configurations
- `welcome_stats` - Welcome message statistics
- `admin_actions` - Administrative action logs

---

## 🎨 Customization Examples

### Custom Welcome Handler
```python
# In bot/handlers/welcome.py
async def handle_new_member(self, update, context):
    # Your custom logic here
    member = update.message.new_chat_members[0]
    custom_message = f"🌟 {member.first_name}, you've joined something special!"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=custom_message,
        reply_markup=get_welcome_keyboard()
    )
```

### Custom Admin Commands
```python
# Add to bot/handlers/admin.py
@admin_required
async def custom_admin_command(self, update, context):
    # Your admin functionality here
    pass
```

---

## 🐛 Troubleshooting

### Common Issues

**Bot not responding to commands:**
- Ensure the bot has proper permissions in your group
- Check that the bot token is correct in your `.env` file
- Verify the bot is added as an administrator

**Welcome messages not working:**
- Confirm the bot has "Delete messages" and "Restrict members" permissions
- Check the `GROUP_ID` in your configuration
- Review the logs for any error messages

**Database errors:**
- Ensure the `data/` directory exists and is writable
- Check SQLite installation: `python -c "import sqlite3; print('SQLite OK')"`
- Verify database file permissions

### Debug Mode
Enable debug logging:
```bash
export LOG_LEVEL=DEBUG
python main.py
```

### Log Analysis
Check recent logs:
```bash
tail -f logs/bot_$(date +%Y%m%d).log
```

---

## 🧪 Testing

Run the test suite:
```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-telegram-bot

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=bot --cov-report=html
```

---

## 🚀 Deployment

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

```bash
docker build -t telegram-support-bot .
docker run -d --env-file .env telegram-support-bot
```

### Heroku Deployment
```bash
# Create Procfile
echo "worker: python main.py" > Procfile

# Deploy to Heroku
heroku create your-bot-name
heroku config:set BOT_TOKEN=your_token_here
git push heroku main
```

### VPS Deployment with systemd
Create `/etc/systemd/system/telegram-bot.service`:
```ini
[Unit]
Description=TrueSyncAI Telegram Bot
After=network.target

[Service]
Type=simple
User=botuser
WorkingDirectory=/opt/telegram-bot
Environment=PATH=/opt/telegram-bot/venv/bin
ExecStart=/opt/telegram-bot/venv/bin/python main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup
```bash
# Fork and clone the repo
git clone https://github.com/sujalrajpoot/TrueSyncAI-Telegram-Support-Bot.git
cd TrueSyncAI-Telegram-Support-Bot

# Create development environment
python -m venv dev-env
source dev-env/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run pre-commit hooks
pre-commit install
```

### Contribution Guidelines
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Code Standards
- Follow PEP 8 style guidelines
- Add type hints where appropriate
- Write comprehensive docstrings
- Include unit tests for new features
- Update documentation as needed

---

## 📊 Roadmap

### Version 2.0 (Coming Soon)
- [ ] Web dashboard for bot management
- [ ] Advanced analytics and reporting
- [ ] Multi-language support
- [ ] Plugin system for custom features
- [ ] Integration with popular services (GitHub, Jira, etc.)

### Version 2.1 (Future)
- [ ] AI-powered auto-moderation
- [ ] Voice message support
- [ ] Advanced user verification
- [ ] Custom bot themes
- [ ] Mobile app companion

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 TrueSyncAI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🆘 Support & Community

### Get Help
- 📚 **Documentation**: [Wiki](TrueSyncAI-Telegram-Support-Bot/wiki)
- 🐛 **Bug Reports**: [Issues](TrueSyncAI-Telegram-Support-Bot/issues)
- 💡 **Feature Requests**: [Discussions](TrueSyncAI-Telegram-Support-Bot/discussions)

### Professional Support
Need custom development or priority support? Contact us:
- 📧 Email: support@truesyncai.com
- 🌐 Website: [truesyncai.com](https://truesyncai.com)

---

## 🏆 Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Excellent Telegram Bot API wrapper
- [Telegram Bot API](https://core.telegram.org/bots/api) - Official Telegram Bot API
- Contributors and community members who make this project better

---

## 📈 Statistics

![GitHub stars](https://img.shields.io/github/stars/sujalrajpoot/TrueSyncAI-Telegram-Support-Bot?style=social)
![GitHub forks](https://img.shields.io/github/forks/sujalrajpoot/TrueSyncAI-Telegram-Support-Bot?style=social)
![GitHub issues](https://img.shields.io/github/issues/sujalrajpoot/TrueSyncAI-Telegram-Support-Bot)
![GitHub last commit](https://img.shields.io/github/last-commit/sujalrajpoot/TrueSyncAI-Telegram-Support-Bot)

**⭐ If you find this project helpful, please give it a star! ⭐**

Made with ❤️ by [Sujal Rajpoot](https://github.com/sujalrajpoot)
