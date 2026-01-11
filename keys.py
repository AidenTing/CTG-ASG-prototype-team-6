#For key gen using ECC
from ecdsa import SigningKey, SECP256k1

class KeyPair:

#Generate Private Key + Public Key
    def __init__(self):
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

#Digital SIgnature usig ECDSA
    def sign(self, message: bytes) -> bytes:
        return self.private_key.sign(message)

#Signature verifying
    def verify(self, signature: bytes, message: bytes) -> bool:
        return self.public_key.verify(signature, message)

#Convert both keys to be able to printable/displayable
    def get_private_key_hex(self):
        return self.private_key.to_string().hex()
    
    def get_public_key_hex(self):
        return self.public_key.to_string().hex()