::: {align="center"}
# 🎵 AXIZTEAMM MUSIC

### ⚡ Telegram Music Bot • Powered by AXIZTEAMM

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Platform-Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://telegram.org/)
[![Status](https://img.shields.io/badge/Status-Live-16A34A?style=for-the-badge)]()
[![API](https://img.shields.io/badge/API-Shruti-7C3AED?style=for-the-badge)]()

**A clean Telegram voice-chat music bot built for fast and reliable
streaming**

[Support](https://t.me/Axizsupport) •
[Updates](https://t.me/AxizUpdates) • [Team](https://t.me/Axizteamm)
:::

------------------------------------------------------------------------

## ✦ AXIZTEAMM

AXIZTEAMM MUSIC is a Telegram voice-chat music bot with fast song
search, voice-chat playback, queue management and interactive player
controls.

## 🎧 Features

-   🎵 Music search and playback
-   🔎 Fast song search
-   ▶️ Play, pause and resume
-   ↻ Replay current track
-   ⏭️ Skip and stop controls
-   📋 Queue management
-   🎛️ Interactive player buttons
-   🔄 Rotating start stickers
-   ⚡ Shruti API powered downloads
-   🍪 Cookie-free architecture
-   💾 MongoDB storage
-   🛡️ Permanent systemd deployment

## 🎶 Player

``` text
┌──────────────────────────────────────────┐
│              🎵 NOW PLAYING              │
│                                          │
│              Song Title                  │
│              Duration                    │
│              By AXIZTEAMM                │
│                                          │
│          II    ▷    ↻                    │
│          ‣‣I         ▢                   │
└──────────────────────────────────────────┘
```

## 📋 Queue

``` text
❖ QUEUE

◯ NOW PLAYING : Song
◯ DURATION : 5:17
◯ BY : AXIZTEAMM

◯ #2 — Next Song
◯ #3 — Next Song
```

## ⚡ Architecture

``` text
Telegram
   │
   ▼
AXIZTEAMM MUSIC
   │
   ├── Search
   ├── Player
   ├── Queue
   └── Voice Chat
          │
          ▼
      Shruti API
```

## 🔐 Configuration

Create a `.env` file:

``` env
API_ID=
API_HASH=
BOT_TOKEN=
MONGO_DB_URI=
SHRUTI_API_URL=https://shrutibots.site
SHRUTI_API_KEY=
```

**Never publish real tokens, API keys or database credentials.**

## 🚀 Deployment

The bot can run as a permanent Linux `systemd` service.

``` bash
sudo systemctl restart xhamsterbeats
sudo systemctl status xhamsterbeats --no-pager
```

Live logs:

``` bash
sudo journalctl -u xhamsterbeats -f -o cat
```

## 🧪 Testing

``` bash
python3 -m pytest -q
python3 -m compileall -q .
```

## 📁 Project Structure

``` text
XhamsterBeats/
├── AnonXMusic/
│   ├── plugins/
│   ├── core/
│   ├── utils/
│   └── __main__.py
├── tests/
├── strings/
├── .env
├── pyproject.toml
└── README.md
```

## 🌐 AXIZTEAMM

  ------------ ----------------------------------------------------
  🤖 Bot       [@XhamsterBeatsbot](https://t.me/XhamsterBeatsbot)
  🛠 Support    [@Axizsupport](https://t.me/Axizsupport)
  📢 Updates   [@AxizUpdates](https://t.me/AxizUpdates)
  👥 Team      [@Axizteamm](https://t.me/Axizteamm)
  ------------ ----------------------------------------------------

## 👑 Credits

**Owner:** [@Sexybeginner](https://t.me/SexybeginnER)

**Developer:** [@Civilianssz](https://t.me/Civilianssz)

------------------------------------------------------------------------

::: {align="center"}
### 🎵 AXIZTEAMM MUSIC

**Built for Telegram • Built for Music • Built by AXIZTEAMM**
:::
