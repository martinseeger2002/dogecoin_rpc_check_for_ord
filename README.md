
# Dogcoin Ord TXID finder

This collection of Python scripts is designed to analyze Dogecoin transactions. The main functionality revolves around examining specific transaction IDs (TXIDs) in the Dogecoin network, identifying ord in transactions.

## Files

- `getTXIDinfo.py`: This script contains functions to interact with the Dogecoin network using RPC (Remote Procedure Call). It fetches detailed information about a given TXID.

- `main.py`: This script uses `getTXIDinfo.py` to analyze a specific TXID for certain criteria, such as checking if the TXID contains a specific sequence of characters.

- `RPC.conf`: Configuration file for storing RPC connection details like user, password, IP, and port.

## Requirements

- Python 3.x
- `bitcoinrpc` Python package for interacting with the Dogecoin network.

## Setup

1. Ensure Python 3.x is installed on your system.
2. Install the `bitcoinrpc` package using pip:
   ```bash
   pip install python-bitcoinrpc
   ```
3. Configure the `RPC.conf` file with your RPC credentials.

## Usage

Run the `main.py` script with Python:

```bash
python main.py
```

The script is currently set up to analyze a hardcoded TXID. Modify `main.py` to analyze different TXIDs as needed.


