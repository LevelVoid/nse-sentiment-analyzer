"""Market-wide data for NSE Sentiment Analyzer.
FII/DII institutional flow fetched via nsepython.
"""

import logging
import streamlit as st

logger = logging.getLogger(__name__)


def _fii_dii_action(net):
    """Classify FII/DII net flow as Buying/Selling/Flat (threshold ±200 Cr)."""
    if net > 200:
        return "Buying"
    elif net < -200:
        return "Selling"
    return "Flat"


@st.cache_data(ttl=3600)
def get_fii_dii_flow():
    """Fetch latest FII/DII net flow from NSE India.

    Returns a dict:
        {
            "fii_net": float (Cr),
            "dii_net": float (Cr),
            "date": str,
            "combined_net": float (Cr),
            "fii_action": "Buying"|"Selling"|"Flat",
            "dii_action": "Buying"|"Selling"|"Flat",
        }
    Returns None on failure.
    """
    try:
        from nsepython import nse_fiidii
        df = nse_fiidii()
        if df is None or df.empty:
            return None

        fii_row = df[df["category"].str.contains("FII|FPI", case=False, na=False)]
        dii_row = df[df["category"].str.contains("DII", case=False, na=False)]

        fii_net = float(fii_row["netValue"].iloc[0]) if not fii_row.empty else 0.0
        dii_net = float(dii_row["netValue"].iloc[0]) if not dii_row.empty else 0.0
        date = str(fii_row["date"].iloc[0]) if not fii_row.empty else str(dii_row["date"].iloc[0]) if not dii_row.empty else ""

        return {
            "fii_net": fii_net,
            "dii_net": dii_net,
            "date": date,
            "combined_net": fii_net + dii_net,
            "fii_action": _fii_dii_action(fii_net),
            "dii_action": _fii_dii_action(dii_net),
        }
    except Exception as e:
        logger.debug("get_fii_dii_flow() failed: %s", e)
        return None


def get_market_pulse():
    """Fetch Nifty 50 index and return market-level pulse + actionable verdict.

    Uses the same yfinance pattern as get_vix() for index tickers.
    Returns a verdict based on Nifty change % + VIX level (caller passes
    the already-fetched VIX since it's cached in session_state).

    Returns:
        dict with keys:
            nifty_price (float|None), nifty_change_pct (float|None),
            verdict (str), verdict_icon (str), verdict_detail (str)
    """
    try:
        import yfinance as yf
        t = yf.Ticker("^NSEI")
        data = t.history(period="5d")
    except Exception:
        return {
            "nifty_price": None, "nifty_change_pct": None,
        }

    if data is None or data.empty or len(data) < 2:
        return {
            "nifty_price": None, "nifty_change_pct": None,
        }

    try:
        closes = data["Close"].dropna()
        if len(closes) < 2:
            return {
                "nifty_price": None, "nifty_change_pct": None,
            }
        nifty_price = float(closes.iloc[-1])
        prev_close = float(closes.iloc[-2])
        nifty_change_pct = round((nifty_price - prev_close) / prev_close * 100, 2)
    except (KeyError, IndexError, TypeError, ValueError, AttributeError):
        return {
            "nifty_price": None, "nifty_change_pct": None,
        }

    return {
        "nifty_price": nifty_price,
        "nifty_change_pct": nifty_change_pct,
    }


def get_market_verdict(nifty_change_pct, vix_level):
    """Determine market climate verdict from Nifty change and VIX level.

    Args:
        nifty_change_pct: float or None — Nifty 50 daily % change
        vix_level: str — 'Low', 'Medium', 'High', or 'N/A'

    Returns:
        tuple of (verdict, icon, detail)
    """
    if vix_level is None or vix_level == "N/A":
        return "Neutral", "\u26aa", "VIX data unavailable"

    # Determine direction from Nifty change
    is_up = nifty_change_pct is not None and nifty_change_pct >= 0.3
    is_down = nifty_change_pct is not None and nifty_change_pct <= -0.3

    if vix_level == "High":
        if is_down:
            return "Risky", "\U0001f534", "High VIX + market dropping — avoid new positions"
        return "Cautious", "\U0001f7e0", "Elevated volatility — use stop-losses, size down"
    elif vix_level == "Medium":
        if is_up:
            return "Bullish", "\U0001f7e2", "Positive momentum, normal volatility"
        return "Neutral", "\u26aa", "Mixed conditions — stock-specific action"
    else:  # Low VIX
        if is_down:
            return "Cautious", "\U0001f7e0", "Low VIX but weakness detected — wait for confirmation"
        return "Bullish", "\U0001f7e2", "Low VIX — trending markets favor swing trades"
