import requests
from datetime import datetime

# ----- CONFIG -----
MONAD_RPC_URL = "https://rpc.monk.testnet/"  # RPC optional (boleh offline)

# ----- FUNCTIONS -----
def rpc_call(method, params=[]):
    try:
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        response = requests.post(MONAD_RPC_URL, json=payload, timeout=5)
        return response.json()
    except Exception as e:
        print(f"[RPC WARNING] {e}")
        return {"result": "0x0"}  # fallback aman

def wallet_summary(address):
    balance_response = rpc_call("eth_getBalance", [address, "latest"])
    balance = int(balance_response.get("result", "0x0"), 16) / 10**18

    summary = f"""
----------------------------
Wallet Summary
Address   : {address}
Balance   : {balance} ETH
Timestamp : {datetime.now().isoformat()}
----------------------------
"""
    print(summary)

    with open("wallet_log.txt", "a") as f:
        f.write(summary + "\n")

    return balance

def decision_logic(balance):
    if balance > 0.01:
        action = "Ready to trade"
    else:
        action = "Waiting for funds"

    log = f"[DECISION] {action} | {datetime.now().isoformat()}"
    print(log)

    with open("wallet_log.txt", "a") as f:
        f.write(log + "\n")

    return action

# ----- MAIN -----
if __name__ == "__main__":
    my_address = "0xABC123ABC123ABC123ABC123ABC123ABC123AB"

    balance = wallet_summary(my_address)
    decision_logic(balance)
