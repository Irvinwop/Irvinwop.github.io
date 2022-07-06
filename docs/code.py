from cryptography.fernet import Fernet
import base64, hashlib

def gen_fernet_key(passcode:bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    print(hlib)
    hlib.update(passcode)
    print(hlib)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))
passcode = UserInput
key = gen_fernet_key(passcode.encode('utf-8'))
fernet = Fernet(key)
data_input = "The message you were trying to send"
cypher_text = fernet.encrypt(data_input.encode('utf-8'))
decrypted_data = fernet.decrypt(cypher_text).decode('utf-8')

print(f"passcode: {passcode}")
print(f"data_input: {data_input}")
print(f"key: {key}")
print(f"cypher_text: {cypher_text}")
print(f"decrypted_data: {decrypted_data}")