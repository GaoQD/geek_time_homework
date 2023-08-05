
"""
============================
@description:TODO
@author:gaoqd
@time:2023/8/5  18:21
@version: 1.0
@file: test_wework.py
============================
"""

from datetime import datetime

import pytest

from wework.wework_page import WeworkPage


class TestWework:
    def setup_class(self):
        self.wework = WeworkPage()
        self.contact = self.wework.address_book()

    def teardown_class(self):
        ...

    @pytest.mark.parametrize('name', ['憨豆', 'hero', '_'])
    @pytest.mark.parametrize('phone', ['133'])
    def test_add_member(self, name, phone):
        phone = phone + datetime.now().strftime('%d%H%M%S')

        assert name == self.contact.manage().add_member(name=name, phone=phone).cancel().search(name).get_info()["name"]

    @pytest.mark.parametrize('name', ['憨豆', 'hero', '_'])
    def test_delete_member(self, name):
        self.contact.search(name).delete()
