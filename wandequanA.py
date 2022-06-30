# 万德全A
import time
import requests
URL = 'https://api.jiucaishuo.com/v2/guzhi/newtubiaolinedata'

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
}
# year:5
data = {"gu_code": "881003.WI", "pe_category": "pb", "year": 5, "ver": "new", "type": "pc", "data_source": "xichou",
        "version": "2.0.0", "authtoken": "fF1qu720kZQZf14E2zhhAgMFCpjuC/qW", "act_time": int(time.time() * 1000),
        "tirgkjfs": "46", "abiokytke": "d3", "u54rg5d": "94", "kf54ge7": "2", "tiklsktr4": "6", "lksytkjh": "18de",
        "sbnoywr": "b1", "bgd7h8tyu54": "2b", "y654b5fs3tr": "6", "bioduytlw": "f", "bd4uy742": "8", "h67456y": "c18",
        "bvytikwqjk": "2b", "ngd4uy551": "18", "bgiuytkw": "de", "nd354uy4752": "3", "ghtoiutkmlg": "6dc",
        "bd24y6421f": "16", "tbvdiuytk": "c", "ibvytiqjek": "b7", "jnhf8u5231": "de", "fjlkatj": "946",
        "hy5641d321t": "68", "iogojti": "6", "ngd4yut78": "dc", "nkjhrew": "8", "yt447e13f": "5", "n3bf4uj7y7": "8",
        "nbf4uj7y432": "d3", "yi854tew": "a3", "h13ey474": "a32", "quikgdky": "94"}

res = requests.post(url=URL, headers=headers, json=data)
print(res.json())