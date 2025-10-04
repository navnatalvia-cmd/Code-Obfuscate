import base64
enc = "cHJpbnQoZigiZGVmIikp"
dec = base64.b64decode(enc).decode('utf-8')
exec(dec)
