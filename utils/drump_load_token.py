import time
import base64
import hashlib
import random


def drumps_token(data):
    times = "".join(reversed(str(int(time.mktime(time.localtime())))))
    id = hashlib.sha256(base64.b64encode(str(data * 3).encode('utf-8')))
    sig = hashlib.sha256(base64.b64encode("PTSD".encode('utf-8')))
    result = times + id.hexdigest() + str(round(random.random() * 10000000))[:4] + "$" + sig.hexdigest()
    return result


def loads_token(data, id):
    try:
        times = eval("".join(reversed(data[:10])))
        now = time.mktime(time.localtime())
        if now - times > 24 * 3600:
            return False
        id = hashlib.sha256(base64.b64encode(str(id * 3).encode('utf-8')))
        sig = hashlib.sha256(base64.b64encode("PTSD".encode('utf-8')))
        data = data.split("$")
        if id.hexdigest() == data[0][10:-4] and sig.hexdigest() == data[1]:
            return True
        else:
            return False
    except Exception:
        return False
