"""Tests for volume spike detection (detect_volume_spike)."""

import pytest


class TestDetectVolumeSpike:
    """Tests for detect_volume_spike()."""

    def test_returns_spike_when_above_threshold(self):
        from indicators import detect_volume_spike

        result = detect_volume_spike(2_000_000, 500_000, threshold=2.0)

        assert result["spike"] is True
        assert result["ratio"] == 4.0

    def test_returns_no_spike_when_below_threshold(self):
        from indicators import detect_volume_spike

        result = detect_volume_spike(750_000, 500_000, threshold=2.0)

        assert result["spike"] is False
        assert pytest.approx(result["ratio"], 0.01) == 1.5

    def test_returns_no_spike_on_zero_avg(self):
        from indicators import detect_volume_spike

        result = detect_volume_spike(1_000_000, 0)

        assert result["spike"] is False

    def test_returns_no_spike_on_none_avg(self):
        from indicators import detect_volume_spike

        result = detect_volume_spike(1_000_000, None)

        assert result["spike"] is False

    def test_returns_no_spike_on_none_current(self):
        from indicators import detect_volume_spike

        result = detect_volume_spike(None, 500_000)

        assert result["spike"] is False


class TestMarketVerdict:
    """Tests for get_market_verdict()."""

    def test_bullish_low_vix_market_up(self):
        """Low VIX + Nifty up → Bullish."""
        from market_data import get_market_verdict
        verdict, icon, detail = get_market_verdict(0.8, "Low")
        assert verdict == "Bullish"
        assert "swing trades" in detail.lower()

    def test_bullish_medium_vix_market_up(self):
        """Medium VIX + Nifty up → Bullish."""
        from market_data import get_market_verdict
        verdict, icon, detail = get_market_verdict(0.5, "Medium")
        assert verdict == "Bullish"
        assert "positive momentum" in detail.lower()

    def test_risky_high_vix_market_down(self):
        """High VIX + Nifty down → Risky."""
        from market_data import get_market_verdict
        verdict, icon, detail = get_market_verdict(-1.2, "High")
        assert verdict == "Risky"
        assert "avoid" in detail.lower()

    def test_cautious_high_vix_market_flat(self):
        """High VIX + Nifty flat → Cautious."""
        from market_data import get_market_verdict
        verdict, icon, detail = get_market_verdict(0.0, "High")
        assert verdict == "Cautious"
        assert "stop-loss" in detail.lower()

    def test_cautious_low_vix_market_down(self):
        """Low VIX + Nifty down → Cautious."""
        from market_data import get_market_verdict
        verdict, icon, detail = get_market_verdict(-0.5, "Low")
        assert verdict == "Cautious"
        assert "wait for confirmation" in detail.lower()

    def test_neutral_medium_vix_flat(self):
        """Medium VIX + Nifty flat → Neutral."""
        from market_data import get_market_verdict
        verdict, icon, detail = get_market_verdict(-0.1, "Medium")
        assert verdict == "Neutral"
        assert "stock-specific" in detail.lower()

    def test_na_vix_returns_neutral(self):
        """N/A VIX → Neutral."""
        from market_data import get_market_verdict
        verdict, icon, detail = get_market_verdict(0.5, None)
        assert verdict == "Neutral"
        assert "unavailable" in detail.lower()

    def test_none_vix_returns_neutral(self):
        """None VIX → Neutral fallback."""
        from market_data import get_market_verdict
        verdict, icon, detail = get_market_verdict(0.0, "N/A")
        assert verdict == "Neutral"


class TestMarketPulse:
    """Tests for get_market_pulse()."""

    def test_graceful_on_yfinance_failure(self, mocker):
        """yfinance failure should return None-safe dict, not crash."""
        mock_ticker = mocker.patch("yfinance.Ticker")
        mock_ticker.return_value.history.side_effect = Exception("API down")
        from market_data import get_market_pulse
        result = get_market_pulse()
        assert result is not None
        assert result["nifty_price"] is None
        assert result["nifty_change_pct"] is None

    def test_graceful_on_empty_data(self, mocker):
        """Empty dataframe should return None-safe dict."""
        import pandas as pd
        mock_ticker = mocker.patch("yfinance.Ticker")
        mock_ticker.return_value.history.return_value = pd.DataFrame()
        from market_data import get_market_pulse
        result = get_market_pulse()
        assert result is not None
        assert result["nifty_price"] is None
