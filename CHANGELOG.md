# Changelog

## [2.2.2] — 2026-06-20

### Fixed
- **SmartScore breadth now uses event-adjusted scores** — S_breadth was counting positive/negative headlines using raw VADER compound scores, ignoring event classifier adjustments. Headlines like "SEBI penalty" (VADER neutral, event-adjusted negative) are now correctly counted. This improves the composite Trend number and component bars.
- **History entries with 0.0 score no longer skipped** — `avg_compound` and `smartscore` truthiness checks now allow 0.0 values. A genuinely neutral day no longer falls out of the EWMA recency calculation and sparkline history.
- **Bold markdown rendering in sidebar** — `**PARAS**` was showing literal asterisks in the portfolio list because markdown bold syntax inside an HTML `<div>` with `unsafe_allow_html=True` isn't processed by Streamlit. Switched to `<strong>` HTML tag.

### Changed
- **Sidebar portfolio UX** — Clearer layout with "ADD STOCK" section header, "ATP" (Average Trade Price) field label instead of cryptic "₹", current price shown inline, buy price shown as "ATP: ₹X,XXX", heatmap legend, and explicit "No ATP set" state.
- **Portfolio field relabeled: "Buy Price" → "ATP"** — All sidebar labels, tooltips, and portfolio display lines now use "ATP" (Average Trade Price) for consistency with brokerage terminology.

## [2.2.1] — 2026-06-20

### Changed
- **Dead code removed:** `find_portfolio_matches()`, `_fill_from_nse()`, `_fetch_reddit_rdtcli()`, `detect_stagnation()` — net -101 lines.
- **Duplicate config unified:** `sentiment.py:SOURCE_WEIGHTS` removed; `get_source_weights()` now references `persistence.SOURCE_WEIGHTS_PRIOR` as single source of truth.
- **Reddit simplified:** OAuth-only path; rdt-cli fallback removed.
- **`detect_volume_spike()` wired** — now powers dashboard volume spike badges (was duplicated inline in render.py).

### Fixed
- **Sentiment history CSV mislabeled field** — `neg_count` was storing neutral count instead of actual negative headline count. Field semantics corrected.
- **Orphaned import removed:** `import subprocess` removed from data_fetcher.py.

## [2.2.0] — 2026-06-20

### Added
- **Portfolio P&L Tracking** — Set entry price when adding a stock. Sidebar shows live P&L (₹ and %) per holding, green for profit, red for loss.
- **Market Heatmap** — Compact 3-column grid in sidebar, every holding color-coded by daily % change.
- **Portfolio News Badges** — 📌 In portfolio badge on headlines that mention your holdings.
- **Volume Spike Detection** — `detect_volume_spike()` flags abnormal trading volume (N× 20-day average).
- **Stagnation Warnings** — `detect_stagnation()` flags stocks stuck in a tight range for 10+ days.

### Changed
- New entry price column in add-ticker row (sidebar)
- Metrics grid on landing page expanded from 4 to 6 columns

### Fixed
- **Trend sparkline blank on first analysis** — `render_sparkline()` now draws a dashed flat line + dot for single data points instead of returning empty SVG. Users see their SmartScore level immediately on first use.

## [2.1.3] — 2026-06-20

### Added
- **Shareable Snapshot Links** — Every ticker now has a public URL (`?ticker=RELIANCE`) showing SmartScore, signal, and price. Share on Telegram/WhatsApp/X. Full analysis unlocks behind the paywall.
- **Public changelog** — This file. Users can see what's new.
- **Feature request channel** — Feedback form linked in sidebar.

### Fixed
- **ETF 52W proximity crash** — `None` price (ETFs) caused `TypeError` in the proximity badge calculation. Guarded with `_is_valid_num()`.

## [2.1.2] — 2026-06-20

### Fixed
- **ETF NaN prices** — ETFs (NIFTYBEES, GOLDBEES, MIDCAPETF) showed `₹nan` and `nan%` because `float('nan')` is truthy in Python. Added `_nf()` NaN-safe extractor and `_is_valid_num()` guards throughout.

## [2.1.1] — 2026-06-20

### Changed
- Removed duplicate emoji-to-SVG mapping, consolidated to `get_signal_icon()`
- Collapsed 15-line if/elif sentiment chain to 7-line dict lookup
- Moved lazy imports to module level
- Removed 6 redundant `str()` wrappers

### Fixed
- Dashboard iframe height: formula-based (`2200 + n_news*120`)
- Mobile-responsive CSS breakpoints

## [2.1.0] — 2026-06-20

### Added
- 504 ticker aliases (was 72)
- 18 event types (was 13): `RATING_UPGRADE`, `JV_MOU`, `FUNDRAISE`, `CONTRACT_LOSS`, `DIVESTMENT`
- Bayesian calibration visible in dashboard
- 270 NSE tickers (was 85)

## [2.0.0] — 2026-06

### Added
- Bayesian source calibration (learns from 👍/👎 votes)
- Optional FinBERT transformer (`USE_FINBERT=true`)
- Lucide SVG icons throughout (replaced Unicode emojis)
- Yahoo Finance retries with jitter + suffix fallback

## [1.0.0] — 2026-05

### Added
- Initial release
- Live NSE stock data via yfinance
- Multi-source RSS news sentiment
- SmartScore composite (0-100)
- Technical indicators (RSI, SMA, MACD)
- Portfolio tracking
- Dark-themed HTML dashboard
