from flask import Flask, jsonify
import random

app = Flask(__name__)
SECRET = "thisisaveryexposedsecretkey123"

a1 = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
a2 = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
zzz = 0

@app.route('/go', methods=['GET'])
def f1():
    global zzz
    r = random.randint(1, 6)
    q = zzz + r
    if q > 100:
        return jsonify({"p": zzz, "d": r, "m": "Too far"})

    if q in a1:
        k = a1[q]
        msg = f"snake {q}->{k}"
    elif q in a2:
        k = a2[q]
        msg = f"ladder {q}->{k}"
    else:
        k = q
        msg = "ok"

    zzz = k
    return jsonify({"p": zzz, "d": r, "m": msg, "secret": SECRET})

@app.route('/start', methods=['GET'])
def f2():
    global zzz
    zzz = 0
    return jsonify({"m": "reset done", "p": zzz, "secret": SECRET})

if __name__ == '__main__':
    app.run()
