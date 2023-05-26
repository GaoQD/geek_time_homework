"""
============================
@description:TODO
@author:gaoqd
@time:2023/5/26  22:15
@version: 1.0
@file: test_create_hero.py
============================
"""
import pytest

from pytest_test_framework_1.hero_management import HeroManagement


class TestCreateHero:
    def setup(self):
        self.hero_management = HeroManagement()

    @pytest.mark.parametrize("name", ['jinkx', 'ez'])
    @pytest.mark.parametrize("volume", [1, 2])
    def test_create_hero_success(self, name, volume):
        """
        创建英雄成功的测试用例
        :param name:
        :param volume:
        :return:
        """
        self.hero_management.create_hero(name, volume, 30)
        res = self.hero_management.find_hero(name)
        assert res.get('name') == name
        assert res.get('volume') == volume

    @pytest.mark.parametrize("volume", [0, 100], ids=["血量边界值为0", "血量边界值为100"])
    def test_create_hero_fail_1(self, volume):
        """
        创建英雄失败的测试用例
        :param volume:
        :return:
        """
        self.hero_management.create_hero('name', volume, 30)
        res = self.hero_management.find_hero('name')
        assert res == False

    @pytest.mark.parametrize("name,volume", [("jinx", 0), ("ez", 100)], ids = ["血量边界值为0", "血量边界值为100"])
    def test_create_hero_fail_2(self, name, volume):
        """
        创建英雄失败的测试用例
        :param power:
        :return:
        """
        self.hero_management.create_hero(name, volume, 30)
        res = self.hero_management.find_hero(name)
        assert res == False
