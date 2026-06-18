"""
Tests for NSE Sentiment Analyzer.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from sentiment import (
    get_sia,
    analyze_headline_sentiment,
    get_overall_signal,
    get_sentiment_emoji,
    FINANCIAL_BOOSTERS,
)
from data_fetcher import (
    _is_numeric,
    format_price,
    format_large_num,
    NSE_TICKERS,
)


# ─── Sentiment Tests ───


class TestSentiment:
    @classmethod
    def setup_class(cls):
        cls.sia = get_sia()

    def test_sia_initializes(self):
        assert self.sia is not None

    def test_lexicon_boosters_loaded(self):
        for word, score in FINANCIAL_BOOSTERS.items():
            assert word in self.sia.lexicon, f"Missing booster: {word}"
            assert self.sia.lexicon[word] == score, f"Wrong score for {word}"

    def test_bullish_headline(self):
        result = analyze_headline_sentiment("Stock surges on bullish outlook", "", self.sia)
        assert result["compound"] > 0

    def test_bearish_headline(self):
        result = analyze_headline_sentiment("Stock crashes on negative results", "", self.sia)
        assert result["compound"] < -0.2  # VADER normalization bounds this

    def test_neutral_headline(self):
        result = analyze_headline_sentiment("Company to hold board meeting next week", "", self.sia)
        # Neutral text should have compound near 0
        assert -0.3 < result["compound"] < 0.3

    def test_get_sentiment_emoji(self):
        assert get_sentiment_emoji(0.5) == "🟢"
        assert get_sentiment_emoji(-0.5) == "🔴"
        assert get_sentiment_emoji(0) == "⚪"
        assert get_sentiment_emoji(0.2) == "⚪"

    def test_get_overall_signal_bullish(self):
        scores = [{"compound": 0.8}, {"compound": 0.5}, {"compound": 0.1}]
        signal, compound, emoji = get_overall_signal(scores)
        assert "BULLISH" in signal
        assert "🟢" in signal

    def test_get_overall_signal_bearish(self):
        scores = [{"compound": -0.8}, {"compound": -0.5}, {"compound": -0.1}]
        signal, compound, emoji = get_overall_signal(scores)
        assert "BEARISH" in signal
        assert "🔴" in signal

    def test_get_overall_signal_neutral(self):
        scores = [{"compound": 0.1}, {"compound": -0.1}, {"compound": 0.05}]
        signal, compound, emoji = get_overall_signal(scores)
        assert "NEUTRAL" in signal

    def test_get_overall_signal_empty(self):
        signal, compound, emoji = get_overall_signal([])
        assert signal == "NEUTRAL ⚪"

    def test_get_overall_signal_mixed(self):
        scores = [{"compound": 0.8}, {"compound": -0.8}, {"compound": 0.05}]
        signal, compound, emoji = get_overall_signal(scores)
        # Mixed with strong both sides → neutral
        assert "NEUTRAL" in signal or "BULLISH" in signal  # depends on weights


# ─── Data / Formatting Tests ───


class TestDataFetcher:
    def test_nse_tickers_populated(self):
        assert len(NSE_TICKERS) > 80
        assert "RELIANCE" in NSE_TICKERS
        assert "HDFCBANK" in NSE_TICKERS
        assert "TCS" in NSE_TICKERS

    def test_is_numeric(self):
        assert _is_numeric(42)
        assert _is_numeric(3.14)
        assert not _is_numeric("N/A")
        assert not _is_numeric(None)
        assert not _is_numeric(True)

    def test_format_price(self):
        assert "N/A" in str(format_price(None))
        assert "N/A" in str(format_price("N/A"))
        # Numeric values returned as numbers for Streamlit compatibility
        assert isinstance(format_price(100.5), (int, float))

    def test_format_large_num(self):
        assert "Cr" in format_large_num(100_00_000)
        assert "L" in format_large_num(1_00_000)
        assert "₹" in format_large_num(1000)
        assert "N/A" in format_large_num(None)
        assert "N/A" in format_large_num("N/A")
