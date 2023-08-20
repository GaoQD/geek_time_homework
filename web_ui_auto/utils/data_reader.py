"""
============================
@description:TODO
@author:gaoqd
@time:2023/8/20  16:33
@version: 1.0
@file: data_reader.py
============================
"""
import json


class DataReader:
    @classmethod
    def load_json(cls, path):
        with open(path, 'r', encoding="utf-8") as f:
            return json.load(f)
