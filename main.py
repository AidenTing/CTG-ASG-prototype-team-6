from keys import KeyPair
from transaction import Transaction
from blockchain import Blockchain
import hashlib

def main():
    print("=== Bitcoin Cryptography Prototype ===\n")

#Step 1: Show Keygen works by printing (ECC)
    alice = KeyPair()
    bob = KeyPair()
    print("=== Step 1:Key Generation (ECC) ===")
    print()
    print("=== Alice Keys ===")
    print("Private Key:", alice.get_private_key_hex())
    print("Public Key :", alice.get_public_key_hex())
    print()
    print("=== Bob Keys ===")
    print("Private Key:", bob.get_private_key_hex())
    print("Public Key :", bob.get_public_key_hex())
    print()

#Step 2: Create the BlockChain
    print("=== Step 2: Blockchain Creation ===")
    blockchain = Blockchain()
    print("blockchain created with genesis block.")
    print()

#Step 3: Create a Trasnsaction
    print("=== Step 3: Create Transaction ===")
    tx1 = Transaction(alice.public_key, bob.public_key, 10)
    print("Sender  : Alice")
    print("Receiver: Bob")
    print("Amount  : 10 BTC")
    print()

#Step 4: Sign Transaction 
    print("=== Step 4: Signing Transaction (ECDSA) ===")
    tx1.sign_transaction(alice.private_key)
    print("Transaction Signature:", tx1.signature.hex())
    print()

#Step 5: Verify Signature
    print("=== Step 5: Verify Signature ===")
    print("Signature valid:", tx1.is_valid())
    print()

#Step 6: Tampering Transaction
    print("=== Step 6: Transaction Tampering (SHA-256) ===")
    original_hash = hashlib.sha256(tx1.transaction_data()).hexdigest()
    tx1.amount = 999
    tampered_hash = hashlib.sha256(tx1.transaction_data()).hexdigest()
    print("Original Hash :", original_hash)
    print("Tampered Hash :", tampered_hash)
    print("Signature valid after tampering:", tx1.is_valid())
    print()

#Step 7: Fix Tampered Transaction
    print("=== Step 7: Re-signing After Fix ===")
    tx1.amount = 10
    print("Old signature valid:", tx1.is_valid())
    tx1.sign_transaction(alice.private_key)
    print("New Signature:", tx1.signature.hex())
    print("Signature valid after re-signing:", tx1.is_valid())
    print()

#Step 8: Mining Block
    print("=== Step 8: Mining Block (Proof of Work) ===")
    print("Mining block...")
    blockchain.add_block([tx1])
    print("Block successfully mined")
    print()

#Step 9: Blockchain Validation
    print("=== Step 9: Blockchain Validation ===")
    print("Blockchain valid:", blockchain.is_chain_valid())
    print()

#Step 10: Blockchain Tampering
    print("=== Step 10: Tampering Blockchain ===")
    blockchain.chain[1].transactions[0].amount = 999
    print("Blockchain valid after tampering:", blockchain.is_chain_valid())
    print()

if __name__ == "__main__":
    main()
