
import hashlib, random

def uuid() -> int:
    return int(hashlib.sha256(str(random.random()).encode()).hexdigest(), 16) % (2**31 - 1)
