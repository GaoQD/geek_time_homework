"""
============================
@description:TODO
@author:gaoqd
@time:2023/5/26  21:00
@version: 1.0
@file: hero_management.py
============================
"""
"""
每个操作封装成一个函数
创建英雄：当前游戏中，创建英雄角色，定义好对应英雄的血量及其攻击力。
查看英雄信息：查看当前游戏中所有的英雄信息。
修改英雄信息：修改英雄的血量。
删除英雄：英雄太弱，不需要，删除掉。
退出系统：结束程序
"""


class HeroManagement:

    def __init__(self):
        self.hero_list = []

    def update_hero(self, hero_name, hero_volume):
        """
        根据英雄名称修改英雄的血量
        :param hero_name: 英雄名称
        :param hero_volume: 英雄血量
        :return:
        """
        for i in self.hero_list:
            if i.get("name") == hero_name:
                i["volume"] = hero_volume
                return i
        return False

    def create_hero(self, hero_name, hero_volume, hero_power):
        """
        当前游戏中，创建英雄角色，定义好对应英雄的血量及其攻击力。
        :param hero_name:
        :param hero_volume:
        :param hero_power: 英雄攻击力
        :return:
        """
        if hero_volume <= 0 or hero_power >= 100:
            return False
        if hero_power <= 0:
            return False
        hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}
        self.hero_list.append(hero_info)
        return True

    def find_hero(self):
        """
        查看当前游戏中所有的英雄信息
        :param res:
        :return:
        """
        return self.hero_list

    def delete_hero(self, hero_name):
        """
        英雄太弱，不需要，删除掉
        :param hero_name:
        :return:
        """
        for i in self.hero_list:
            if hero_name == i['name']:
                self.hero_list.remove(i)
                return self.hero_list
        return False
