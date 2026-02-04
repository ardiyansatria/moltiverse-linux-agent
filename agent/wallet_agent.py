import requests
from datetime import datetime

# ----- CONFIG -----
MONAD_RPC_URL = "https://rpc.monk.testnet/"  # Ganti sesuai RPC

# ----- FUNCTIONS -----
def rpc_call(method, params=[]):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    response = requests.post(MONAD_RPC_URL, json=payload)
    return response.json()

def wallet_summary(address):
    balance_response = rpc_call("eth_getBalance", [address, "latest"])
    balance = int(balance_response.get("result", "0x0"), 16) / 10**18

    summary = f"""
----------------------------
Wallet Summary:
Address: {address}
Balance: {balance} ETH
Timestamp: {datetime.now().isoformat()}
----------------------------
"""
    print(summary)
    with open("wallet_log.txt", "a") as f:
        f.write(summary + "\n")

def decision_logic(balance):
    if balance > 0.01:
        action = "Ready to trade"
    else:
        action = "Waiting for funds"

    log = f"Decision: {action} at {datetime.now().isoformat()}"
    print(log)
    with open("wallet_log.txt", "a") as f:
        f.write(log + "\n")
    return action

# ----- MAIN -----
if __name__ == "__main__":
    # Ganti dengan wallet hasil generate
    my_address = "0xABC123..."  

    # Step 1: Wallet summary
    wallet_summary(my_address)

    # Step 2: Decision logic
    balance = 0.0  # Bisa diupdate dari RPC
    decision_logic(balance)
