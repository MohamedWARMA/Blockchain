import ecdsa
import binascii
import uuid

class user:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = str(uuid.uuid4())

        #Generate ECDSA Keys
        self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def get_public_key(self):
        return binascii.hexlify(self.public_key.to_string()).decode()

    def sign_transaction(self, transaction):
        transaction_str = str(transaction).encode()
        signature = self.private_key.sign(transaction_str)
        return binascii.hexlify(signature).decode()