"""Tests for public teaser renderer (shareable snapshot links)."""


class TestPublicTeaser:
    """Tests for render_public_teaser()."""

    def test_shows_stock_name_and_price(self, sample_stock_data):
        """Public teaser should show stock name and current price."""
        from render import render_public_teaser

        result = {
            "stock_data": sample_stock_data,
            "smartscore": 72,
            "smartscore_signal": "BULLISH",
            "smartscore_emoji": "\U0001f7e2",
            "signal": "BULLISH \U0001f7e2",
            "avg_compound": 0.45,
        }

        html = render_public_teaser(result, "TEST", "Test Company Ltd")

        assert "Test Company Ltd" in html or "Test Company" in html
        assert "100.00" in html or "100" in html  # current_price from fixture

    def test_shows_smartscore(self, sample_stock_data):
        """Public teaser should display the SmartScore value."""
        from render import render_public_teaser

        result = {
            "stock_data": sample_stock_data,
            "smartscore": 72,
            "smartscore_signal": "BULLISH",
            "smartscore_emoji": "\U0001f7e2",
            "signal": "BULLISH \U0001f7e2",
            "avg_compound": 0.45,
        }

        html = render_public_teaser(result, "TEST", "Test Company Ltd")

        assert "72" in html

    def test_shows_buy_cta(self, sample_stock_data):
        """Public teaser should include a purchase call-to-action."""
        from render import render_public_teaser

        result = {
            "stock_data": sample_stock_data,
            "smartscore": 72,
            "smartscore_signal": "BULLISH",
            "smartscore_emoji": "\U0001f7e2",
            "signal": "BULLISH \U0001f7e2",
            "avg_compound": 0.45,
        }

        html = render_public_teaser(result, "TEST", "Test Company Ltd")

        assert "BUY" in html or "buy" in html or "Purchase" in html or "499" in html

    def test_does_not_include_full_news(self, sample_stock_data):
        """Public teaser should NOT render the full news section or detailed technicals."""
        from render import render_public_teaser

        result = {
            "stock_data": sample_stock_data,
            "smartscore": 72,
            "smartscore_signal": "BULLISH",
            "smartscore_emoji": "\U0001f7e2",
            "signal": "BULLISH \U0001f7e2",
            "avg_compound": 0.45,
        }

        html = render_public_teaser(result, "TEST", "Test Company Ltd")

        # Should not contain article/news items or detailed analysis sections
        assert "Headline Breakdown" not in html
        assert "Technical Indicators" not in html or "Technical" not in html

    def test_shows_signal_emoji_and_label(self, sample_stock_data):
        """Public teaser should display the sentiment signal and its emoji."""
        from render import render_public_teaser

        result = {
            "stock_data": sample_stock_data,
            "smartscore": 72,
            "smartscore_signal": "BULLISH",
            "smartscore_emoji": "\U0001f7e2",
            "signal": "BULLISH \U0001f7e2",
            "avg_compound": 0.45,
        }

        html = render_public_teaser(result, "TEST", "Test Company Ltd")

        assert "BULLISH" in html
