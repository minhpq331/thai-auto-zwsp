# -*- coding: utf-8 -*-
"""
Wrapper for PyICU word segmentation
https://github.com/ovalhub/pyicu/blob/master/samples/break.py
https://github.com/danhhong/khmer_segment/blob/main/khmer_segment_icu.py
"""
from waitress import serve
from flask import Flask, request, jsonify

from core import segment

app = Flask(__name__)

@app.route("/", methods = ['post'])
def index():
    data = request.json['data']
    return {'data': segment(data) }

serve(app, port=5000)
