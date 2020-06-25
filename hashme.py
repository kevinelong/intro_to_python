import hashlib

salt = "kevinelong"
s = "password" + salt
e = s.encode()
b = bytearray()
b.extend(e)

hashed = hashlib.sha256(e)
result = hashed.hexdigest()

print(result)
