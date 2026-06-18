"""
Sentiment analysis for NSE Stock Sentiment Analyzer.
VADER + custom financial lexicon tuned for Indian markets.
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st


# ─── Financial sentiment augmentations ───
# Words VADER doesn't score well for finance
FINANCIAL_BOOSTERS = {
    "bullish": 2.5,
    "bearish": -2.5,
    "outperform": 2.0,
    "underperform": -2.0,
    "overweight": 1.5,
    "underweight": -1.5,
    "upside": 1.8,
    "downside": -1.8,
    "buy": 1.5,
    "accumulate": 1.2,
    "reduce": -1.2,
    "sell": -2.0,
    "downgrade": -2.0,
    "upgrade": 2.0,
    "positive": 1.0,
    "negative": -1.0,
    "surge": 1.5,
    "plunge": -2.0,
    "rally": 1.5,
    "crash": -2.5,
    "record": 1.0,
    "decline": -1.0,
    "profit": 1.0,
    "loss": -1.0,
    "dividend": 1.0,
    "expansion": 1.0,
    "growth": 1.0,
    "slowdown": -1.5,
    "momentum": 1.0,
    "volatility": -0.5,
    "correction": -1.0,
    "breakout": 1.5,
    "breakdown": -1.5,
    "resistance": -0.3,
    "support": 0.3,
    "all-time high": 2.0,
    "52-week high": 1.5,
    "52-week low": -1.5,
}


@st.cache_resource
def get_sia():
    """Initialize VADER with custom financial lexicon."""
    sia = SentimentIntensityAnalyzer()
    sia.lexicon.update(FINANCIAL_BOOSTERS)
    return sia


def analyze_headline_sentiment(headline, body, sia):
    """Score a headline using VADER + financial lexicon."""
    text = f"{headline}. {body}" if body else headline
    vader = sia.polarity_scores(text)
    return {"compound": vader["compound"], "vader": vader}


def get_overall_signal(headline_scores):
    """Determine overall signal from headline scores."""
    if not headline_scores:
        return "NEUTRAL ⚪", 0.0, "⚪"

    avg_compound = sum(s["compound"] for s in headline_scores) / len(headline_scores)
    pos_count = sum(1 for s in headline_scores if s["compound"] >= 0.3)
    neg_count = sum(1 for s in headline_scores if s["compound"] <= -0.3)

    if avg_compound >= 0.2 and pos_count > neg_count:
        return "BULLISH 🟢", avg_compound, "🟢"
    elif avg_compound <= -0.2 and neg_count > pos_count:
        return "BEARISH 🔴", avg_compound, "🔴"
    else:
        return "NEUTRAL ⚪", avg_compound, "⚪"


def get_sentiment_emoji(compound):
    if compound >= 0.3:
        return "🟢"
    elif compound <= -0.3:
        return "🔴"
    return "⚪"
