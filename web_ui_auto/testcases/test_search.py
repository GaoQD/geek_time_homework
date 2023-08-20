"""
============================
@description:TODO
@author:gaoqd
@time:2023/8/20  16:40
@version: 1.0
@file: test_search.py
============================
"""
import datetime

import pytest
import os
from page.main_page import MainPage
from utils.data_reader import DataReader
from utils.path import data_path
from page.enum_data import EmumData

data_path = os.path.join(data_path, 'search_data.json')
search_data = DataReader.load_json(data_path)


class TestSearch:

    def setup_class(self):
        self.main = MainPage()

    def setup(self):
        self.search = self.main.to_search_advance()

    def teardown_class(self):
        self.main.close()

    @pytest.mark.parametrize("keyword", search_data["keyword_fail"], ids=search_data["keyword_fail_ids"])
    def test_input_search_fail(self, keyword):
        result = self.search.input_search(keyword).click_search().get_result_fail()
        assert '找不到结果' in result or "您的搜索词过短" in result

    @pytest.mark.parametrize("keyword", search_data["keyword_success"], ids=search_data["keyword_success_ids"])
    def test_input_search_success(self, keyword):
        """
        测试输入关键字搜索
        :param keyword:
        :return:
        """
        search_type = EmumData.PostOrTopic()
        result_content_list = \
        self.search.input_search(keyword).click_search().get_search_result_success(search_type)[0]["content"]
        result_title = self.search.input_search(keyword).click_search().get_search_result_success(search_type)[0][
            "title"]
        assert keyword in result_content_list or result_title

    @pytest.mark.parametrize("keyword,search_type", search_data["topic_post_success"],
                             ids=search_data["topic_post_success_ids"])
    def test_select_topic_post_success(self, keyword, search_type):
        """
        选择话题/帖子
            步骤：1 先输入关键字
                 2 选择话题/帖子
        :return:
        """
        search_type_ = EmumData(search_type)

        assert keyword in str(self.search.input_search(keyword).click_search()
                              .get_search_result_success(search_type_)[0]["content"]).lower()

    @pytest.mark.parametrize("keyword,search_type", search_data["category_tag_success"],
                             ids=search_data["category_tag_success_ids"])
    def test_select_category_tag_success(self, keyword, search_type):
        """
        选择话题/帖子
            步骤：1 先输入关键字
                 2 选择分类或标签
        :return:
        """
        search_type_ = EmumData(search_type)

        category_tag_list = self.search.select_search_type(search_type_).input_search(
            keyword).click_search().get_search_result_success(search_type_)

        assert keyword in category_tag_list[0]

    @pytest.mark.parametrize("keyword,search_type", search_data["category_tag_fail"],
                             ids=search_data["category_tag_fail_ids"])
    def test_select_category_tag_fail(self, keyword, search_type):
        """
        选择话题/帖子
            步骤：1 先输入关键字
                 2 选择分类或标签
        :return:
        """
        search_type_ = EmumData(search_type)

        result = self.search.select_search_type(search_type_) \
            .input_search(keyword).click_search() \
            .get_result_fail()
        assert '找不到结果' in result or "搜索词过短" in result

    @pytest.mark.parametrize("keyword,search_type", search_data["user_success"], ids=search_data["user_success_ids"])
    def test_select_user_success(self, keyword, search_type):
        """
        选择用户
        :return:
        """
        search_type_ = EmumData(search_type)

        user_list = self.search.select_search_type(search_type_) \
            .input_search(keyword).click_search() \
            .get_search_result_success(search_type_)
        valid_names = []
        for name in user_list[0]:
            if keyword in name.lower():
                valid_names.append(name)
        assert valid_names

    @pytest.mark.parametrize("keyword,search_type", search_data["user_fail"], ids=search_data["user_fail_ids"])
    def test_select_user_fail(self, keyword, search_type):
        search_type_ = EmumData(search_type)

        result = self.search.select_search_type(search_type_) \
            .input_search(keyword).click_search() \
            .get_result_fail()
        assert '找不到结果' in result or "搜索词过短" in result

    @pytest.mark.parametrize("keyword,search_type,author_name", search_data["author_success"],
                             ids=search_data["author_success_ids"])
    def test_search_author_success(self, keyword, search_type, author_name):
        """
        高级筛选器---发帖人输入框
            步骤：1 先输入搜索关键字，
                 2 再选择搜索类型：话题/帖子
                 3 最后选择发帖人
        :return:
        """
        search_type_ = EmumData(search_type)
        post_list = self.search.input_search(keyword) \
            .select_search_type(search_type_) \
            .search_author(author_name).click_search().get_search_result_success(search_type_)
        assert post_list[0]["username"] == author_name

    @pytest.mark.parametrize("keyword", search_data["author_fail"], ids=search_data["author_fail_ids"])
    def test_search_author_fail(self, keyword):
        result = self.search.search_author_fail(keyword)
        assert "未找到匹配项" in result

    @pytest.mark.parametrize("keyword,search_type,data_name,datetime_input", search_data["search_date_success"],
                             ids=search_data["search_date_success_ids"])
    def test_search_date(self, keyword, search_type, data_name, datetime_input):
        """
        高级筛选器---发布时间
            步骤：1 先输入搜索关键字，
                 2 再选择搜索类型：话题/帖子
                 3 最后选择发帖人
        :param datetime_input: '2023/08/20'
        :return:
        """
        search_type_ = EmumData(search_type)

        data_name_ = EmumData(data_name)
        post_list = self.search.input_search(keyword) \
            .select_search_type(search_type_) \
            .select_post_date(data_name_, datetime_input).click_search().get_search_result_success(search_type_)[0][
            "data_time"]
        post_time = datetime.datetime.fromtimestamp(int(post_list[:-3])).date()
        date_pick_time = datetime.datetime.strptime(datetime_input, '%Y/%m/%d').date()
        if data_name_ == "晚于":
            assert post_time < date_pick_time
        elif data_name_ == "早于":
            assert post_time > date_pick_time

    @pytest.mark.parametrize("keyword,search_type,", search_data["only_title_success"],
                             ids=search_data["only_title_success_ids"])
    def test_select_only_title_success(self, keyword, search_type):
        search_type_ = EmumData(search_type)
        result = str(self.search.input_search(keyword).select_search_type(
            search_type_).select_only_title().click_search().get_search_result_success(search_type_)[0][
                         "title"]).lower()
        assert keyword in result

    @pytest.mark.parametrize("keyword,search_type,", search_data["only_title_fail"],
                             ids=search_data["only_title_fail_ids"])
    def test_select_only_title_fail(self, keyword, search_type):
        search_type_ = EmumData(search_type)
        result = self.search.input_search(keyword).select_search_type(
            search_type_).select_only_title().click_search().get_result_fail()
        assert '找不到结果' in result
