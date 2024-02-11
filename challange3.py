import sqlite3
from hashlib import (md5,sha256,sha512,sha384,sha3_224,sha3_256,sha3_384,sha3_512,blake2b,blake2s,sha1,sha224)
funkcje =[md5,sha256,sha512,sha384,sha3_224,sha3_256,sha3_384,sha3_512,blake2b,blake2s,sha1,sha224] 


def zlam_hash(hash):
    for funkcja in funkcje:
        with open("rockyou.txt", "r") as slownik:
            for linia in slownik:
        
    return hash


db = sqlite3.connect("users-challange.db").fetchall()
c = db.cursor()
users = c.execute("Select * from users")
c.close()
print(users)
for u in users:
    #id
    print(u[1])

    #imie
    print(u[1])
    #email
    print(u[2])
    #hash
    print(u(3))