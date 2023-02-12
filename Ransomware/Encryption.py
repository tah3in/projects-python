from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

key2 = Fernet(key)
 #if replace key and kod(mr vampire) -> decrypt
name = key2.encrypt(b"mr vampire")

print(name)