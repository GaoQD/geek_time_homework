"""
============================
@description:TODO
@author:gaoqd
@time:2023/5/26  21:33
@version: 1.0
@file: test_hero_management.py
============================
"""
from python_programming_practice1.hero_management import HeroManagement

print("""
    1. **创建英雄**
    2. **查看英雄信息**
    3. **修改英雄信息**
    4. **删除英雄**
    5. **退出系统**
""")

hero_management = HeroManagement()

while True:
    res = input("请输入对应的值，执行对应的操作：")
    if res == "1":
        hero_name = input("请输入英雄的名称：")
        hero_volume = int(input("请输入英雄的血量："))
        hero_power = int(input("请输入英雄的攻击力："))
        print(f"创建成功！英雄名称为{hero_name} ，英雄的血量为{hero_volume} ，英雄的攻击力为{hero_power}")
        hero_management.create_hero(hero_name, hero_volume, hero_power)
    elif res == "2":
        print(f'查询成功！英雄信息为{hero_management.find_hero()}')
    elif res == "3":
        hero_name = input("请输入英雄的名称：")
        hero_volume = input("请输入英雄的血量：")
        hero_management.update_hero(hero_name, hero_volume)
        print(f"修改成功，英雄名称为{hero_name}, 修改后英雄的血量为{hero_volume}")
    elif res == "4":
        res = input("请输入需要删除的英雄信息：")
        hero_management.delete_hero(res)
        print(f"英雄太弱，不需要，已将英雄名称为{res}删除成功")
    elif res == "5":
        print(f"退出系统")
        break
