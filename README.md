<div align="center">

# ✦ AXIZTEAMM MUSIC

### A Premium Telegram Music Bot

**Search • Stream • Queue • Control**

[![Python](https://img.shields.io/badge/Python-3.10%2B-7c3aed?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-7c3aed?style=for-the-badge&logo=telegram&logoColor=white)](https://telegram.org/)
[![API](https://img.shields.io/badge/API-Shruti-7c3aed?style=for-the-badge)](https://shrutibots.site/)
[![Status](https://img.shields.io/badge/Status-Online-22c55e?style=for-the-badge)](https://t.me/XhamsterBeatsbot)

</div>

---

## ◈ Overview

**AXIZTEAMM MUSIC** is a Telegram voice-chat music bot built for fast searching, smooth streaming and simple controls.

It uses the **Shruti API** for media resolution and keeps the playback experience focused on Telegram.

> **AXIZTEAMM**
>
> Music without the unnecessary complexity.

---

## ✦ Features

| Feature | Description |
|---|---|
| 🎵 Music Search | Search and play tracks directly from Telegram |
| ⚡ Fast Resolution | Uses Shruti API for media resolution |
| 🎧 Voice Chat | Stream audio directly into Telegram voice chats |
| 📋 Queue | Add, view and manage multiple tracks |
| ⏯ Playback Controls | Pause, resume, replay, skip and stop |
| 🔁 Queue Management | Keep playback organized across tracks |
| 🖼 Rich Now Playing | Clean streaming card with track information |
| 🧩 Inline Controls | Simple callback buttons for playback |
| 🔐 Environment Config | Secrets stay outside the source code |
| 🖥 VPS Ready | Designed for permanent systemd deployment |

---

## ◈ Player Experience

```text
╭──────────────────────────────────────╮
│          🎵 NOW PLAYING              │
│                                      │
│  Track       Your Requested Song     │
│  Duration    04:32                   │
│  By          AXIZTEAMM               │
│                                      │
│        II   ▷   ↻                    │
│        ‣‣I  ▢                        │
╰──────────────────────────────────────╯
```

### Controls

**II** Pause  
**▷** Resume  
**↻** Replay  
**‣‣I** Skip  
**▢** Stop

---

## 📋 Queue System

The queue keeps every requested track organized.

```text
❖ QUEUE

◯ NOW PLAYING : Current Song
◯ DURATION : 04:32
◯ BY : AXIZTEAMM

◯ #2 — Next Song
◯ #3 — Another Song
◯ #4 — Another Track
```

Queue controls allow users to move through tracks without interrupting the overall playback flow.

---

## ⚙ Architecture

```text
                 ┌──────────────────┐
                 │     TELEGRAM     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  AXIZTEAMM BOT   │
                 └────────┬─────────┘
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
      ┌──────────────┐         ┌──────────────┐
      │    Shruti    │         │   MongoDB    │
      │     API      │         │   Database   │
      └──────┬───────┘         └──────────────┘
             │
             ▼
      ┌──────────────┐
      │ Audio Stream │
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐
      │ Telegram VC  │
      └──────────────┘
```

---

# 🚀 Deployment

## 1. Prerequisites

You need:

- Python 3.10+
- Git
- FFmpeg
- Telegram Bot Token
- Telegram API ID
- Telegram API Hash
- MongoDB connection URI
- Shruti API key

Clone the repository:

```bash
git clone https://github.com/tajamullone106-droid/x.git
cd x
```

---

# ☁️ Deploy on Render

### Step 1 — Create a Render service

Create a new **Background Worker** and connect your GitHub repository.

Repository:

```text
https://github.com/tajamullone106-droid/x
```

### Step 2 — Build Command

```bash
pip install -r requirements.txt
```

If the repository uses `uv`, use:

```bash
pip install uv
uv sync
```

### Step 3 — Start Command

```bash
python3 -m AnonXMusic
```

### Step 4 — Environment Variables

Add these variables inside Render:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_DB_URI=your_mongodb_uri
SHRUTI_API_URL=https://shrutibots.site
SHRUTI_API_KEY=your_shruti_api_key
```

Do **not** put real tokens or API keys inside `README.md` or GitHub source files.

### Render Notes

- Use a **Background Worker**, not a static site.
- Make sure FFmpeg is available in the runtime.
- Configure all required environment variables before starting the service.
- Check Render logs if the bot exits during startup.

---

# 🟣 Deploy on Heroku

### Step 1 — Install Heroku CLI

Install the Heroku CLI and log in:

```bash
heroku login
```

### Step 2 — Create the application

```bash
heroku create axizteamm-music
```

### Step 3 — Configure environment variables

```bash
heroku config:set API_ID="your_api_id"
heroku config:set API_HASH="your_api_hash"
heroku config:set BOT_TOKEN="your_bot_token"
heroku config:set MONGO_DB_URI="your_mongodb_uri"
heroku config:set SHRUTI_API_URL="https://shrutibots.site"
heroku config:set SHRUTI_API_KEY="your_shruti_api_key"
```

### Step 4 — Add FFmpeg

The application needs FFmpeg for audio processing.

Use an appropriate Heroku buildpack or container image that provides FFmpeg.

### Step 5 — Deploy

```bash
git add .
git commit -m "Deploy AXIZTEAMM MUSIC"
git push heroku main
```

If your local branch is `master`:

```bash
git push heroku master
```

### Step 6 — Check logs

```bash
heroku logs --tail
```

---

# 🖥 Deploy on VPS

A VPS is recommended when you want a long-running music bot with full control.

### Step 1 — Update server

```bash
sudo apt update && sudo apt upgrade -y
```

Install required packages:

```bash
sudo apt install -y git python3 python3-venv python3-pip ffmpeg
```

### Step 2 — Clone

```bash
cd ~
git clone https://github.com/tajamullone106-droid/x.git XhamsterBeats
cd ~/XhamsterBeats
```

### Step 3 — Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

If the project uses `uv`:

```bash
pip install uv
uv sync
```

### Step 4 — Configure `.env`

Create the environment file:

```bash
nano .env
```

Add:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_DB_URI=your_mongodb_uri
SHRUTI_API_URL=https://shrutibots.site
SHRUTI_API_KEY=your_shruti_api_key
```

Save with:

```text
CTRL + O
ENTER
CTRL + X
```

### Step 5 — Test the bot

```bash
cd ~/XhamsterBeats
source .venv/bin/activate
python3 -m AnonXMusic
```

If the bot starts correctly, stop it with:

```text
CTRL + C
```

---

# 🔧 Permanent VPS Deployment with systemd

Create the service:

```bash
sudo nano /etc/systemd/system/xhamsterbeats.service
```

Use:

```ini
[Unit]
Description=AXIZTEAMM Music Bot
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/XhamsterBeats
Environment=HOME=/home/ubuntu
Environment=PATH=/home/ubuntu/.local/bin:/home/ubuntu/XhamsterBeats/.venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin
ExecStart=/home/ubuntu/.local/bin/uv run --project /home/ubuntu/XhamsterBeats python -m AnonXMusic
Restart=always
RestartSec=5
KillSignal=SIGINT
TimeoutStopSec=30
NoNewPrivileges=true

[Install]
WantedBy=multi-user.target
```

Reload systemd:

```bash
sudo systemctl daemon-reload
```

Enable the service:

```bash
sudo systemctl enable xhamsterbeats
```

Start it:

```bash
sudo systemctl start xhamsterbeats
```

Check status:

```bash
sudo systemctl status xhamsterbeats --no-pager
```

View live logs:

```bash
sudo journalctl -u xhamsterbeats -f -o cat
```

Restart:

```bash
sudo systemctl restart xhamsterbeats
```

Stop:

```bash
sudo systemctl stop xhamsterbeats
```

---

# 🔄 Updating the VPS Bot

```bash
cd ~/XhamsterBeats
git pull
sudo systemctl restart xhamsterbeats
```

Check:

```bash
sudo systemctl status xhamsterbeats --no-pager
```

---

# 🔐 Configuration

Never commit secrets.

Example:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_DB_URI=your_mongodb_uri
SHRUTI_API_URL=https://shrutibots.site
SHRUTI_API_KEY=your_shruti_api_key
```

Recommended `.gitignore` entries:

```gitignore
.env
.venv/
__pycache__/
*.pyc
*.session
```

---

# 🧪 Development & Testing

Install dependencies:

```bash
pip install -r requirements.txt
```

Compile-check Python files:

```bash
python3 -m compileall .
```

Run the test suite:

```bash
pytest -q
```

Run the bot:

```bash
python3 -m AnonXMusic
```

---

# 📁 Project Structure

```text
XhamsterBeats/
├── AnonXMusic/
│   ├── core/
│   ├── plugins/
│   ├── utils/
│   └── __main__.py
├── strings/
├── tests/
├── .env
├── .gitignore
├── LICENSE
├── README.md
└── pyproject.toml
```

---

# ◈ Community

<div align="center">

### AXIZTEAMM

[Bot](https://t.me/XhamsterBeatsbot) •
[Support](https://t.me/Axizsupport) •
[Updates](https://t.me/AxizUpdates) •
[Team](https://t.me/Axizteamm)

</div>

---

# 👑 Credits

**Owner:** [@Sexybeginner](https://t.me/Sexybeginner)

**Developer:** [@Civilianssz](https://t.me/Civilianssz)

**Team:** [@Axizteamm](https://t.me/Axizteamm)

---

## 📜 License

This project is distributed under the license included in the repository.

Please review `LICENSE` before redistributing or modifying the project.

---

<div align="center">

### ✦ AXIZTEAMM

**Built for Telegram • Powered by code • Made for music**

⭐ Star the repository if you find it useful.

</div>
