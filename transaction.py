#Transaction Logic Code
import hashlib

class Transaction:
#Initalise Transaction
    def __init__(self, sender_pub, receiver_pub, amount):
        self.sender_pub = sender_pub
        self.receiver_pub = receiver_pub
        self.amount = amount
        self.signature = None

#byte representation for it to be hashed, digitally signed and for verification
    def transaction_data(self):
        return f"{self.sender_pub}{self.receiver_pub}{self.amount}".encode()

#Use ECDSA to sign transaction
    def sign_transaction(self, sender_private_key):
        self.signature = sender_private_key.sign(self.transaction_data())

#Verification
    def is_valid(self):
        if self.signature is None:
            return False
        try:
            return self.sender_pub.verify(self.signature, self.transaction_data())
        except:
            return False
