from Crypto.Cipher import AES    
from Crypto.Hash import SHA256

password = ("abda")    
hash_obj = SHA256.new(password.encode('utf-8'))    
hkey = hash_obj.digest()

encrypted_msg = b'\x1bkw\x00\x01#\x1dv\xd1\x1e\xfb\xba\xac_b\x02T\xfbZ\xca\xac8Y\\8@4\xba;\xe1\x11$\x19\xe8\x89t\t\xc8\xfd\x93\xd8-\xba\xaa\xbe\xf1\xa0\xab\x18\xa0\x12$\x9f\xdb\x08~\x81O\xf0y\xe9\xef\xc41\x1a$\x1cN3\xe8F\\\xef\xc1G\xeb\xdb\xa1\x93*F\x1b|\x1c\xec\xa3\x04\xbf\x8a\xd9\x16\xbc;\xd2\xaav6pWX\xc1\xc0o\xab\xd5V^\x1d\x11\xe4}6\xa4\x1b\\G\xd4e\xc2mP\xdb\x9b\x9f\xb0Z\xf12'

def decrypt(msg):
    decipher = AES.new(hkey, AES.MODE_ECB)
    result = decipher.decrypt(msg).decode('utf-8')
    return result

print(decrypt(encrypted_msg))
