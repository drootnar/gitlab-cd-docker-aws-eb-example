# -*- coding: utf-8 -*-
import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def greetings():
    name = request.args.get('name', 'anonymous')
    return "Hello {}!".format(name)
