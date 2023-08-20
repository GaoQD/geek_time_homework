"""
============================
@description:TODO
@author:gaoqd
@time:2023/8/6  16:39
@version: 1.0
@file: search_page.py
============================
"""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.base_page import BasePage
from page.enum_data import EmumData
from utils.ec import visibility_of_elements_located


class SearchPage(BasePage):

    def __init__(self, driver: WebDriver = None):
        super().__init__(driver)

    def get_result_fail(self):
        search_result_loc = (By.CSS_SELECTOR, '.search-results')
        search_notice_loc = (By.CSS_SELECTOR, '.fps-invalid')
        WebDriverWait(self.driver, 5).until(visibility_of_elements_located(search_result_loc, search_notice_loc))
        try:
            search_result_ele = self.driver.find_element(*search_result_loc)
            result = search_result_ele.find_element(By.TAG_NAME, 'h3').text
        # except Exception:
        except NoSuchElementException:
            search_notice_ele = self.driver.find_element(*search_notice_loc)
            result = search_notice_ele.text
        return result

    def input_search(self, keyword):
        query = self.find_element(By.CSS_SELECTOR, "input.search-query")
        query.clear()
        query.send_keys(keyword)
        return self

    def click_search(self):
        self.click(By.CSS_SELECTOR, '.search-bar .search-cta')
        return self

    def get_search_result_success(self, search_type) -> list:
        loc_result = (By.CSS_SELECTOR, ".search-results")
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(loc_result))
        search_result = self.driver.find_element(*loc_result)

        if search_type == EmumData.PostOrTopic:
            post_list = []
            content_list = []
            for element in search_result.find_elements(By.CSS_SELECTOR, '.fps-result-entries .fps-result'):
                title = element.find_element(By.CSS_SELECTOR, '.topic-title').text
                username = element.find_element(By.CSS_SELECTOR, '.author .avatar').get_attribute("title")
                data_time = element.find_element(By.CSS_SELECTOR, '.relative-date').get_attribute("data-time")
                for content_ele in element.find_elements(By.CSS_SELECTOR, '.ember-view .search-highlight'):
                    content_list.append(content_ele.text)
                post_list.append(
                    {"title": title, "username": username, "data_time": data_time, "content": content_list})
            return post_list
        elif search_type == EmumData.CategoryOrTag:
            category_items = search_result.find_elements(By.CSS_SELECTOR, '.category-items .category-name')
            tag_items = search_result.find_elements(By.CSS_SELECTOR, '.tag-items .tag-name')
            # 列表推导式
            return [ele.text for ele in category_items + tag_items]
        elif search_type == EmumData.User:
            user_titles = search_result.find_elements(By.CSS_SELECTOR, '.user-items .user-titles')
            # 结构: [[name, username]]
            users = []
            for user_title in user_titles:
                names = []
                try:
                    name = user_title.find_element(By.CSS_SELECTOR, '.name')
                    names.append(name.text)
                except NoSuchElementException:
                    pass
                username = user_title.find_element(By.CSS_SELECTOR, '.username')
                names.append(username.text)
                users.append(names)
            return users
        else:
            return

    def select_search_type(self, search_type):
        self.click(By.CSS_SELECTOR, '.search-bar .select-kit')
        select_options = self.driver.find_elements(By.CSS_SELECTOR,
                                                   '.search-bar .select-kit-body .select-kit-row')
        for option in select_options:

            if option.find_element(By.CSS_SELECTOR, '.name').text == search_type.value:
                option.click()
                return self
        raise Exception('search_type输入错误')

    def switch_search_filter(self, action):
        """
        打开或关闭高级筛选器
        :param action:
        :return:
        """
        advanced_filter_ele = self.driver.find_element(By.CSS_SELECTOR, '.search-filters .advanced-filters')
        open_status = advanced_filter_ele.get_attribute("open")
        if action == EmumData.Open and not open_status:
            advanced_filter_ele.click()
        elif action == EmumData.Close and open_status:
            advanced_filter_ele.click()
        return self

    def search_author(self, author_name):
        """
        先点击发帖人搜索框，输入关键字，选择发帖人
        :param author_name:
        :return:
        """
        self.switch_search_filter(EmumData.Open)
        author_chooser_ele = self.driver.find_element(By.CSS_SELECTOR, '.advanced-search-posted-by .user-chooser')
        self.click(By.CSS_SELECTOR, '.advanced-search-posted-by .user-chooser')
        author_chooser_ele.find_element(By.CSS_SELECTOR, '.filter-input').send_keys(author_name)
        author_collection_loc = (By.CSS_SELECTOR, ".select-kit-body .select-kit-collection")
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(author_collection_loc))

        author_rows_elems = author_chooser_ele.find_elements(By.CSS_SELECTOR, ".select-kit-collection .select-kit-row")
        # 先不处理找不到发帖人情况
        for author_name_ele in author_rows_elems:
            if author_name_ele.find_element(By.CSS_SELECTOR, '.username').text == author_name:
                author_name_ele.click()
                return self

    def search_author_fail(self, author_name):
        """
        先点击发帖人搜索框，输入关键字，选择发帖人
        :param author_name:
        :return:
        """
        self.switch_search_filter(EmumData.Open)
        author_chooser_ele = self.driver.find_element(By.CSS_SELECTOR, '.advanced-search-posted-by .user-chooser')
        author_chooser_ele.click()
        self.click(By.CSS_SELECTOR, '.advanced-search-posted-by .user-chooser')
        author_chooser_ele.find_element(By.NAME, 'filter-input-search').send_keys(author_name)
        result_loc = (By.CSS_SELECTOR, '.no-content')
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(result_loc))
        author_chooser_result = author_chooser_ele.find_element(*result_loc).text
        return author_chooser_result

    def select_post_date(self, data_name, datetime_input):
        """
        选择发布时间
        :param data_name:
        :param datetime_input:
        :return:
        """
        self.switch_search_filter(EmumData.Open)
        date_ele = self.driver.find_element(By.CSS_SELECTOR, '.d-date-input .date-picker')
        if data_name == EmumData.Early:
            date_ele.send_keys(datetime_input)
        elif data_name == EmumData.Later:
            # self.driver.find_element(By.CSS_SELECTOR, '.advanced-search-posted-date #postTime').click()
            self.click(By.CSS_SELECTOR, '.advanced-search-posted-date #postTime')
            # self.driver.find_element(By.CSS_SELECTOR, "li[data-value='after']").click()
            self.click(By.CSS_SELECTOR, "li[data-value='after']")
            date_ele.send_keys(datetime_input)
        return self

    def select_only_title(self):
        self.switch_search_filter(EmumData.Open)
        self.click(By.ID, 'matching-title-only')
        return self
