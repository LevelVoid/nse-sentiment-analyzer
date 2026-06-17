<div align="center">

# 📊 NSE Stock Sentiment Analyzer

**AI Tool #1 of 52** — Enter any NSE ticker & get live price + news sentiment analysis in one dashboard.

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/AshayK003/nse-sentiment-analyzer?style=flat&logo=github)](https://github.com/AshayK003/nse-sentiment-analyzer)
[![Open Source](https://img.shields.io/badge/Open%20Source-❤️-red)](https://github.com/AshayK003/nse-sentiment-analyzer)

<p align="center">
  <b>🇮🇳 India-focused</b> &nbsp;·&nbsp; <b>🆓 Zero API costs</b> &nbsp;·&nbsp; <b>🔌 No API keys needed</b> &nbsp;·&nbsp; <b>📡 Live data</b>
</p>

</div>

---

## ✨ Features

- **Live price data** — Current price, day change %, day range, volume for any NSE stock or ETF
- **News sentiment analysis** — Scrapes latest news via DuckDuckGo, scores every headline
- **VADER + Financial Lexicon** — Tuned for Indian market terms (bullish, circuit, demerger, FII, etc.)
- **BUY / HOLD / CAUTION signal** — Aggregated from headline sentiment distribution
- **Headline breakdown** — See exactly which news is driving sentiment positive or negative
- **~3 second scan** — Enter a ticker, get results instantly
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
 yfinance → Live price, PE, volume, 52W range
        ↓
 DuckDuckGo → Last 7 days of news articles
        ↓
 VADER + Financial Lexicon → Per-headline sentiment scores
        ↓
 Dashboard → Overall signal + sentiment distribution
```

Each headline is scored using VADER (Valence Aware Dictionary and sEntiment Reasoner), augmented with a custom financial lexicon tuned for Indian equity markets. The individual scores are aggregated into a single **BUY / HOLD / CAUTION** signal.

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
| **UI** | [Streamlit](https://streamlit.io) | Fastest way to build data dashboards in Python |
| **Market Data** | [yfinance](https://github.com/ranaroussi/yfinance) | Free Yahoo Finance API (`.NS` suffix for NSE) |
| **News** | [DuckDuckGo Search](https://github.com/deedy5/duckduckgo_search) | Free, no API key, privacy-respecting |
| **Sentiment** | [VADER](https://github.com/cjhutto/vaderSentiment) + custom financial lexicon | ~3ms per headline, no GPU, no API calls |
| **Hosting** | [Streamlit Community Cloud](https://streamlit.io/cloud) | Free deploy from GitHub |

**Zero external API costs.** Everything runs on free tiers or local.

---

## 📋 Supported Tickers

All NSE-listed equities and ETFs. Common ones built into the selector:

**Nifty 50:** RELIANCE, HDFCBANK, TCS, INFY, ICICIBANK, SBIN, BHARTIARTL, ITC, LT, AXISBANK, BAJFINANCE, WIPRO, TITAN, MARUTI, HINDUNILIVER, TATAMOTORS, TATASTEEL, ADANIENT, and more.

**ETFs:** NIFTYBEES, GOLDBEES, NEXT50IETF, MIDCAPETF, MODEFENCE, MAKEINDIA, ENERGY, METALETF

**Custom:** Type any NSE ticker (e.g., NYKAA, ZOMATO, PWL, GROWW)

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
