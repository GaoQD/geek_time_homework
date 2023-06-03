"""
============================
@description:TODO
@author:gaoqd
@time:2023/6/3  20:21
@version: 1.0
@file: load_utils.py
============================
"""
import yaml


class LoadUtils:
    @classmethod
    def load_yaml(self, yaml_path):
        return yaml.safe_load(open(yaml_path))
