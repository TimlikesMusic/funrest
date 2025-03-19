from argon2 import PasswordHasher

ph = PasswordHasher()

hash = ph.hash("user123")
print(type(hash))
verify = ph.verify(hash, "user123")


