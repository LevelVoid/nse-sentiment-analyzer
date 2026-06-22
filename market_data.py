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
