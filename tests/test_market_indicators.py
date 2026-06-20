"""Tests for volume spike detection."""

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


class TestDetectStagnation:
    """Tests for detect_stagnation()."""

    def test_returns_stagnant_when_range_below_threshold(self):
        from indicators import detect_stagnation

        prices = [100.0, 100.5, 99.0, 100.0, 101.0, 100.0, 99.5, 100.2, 100.8, 100.1]
        result = detect_stagnation(prices, threshold_pct=3.0)

        assert result["stagnant"] is True
        assert result["range_pct"] < 3.0

    def test_returns_not_stagnant_when_range_above_threshold(self):
        from indicators import detect_stagnation

        prices = [100.0, 105.0, 110.0, 108.0, 112.0]
        result = detect_stagnation(prices, threshold_pct=3.0)

        assert result["stagnant"] is False
        assert result["range_pct"] >= 3.0

    def test_returns_not_stagnant_on_empty(self):
        from indicators import detect_stagnation

        result = detect_stagnation([])

        assert result["stagnant"] is False

    def test_returns_not_stagnant_on_none(self):
        from indicators import detect_stagnation

        result = detect_stagnation(None)

        assert result["stagnant"] is False
