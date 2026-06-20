"""Tests for entry price persistence and portfolio news matching."""

import pytest


class TestEntryPrices:
    """Tests for save_entry_price() and load_entry_prices()."""

    def test_save_and_load_roundtrip(self, tmp_path, monkeypatch):
        from persistence import save_entry_price, load_entry_prices
        from pathlib import Path

        # Redirect data dir to tmp_path
        monkeypatch.setattr("persistence.DATA_DIR", tmp_path)
        monkeypatch.setattr("persistence.ENTRY_PRICES_FILE", tmp_path / "entry_prices.json")

        save_entry_price("RELIANCE", 2850.50)
        prices = load_entry_prices()

        assert prices["RELIANCE"] == 2850.50

    def test_load_empty_returns_empty_dict(self, tmp_path, monkeypatch):
        from persistence import load_entry_prices
        from pathlib import Path

        monkeypatch.setattr("persistence.DATA_DIR", tmp_path)
        monkeypatch.setattr("persistence.ENTRY_PRICES_FILE", tmp_path / "entry_prices.json")

        prices = load_entry_prices()

        assert prices == {}

    def test_update_existing_entry(self, tmp_path, monkeypatch):
        from persistence import save_entry_price, load_entry_prices
        from pathlib import Path

        monkeypatch.setattr("persistence.DATA_DIR", tmp_path)
        monkeypatch.setattr("persistence.ENTRY_PRICES_FILE", tmp_path / "entry_prices.json")

        save_entry_price("RELIANCE", 2850.50)
        save_entry_price("RELIANCE", 2900.00)
        prices = load_entry_prices()

        assert prices["RELIANCE"] == 2900.00

    def test_calc_portfolio_pnl(self):
        from persistence import calc_portfolio_pnl

        result = calc_portfolio_pnl(2850.50, 3277.00, 12)

        assert result["pnl_abs"] == pytest.approx(5118.0, rel=0.1)
        assert "pnl_pct" in result

    def test_calc_portfolio_pnl_negative(self):
        from persistence import calc_portfolio_pnl

        result = calc_portfolio_pnl(512.0, 454.0, 14)

        assert result["pnl_abs"] < 0
        assert result["pnl_pct"] < 0

    def test_calc_portfolio_pnl_none_price(self):
        from persistence import calc_portfolio_pnl

        result = calc_portfolio_pnl(100.0, None, 10)

        assert result["pnl_pct"] == 0.0
        assert result["pnl_abs"] == 0.0


class TestPortfolioNewsMatch:
    """Tests for find_portfolio_matches()."""

    def test_finds_mention_in_headline(self):
        from persistence import find_portfolio_matches

        news = [
            {"title": "RELIANCE announces new energy division"},
            {"title": "TCS wins large deal"},
        ]
        portfolio = ["RELIANCE", "HDFCBANK"]

        matches = find_portfolio_matches(news, portfolio)

        assert "RELIANCE" in matches
        assert "TCS" not in matches

    def test_returns_empty_when_no_match(self):
        from persistence import find_portfolio_matches

        news = [
            {"title": "Markets open flat"},
            {"title": "IT sector outlook"},
        ]
        portfolio = ["RELIANCE", "HDFCBANK"]

        matches = find_portfolio_matches(news, portfolio)

        assert matches == {}

    def test_returns_all_matched_tickers(self):
        from persistence import find_portfolio_matches

        news = [
            {"title": "RELIANCE up 3%, TCS down 1%"},
            {"title": "Nothing about ITC here"},
        ]
        portfolio = ["RELIANCE", "TCS", "HDFCBANK"]

        matches = find_portfolio_matches(news, portfolio)

        assert matches.get("RELIANCE")
        assert matches.get("TCS")
        assert "ITC" not in matches
        assert "HDFCBANK" not in matches
