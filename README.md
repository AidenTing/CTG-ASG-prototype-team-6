Bitcoin Cryptography Prototype

Overview

This is a simplified Bitcoin prototype implemented in Python. It demonstrates the core cryptographic principles behind Bitcoin, including key generation, digital signatures, hashing, proof-of-work, and blockchain integrity.  

Note: This is an educational simulation and does not implement real Bitcoin transactions or networking.

---
Features

1. ECC Key Generation
   - Generates public-private key pairs using **secp256k1 elliptic curve**
   - Demonstrates ownership and authentication

2. Digital Signatures (ECDSA)
   - Transactions are signed by the sender’s private key
   - Verification is done using the sender’s public key
   - Shows that tampering invalidates signatures

3. Transaction Hashing (SHA-256)
   - Hashes transaction data for integrity
   - Changing any transaction field changes the hash

4. Proof-of-Work Mining
   - Simplified mining using SHA-256
   - Difficulty set by leading zeros in the hash
   - Demonstrates computational work required to mine a block

5. Blockchain Integrity
   - Blocks link to the previous block via hash
   - Any modification in a past block breaks the chain
   - Demonstrates immutability

---

File Structure
bitcoin-prototype/
│
├── keys.py # ECC key generation
├── transaction.py # Transaction logic (signing, verification)
├── block.py # Block structure + mining
├── blockchain.py # Blockchain logic (adding blocks, validation)
├── main.py # Demo / test run
├── requirements.txt # Python dependencies
└── README.md # Project explanation


---

Requirements

- Python 3.8+  
- ecdsa library

Install dependencies using:

pip install ecdsa

---

How to Run

python main.py

---

Notes

This prototype does not implement peer-to-peer networking or full Bitcoin scripting.
