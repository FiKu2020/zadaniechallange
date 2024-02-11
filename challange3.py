import sqlite3
import  hashlib
from hashlib import (md5,sha256,sha512,sha384,sha3_224,sha3_256,sha3_384,sha3_512,blake2b,blake2s,sha1,sha224)
funkcje =[md5,sha256,sha512,sha384,sha3_224,sha3_256,sha3_384,sha3_512,blake2b,blake2s,sha1,sha224] 


def zlam_hash(pojed_haslo):
    for funkcja in funkcje:
        with open("rockyou.txt", "r") as slownik:
            for linia in slownik:
                slowo = linia
                zahash_haslo = slowo.encode().hexdigest()
                if zahash_haslo == pojed_haslo:
                    return f"Znaleziono Haslo:{slowo}"
                else:
                    return f"Nie znalez hasla"


db = sqlite3.connect("users-challange.db")
c = db.cursor()
users = c.execute("SELECT * FROM users")
users.fetchall()
c.close()
print(users)
for u in users:
    #id
    print(f"Id uzytk:{u[0]}")
    #imie
    print(f"Imie i Nazwisko:{u[1]}")
    #email
    print(f"Email:{u[2]}")
    #hash
    print(f"zakod haslo:{u(3)}")
    odkod_haslo = zlam_hash(u[3])
    print(f"odkod haslo:{odkod_haslo}")

db.close