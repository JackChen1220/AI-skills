# FAQ Icon Inventory

Use the source filename as the semantic anchor. The category name should drive the motif before visual polish.

| Source filename | Meaning | Motif | Palette token | Notes |
| --- | --- | --- | --- | --- |
| `About Us.png` | Company/about page | Webull crescent/ring mark | `blue.brand.deep` | Brand-led exception; symbol can sit high inside circle. |
| `Account and Login.png` | Account access and sign-in | Wallet/card with small flap | `blue.account` | Rounded white wallet, light blue tint planes. |
| `Account openning.png` | Account opening/onboarding | User avatar | `red.market` | Keep typo if matching source; otherwise use "Account opening". |
| `Advisor.png` | Advisor or representative | Person bust with tie | `orange.trading` | Simple human silhouette, no facial detail. |
| `Asset Transfer.png` | Transfer brokerage assets | House/account container with transfer arrows | `purple.transfer` | Good precedent for inbound/outbound asset movement. |
| `Bank Transfer.png` | Bank transfer | Dollar coin with arrows | `cyan.transfer` | Coin-plus-arrow grammar. |
| `Bind bank card.png` | Link bank card | Credit card with chain link badge | `orange.trading` | Duplicate visual with `Bind card.png`. |
| `Bind card.png` | Link card | Credit card with chain link badge | `orange.trading` | Duplicate visual with `Bind bank card.png`. |
| `China stock.png` | China market | China flag stars inside circle | `red.market` | Flag exception; no centered white pictogram. |
| `Crypto in:out.png` | Crypto deposit/withdrawal | Bitcoin glyph with circular arrows | `orange.crypto` | Use colon only when matching source naming. |
| `Crypto.png` | Crypto category | Bitcoin glyph | `orange.crypto` | White bitcoin mark centered. |
| `Deposit & Withdrawal.png` | Cash deposit and withdrawal | Dollar coin with direction arrow | `orange.trading` | Similar to transfer, warmer finance palette. |
| `Documents and Taxes.png` | Documents and tax forms | Document/receipt sheet | `orange.trading` | White paper with same-hue line accents. |
| `Features and Navigation.png` | Product features/navigation | Desktop screen or app panel | `blue.nav` | Interface metaphor, wide but compact. |
| `Fees.png` | Fees and charges | Money bag with dollar | `orange.trading` | Centered money bag, rounded top. |
| `Fixed investment.png` | Fixed investment/savings | Money bag or scheduled savings mark | `yellow.money` | Same visual family as recurring deposit. |
| `Foreexchange.png` | Foreign exchange/FX | Large `FX` text with wave lines | `cyan.fx` | Legacy large source and typo; normalize new exports to 108px. |
| `Foreign exchange.png` | Foreign exchange | Dollar coin with bidirectional arrows | `purple.transfer` | Prefer for money-conversion questions. |
| `Fractional Stock Shares.png` | Fractional shares | Cut diamond/segmented share mark | `teal.secure` | Abstract split-asset metaphor. |
| `Fraud Prevention.png` | Fraud prevention/security | Shield with check | `orange.trading` | Trust/security without lock. |
| `Green bond.png` | Green bonds/ESG bond | Bars plus leaf | `green.esg` | Finance plus sustainability. |
| `HK stock.png` | Hong Kong market | Hong Kong bauhinia flag mark | `red.market` | Flag exception. |
| `IPO.png` | IPO category | Large `IPO` text | `orange.crypto` | Text-mark exception; bold italic letters. |
| `ISA(Individual Savings Account).png` | UK ISA account | Large `ISA` text | `yellow.money` | Text-mark exception. |
| `Info.png` | Information/help | Lowercase info glyph | `blue.info` | White/light-blue info dot and stem. |
| `Japan stock.png` | Japan market | Japan flag circle | flag palette | Flag exception; mostly white with red center disk. |
| `Margin.png` | Margin financing | Hand holding dollar coin | `cyan.transfer` | Hand and coin, no extra detail. |
| `Market Data and Analysis.png` | Market data/analytics | Rising chart arrow | `yellow.money` | Chart plus arrow, white/tint layers. |
| `Market rule.png` | Market rules | Clipboard checklist | `orange.trading` | Rounded clipboard, horizontal rule lines. |
| `OnlineService.png` | Online customer service | Headset with face/chat mark | `blue.brand.deep` | Legacy 96px source; support category. |
| `Option.png` | Options trading | Contract/card with star | `cyan.transfer` | Keep compact document metaphor. |
| `Password&login.png` | Password and login | Open lock | `teal.secure` | Lock can be unlocked/open to imply access recovery. |
| `Position profit and loss.png` | Position P/L | Bar chart in rounded panel | `purple.transfer` | White panel and vertical bars. |
| `Promotions.png` | Promotions/offers | Gift box | `purple.transfer` | Centered gift, ribbon notch. |
| `Recurring Deposit.png` | Recurring deposit | Scheduled savings/money bag | `yellow.money` | Same family as fixed investment. |
| `Retirement Account.png` | Retirement account | `IRA` text | `blue.account` | Text-mark exception. |
| `Short.png` | Short selling | Cart/down arrow metaphor | `purple.transfer` | Downward motion signal. |
| `Trading and Investing.png` | Trading/investing | Two-way trade arrow | `orange.trading` | Circular white badge with orange arrows. |
| `UK Meridian Membership.png` | UK membership | Webull ring/membership mark | `blue.brand.deep` | Brand-led exception. |
| `UK stock.png` | UK market | UK flag inside circle | flag palette | Flag exception; fill circle with flag. |
| `US bonds.png` | US bonds | Bond certificate with dollar | `blue.nav` | White/tint certificate. |
| `US stock.png` | US market | US flag inside circle | flag palette | Flag exception; fill circle with flag. |
| `Wealth management.png` | Wealth management | Receipt/certificate with dollar | `orange.trading` | Finance-document hybrid. |
| `Webull Premium.png` | Premium product | Dark premium Webull artwork | premium artwork | Legacy photo/brand exception; do not generalize to normal icons. |

## Closest-match selection

- For a new account or access category, start from `Account and Login.png`, `Password&login.png`, or `Account openning.png`.
- For a new transfer category, start from `Bank Transfer.png`, `Asset Transfer.png`, `Foreign exchange.png`, or `Deposit & Withdrawal.png`.
- For a new investing category, start from `Trading and Investing.png`, `Market Data and Analysis.png`, `Fees.png`, or `Margin.png`.
- For a new security category, start from `Fraud Prevention.png` or `Password&login.png`.
- For a new country market, use a circular flag crop if the source set already treats that country as a flag category.
- For a new named product or membership, prefer a simple text/brand mark only if a short abbreviation is recognizable at 24px display size.
