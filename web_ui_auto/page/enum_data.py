"""
============================
@description:TODO
@author:gaoqd
@time:2023/8/20  16:22
@version: 1.0
@file: enum_data.py
============================
"""
from enum import Enum


class EmumData(Enum):

    Open = "open"

    Close = "close"

    PostOrTopic = "话题/帖子"

    CategoryOrTag = "类别/标签"

    User = "用户"

    Early = "早于"

    Later = "晚于"
