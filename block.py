#For Block + Mining code
import time
import hashlib

#Convert bytes apply hashing display in hex string
def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

class Block:

#Initialise block 
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.mine_block()

#Construct block header change to bytes than hash for chain, integrity, POF
    def block_data(self):
        tx_data = "".join([str(tx.transaction_data()) for tx in self.transactions])
        return f"{self.index}{self.timestamp}{tx_data}{self.previous_hash}{self.nonce}".encode()

#POF loop
    def mine_block(self, difficulty=4):
        while True:
            hash_result = sha256(self.block_data())
            if hash_result.startswith("0" * difficulty):
                return hash_result
            self.nonce += 1

