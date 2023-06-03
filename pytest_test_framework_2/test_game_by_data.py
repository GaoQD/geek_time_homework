"""
============================
@description:TODO
@author:gaoqd
@time:2023/5/30  09:05
@version: 1.0
@file: test_game_by_data.py
============================
"""
import allure
import pytest

from pytest_test_framework_1.hero_management import HeroManagement
from pytest_test_framework_2.load_utils import LoadUtils


@pytest.fixture(params=LoadUtils.load_yaml('create_hero_data.yaml')['vloumesuccess'])
def get_volume_success_data(request):
    return request.param + 1


@pytest.fixture(params=LoadUtils.load_yaml('create_hero_data.yaml')['volume_fail'])
def get_volume_fail_data(request):
    return request.param + 1


@pytest.fixture(params=LoadUtils.load_yaml('create_hero_data.yaml')['name_success'])
def get_name_success_data(request):
    return request.param


@pytest.fixture(params=LoadUtils.load_yaml('create_hero_data.yaml')['name_fail'])
def get_name_fail_data(request):
    return request.param


@pytest.fixture(params=LoadUtils.load_yaml('create_hero_data.yaml')['power_success'])
def get_power_success_data(request):
    return request.param + 1


@pytest.fixture(params=LoadUtils.load_yaml('create_hero_data.yaml')['power_fail'])
def get_power_fail_data(request):
    return request.param + 1


class TestGameByData:

    def setup(self):
        self.hero = HeroManagement()

    @pytest.mark.valid_equivalence
    def test_create_hero_volume_success(self, get_volume_success_data):
        """
        有效等价类
        :param get_volume_success_data:
        :return:
        """
        self.hero.create_hero("jinx", get_volume_success_data, 20)
        res = self.hero.find_hero("jinx")
        assert res.get("volume", get_volume_success_data)
        allure.attach.file(open(f'/results/{get_volume_success_data}.png', mode='rb').read(),
                           f'{get_volume_success_data}.png', allure.attachment_type.PNG)

    @pytest.mark.invalid_equivalence
    def test_create_hero_volume_fail(self, get_volume_fail_data):
        self.hero.create_hero("jinx", get_volume_fail_data, 20)
        res = self.hero.find_hero("jinx")
        assert res == False
        allure.attach.file(open(f'/results/{get_volume_fail_data}.png', mode='rb').read(),
                           f'{get_volume_fail_data}.png', allure.attachment_type.PNG)

    @pytest.mark.valid_equivalence
    def test_create_hero_name_success(self, get_name_success_data):
        """
        有效等价类
        :param get_volume_success_data:
        :return:
        """
        self.hero.create_hero(get_name_success_data, 20, 20)
        res = self.hero.find_hero(get_name_success_data)
        assert res.get("name", get_name_success_data)
        allure.attach.file(open(f'/results/{get_name_success_data}.png', mode='rb').read(),
                           f'{get_name_success_data}.png', allure.attachment_type.PNG)

    @pytest.mark.invalid_equivalence
    def test_create_hero_name_fail(self, get_name_fail_data):
        """
        有效等价类
        :param get_name_fail_data:
        :return:
        """
        self.hero.create_hero(get_name_fail_data, 20, 20)
        res = self.hero.find_hero(get_name_fail_data)
        assert res == False
        allure.attach.file(open(f'/results/{get_name_fail_data}.png', mode='rb').read(),
                           f'{get_name_fail_data}.png', allure.attachment_type.PNG)

    @pytest.mark.valid_equivalence
    def test_create_hero_power_success(self, get_power_success_data):
        """
        有效等价类
        :param get_volume_success_data:
        :return:
        """
        self.hero.create_hero("jinx", 20, get_power_success_data)
        res = self.hero.find_hero("jinx")
        assert res.get("name", get_power_success_data)
        allure.attach.file(open(f'/results/{get_power_success_data}.png', mode='rb').read(),
                           f'{get_power_success_data}.png', allure.attachment_type.PNG)

    @pytest.mark.invalid_equivalence
    def test_create_hero_power_fail(self, get_power_fail_data):
        """
        有效等价类
        :param get_name_fail_data:
        :return:
        """
        self.hero.create_hero("jinx", 20, get_power_fail_data)
        res = self.hero.find_hero("jinx")
        assert res == False
        allure.attach.file(open(f'/results/{get_power_fail_data}.png', mode='rb').read(),
                           f'{get_power_fail_data}.png', allure.attachment_type.PNG)
