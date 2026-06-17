<div align="center">

# 📊 NSE Stock Sentiment Analyzer

**AI Tool #1 of 52** — Enter any NSE ticker & get live price + news sentiment + technical indicators in one dashboard.

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/AshayK003/nse-sentiment-analyzer?style=flat&logo=github)](https://github.com/AshayK003/nse-sentiment-analyzer)
[![Open Source](https://img.shields.io/badge/Open%20Source-❤️-red)](https://github.com/AshayK003/nse-sentiment-analyzer)

<p align="center">
  <b>🇮🇳 India-focused</b> &nbsp;·&nbsp; <b>🆓 No API costs</b> &nbsp;·&nbsp; <b>🔌 No API keys</b> &nbsp;·&nbsp; <b>📡 Live data</b>
</p>

</div>

---

## ✨ Features

- **Live price data** — Current price, day change %, day range, volume, PE ratio for any NSE stock or ETF
- **News via RSS** — Fetches from Yahoo Finance RSS + Google News RSS (works reliably from cloud IPs)
- **FinBERT sentiment** — Domain-adapted transformer (87% accuracy on financial text) with VADER fallback
- **BUY / HOLD / CAUTION signal** — Aggregated from headline sentiment distribution
- **Technical indicators** — RSI(14), SMA 50/200 trend, MACD histogram
- **Headline breakdown** — See exactly which news is driving sentiment positive or negative
- **Portfolio mode** — Add stocks to a watchlist and scan all at once
- **Track record** — Rate signals as accurate/wrong and track your accuracy over time
- **No API keys** — Works out of the box, zero configuration
- **Free & open-source** — MIT license, self-host or use the hosted version

---

## 🚀 Hosted Version

**Want to use it without touching a terminal?**

👉 **[Launch NSE Sentiment Analyzer](https://nse-sentiment-analyzer.streamlit.app)**

One click, zero setup. ₹199 one-time on [Gumroad](https://gumroad.com). No subscription, no API keys, no terminal.

---

## 🛠️ How It Works

```
You type "RELIANCE"
        ↓
 yfinance → Live price, PE, volume, 52W range, 1yr history
        ↓
 RSS Feeds → Yahoo Finance + Google News (DuckDuckGo fallback)
        ↓
 FinBERT (primary) / VADER (fallback) → Per-headline sentiment scores
        ↓
 yfinance 1yr history → RSI, SMA 50/200, MACD
        ↓
 Dashboard → Overall signal + sentiment distribution + technicals
```

Sentiment is scored using **FinBERT** (`ProsusAI/finbert`), a BERT model fine-tuned on financial text, achieving ~87% accuracy. Falls back to VADER with a custom financial lexicon when the model isn't available. RSI, SMA trends, and MACD are computed from 1 year of daily price data.

---

## 📦 Local Quick Start

```bash
# Clone the repo
git clone https://github.com/AshayK003/nse-sentiment-analyzer.git
cd nse-sentiment-analyzer

# Install dependencies (Python 3.11+)
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Open **http://localhost:8501** in your browser and start analyzing.

> **Note:** Streamlit Cloud apps sleep after inactivity. First load after sleep takes ~30–60 seconds.

---

## 🧰 Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| **UI** | [Streamlit](https://streamlit.io) | Fastest data dashboards in Python |
| **Market Data** | [yfinance](https://github.com/ranaroussi/yfinance) | Free Yahoo Finance API (`.NS` suffix for NSE) |
| **News (RSS)** | [feedparser](https://github.com/kurtmckee/feedparser) | Yahoo Finance + Google News RSS, works from any IP |
| **News (fallback)** | [duckduckgo_search](https://github.com/deedy5/duckduckgo_search) | Used when RSS returns < 3 articles |
| **Sentiment** | [FinBERT](https://huggingface.co/ProsusAI/finbert) (primary) + [VADER](https://github.com/cjhutto/vaderSentiment) (fallback) | 87% accuracy on financial text via domain-adapted transformer |
| **Indicators** | [pandas](https://pandas.pydata.org) rolling/EWM | RSI(14), SMA 50/200, MACD(12,26,9) computed from 1yr history |
| **Hosting** | [Streamlit Community Cloud](https://streamlit.io/cloud) | Free deploy from GitHub |

**Zero API key costs.** Everything uses free/public data sources.

---

## 📋 Supported Tickers

100+ NSE-listed equities and ETFs built into the selector. Any other NSE ticker can be typed in the custom input.

**Nifty 50:** RELIANCE, HDFCBANK, TCS, INFY, ICICIBANK, SBIN, BHARTIARTL, ITC, LT, AXISBANK, BAJFINANCE, WIPRO, TITAN, MARUTI, HINDUNILVR, TATAMOTORS, TATASTEEL, ADANIENT, M&M, TATAPOWER, HINDALCO, BEL, and more.

**Banks & Finance:** KOTAKBANK, INDUSINDBK, BANKBARODA, PNB, YESBANK, IDFCFIRSTB, PFC, RECLTD, BAJAJFINSV, SBILIFE, HDFCLIFE

**Pharma:** SUNPHARMA, DIVISLAB, CIPLA, DRREDDY, TORNTPHARM, APOLLOHOSP, LUPIN, BIOCON

**Tech:** INFY, WIPRO, HCLTECH, TECHM, LTIM, DIXON

**Consumption:** ITC, NESTLEIND, DMART, BRITANNIA, DABUR, MARICO, GODREJCP, VBL, JUBLFOOD, TATACONSUM

**Auto:** MARUTI, TATAMOTORS, BAJAJ-AUTO, EICHERMOT, HEROMOTOCO, TVSMOTOR

**Infra & Industrials:** LT, ULTRACEMCO, GRASIM, ABB, SIEMENS, POLYCAB, PIDILITIND, HAVELLS, ASTRAL

**Energy:** ONGC, COALINDIA, IOC, BPCL, ADANIPOWER, ADANIGREEN, ADANITRANS, NHPC

**Special Situations:** IRFC, RVNL, IRCTC, IEX, DLF, INDIGO, HAL

**ETFs:** NIFTYBEES, GOLDBEES, NEXT50IETF, MIDCAPETF, MODEFENCE, MAKEINDIA, ENERGY, METALETF

**Custom:** Type any NSE ticker not in the list (e.g., NYKAA, ZOMATO, PWL, GROWW)

---

## 📸 Screenshots

<!-- Add screenshots here once deployed -->
*Coming soon — screenshot of live dashboard with RELIANCE output.*

---

## ❤️ Support the Project

Building 52 AI tools in 52 weeks takes time and coffee. If you find this useful:

<div align="center">
  <a href="https://chai4.me/darkcharon3301">
    <img src="https://chai4.me/icons/wordmark.png" alt="Support on Chai4Me" height="36"/>
  </a>
  <br/>
  <a href="https://gumroad.com">Buy the hosted version →</a>
</div>

---

## 🤝 Contributing

This is Tool #1 of the **52 AI Tools in 52 Weeks** challenge. The goal is to ship fast and iterate.

- **Issues:** Found a bug? Open an issue.
- **PRs:** Feature ideas, better lexicon, UI improvements — all welcome.
- **Tickers:** Know a missing NSE stock? Send a PR to update `NSE_TICKERS` in `app.py`.

---

## 📜 License

MIT © [Ashay Kushwaha](https://github.com/AshayK003)

---

<div align="center">
  <sub>Built by <a href="https://x.com/sentinelcipher">@sentinelcipher</a> · Part of the 52 AI Tools in 52 Weeks challenge</sub>
  <br/>
  <sub>⚠️ Not financial advice. Always do your own research.</sub>
</div>
