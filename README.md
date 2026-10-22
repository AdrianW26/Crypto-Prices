# Crypto Prices

Fetches the current prices of Bitcoin, Ethereum and Solana in GBP, USD and EUR from the CoinGecko API, saves each coin's prices to its own CSV file, then reports the highest-priced, lowest-priced and average coin price in GBP.

## Requirements

- Python 3.9 or later
- Internet connection (the script calls the public CoinGecko API; no API key needed)

## Setup

1. Clone the repository and move into the folder:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```


2. Install the required packages:

   ```bash  
   pip install requests pandas
   ```

## Running

```bash
python3 Crypto\ Prices.py
```

On Windows, use `python` instead of `python3`.

## Output

The script creates three CSV files in the same folder, each with `currency` and `price` columns:

- `bitcoin.csv`
- `ethereum.csv`
- `solana.csv`

It then prints a summary such as:

```
The highest priced coin in GBP is bitcoin at £61,194.00
The lowest priced coin in GBP is solana at £78.27
The average price in GBP across the three coins is £21,024.86
```

Prices are live, so the figures will differ each time you run it.

## Notes

- CoinGecko's free API is rate-limited. If you see `Error: 429`, wait about a minute and run the script again.
