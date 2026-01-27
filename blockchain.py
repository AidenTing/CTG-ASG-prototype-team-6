#For Blockchain logic
from block import Block, sha256

class Blockchain:
#Initialise blockchain
    def __init__(self):
        self.chain = [self.create_genesis_block()]

#Genesis BLock for chain to start
    def create_genesis_block(self):
        return Block(0, [], "0")

#Adding new blocks to the chain
    def add_block(self, transactions):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, prev_block.hash)
        self.chain.append(new_block)

#Blockchain validaton checking
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != sha256(current.block_data()):
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
