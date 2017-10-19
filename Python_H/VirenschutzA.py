from Crypto.Cipher import AES
import base64, random, string, sys

BLOCK_SIZE = 32
PADDING = "{"

pad = lambda s: str(s) + (BLOCK_SIZE - len(str(s)) % BLOCK_SIZE) * PADDING
Enc = lambda c, m: c.encrypt(pad(m))
Dec = lambda c, e: c.decrypt(e).rstrip(PADDING)


