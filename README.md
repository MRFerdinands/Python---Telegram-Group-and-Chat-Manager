# Telegram Group and Chat Manager

A Python script to bulk manage Telegram groups and private chats.

## Features

- Leave multiple groups/channels
- Delete private chats in bulk
- Interactive color-coded menu
- Confirmation before each action
- Works on Windows, macOS, Linux

## Requirements

- Python 3.7+
- Telegram API credentials
- Telethon library

## Setup

1. Clone repo:
```bash
git clone https://github.com/yourusername/telegram-group-manager.git
cd telegram-group-manager
```

2. Install dependencies:
```bash
pip install telethon
```

3. Get API credentials from [my.telegram.org](https://my.telegram.org):
   - Create app in "API development tools"
   - Note your `api_id` and `api_hash`

## How to Use

1. Run script:
```bash
python telegram_manager.py
```

2. Enter when prompted:
   - API ID
   - API Hash
   - Phone number (with country code)

3. Menu options:
   - 1: Manage groups/channels
   - 2: Manage private chats
   - 3: Exit

4. Confirm each action before executing.

## FAQ

**Q: Is this safe?**
A: Yes, uses official Telegram API via Telethon.

**Q: Can I recover deleted chats?**
A: Private chats can be restarted. Groups need re-invite.

**Q: Why API credentials?**
A: Required for Telegram API authentication.

## Contributing

Open issues or PRs for improvements.

## License

MIT
