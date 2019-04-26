# -*- coding: utf-8 -*-

import os

from flask import Flask, request, jsonify
from natto import MeCab


app = Flask(__name__)
# http://datalove.hatenadiary.jp/entry/flask-jsonify-how-to-encode-japanese
app.config['JSON_AS_ASCII'] = False

dicdir = os.environ.get("MECAB_DICDIR")
if dicdir:
    tagger = MeCab("-d %s" % dicdir)
else:
    tagger = MeCab()


@app.route("/parse", methods=['GET'])
def index():
    result = {"result": []}
    query = request.args.get("q", default="", type=str)
    for line in tagger.parse(query).split("\n"):
        line = line.strip()
        parts = line.split("\t", 1)
        if line == "EOS" or len(parts) <= 1:
            continue
        surface, features = parts
        result["result"].append({
            "surface": surface,
            "features": features.split(",")
        })
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
