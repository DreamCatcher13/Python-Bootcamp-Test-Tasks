import hashlib

s = "Python Bootcamp"

#hashing the string
md5 = hashlib.md5(s.encode())
sha1 = hashlib.sha1(s.encode())
sha256 = hashlib.sha256(s.encode())
sha384 = hashlib.sha384(s.encode())
sha512 = hashlib.sha512(s.encode())

#printing result
result = (
    f'"{s}" hashing results:\n'
    f'      MD5 hash: {md5.hexdigest()}\n'
    f'      SHA1 hash: {sha1.hexdigest()}\n'
    f'      SHA-256 hash: {sha256.hexdigest()}\n'
    f'      SHA-384 hash: {sha384.hexdigest()}\n'
    f'      SHA-512 hash: {sha512.hexdigest()}'
)
print(result)

