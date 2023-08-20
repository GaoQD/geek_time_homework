"""
============================
@description:TODO
@author:gaoqd
@time:2023/8/6  16:59
@version: 1.0
@file: ec.py
============================
"""
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.expected_conditions import _element_if_visible


def visibility_of_elements_located(*locators):
    """
    检查页面及元素是否存在
    :param locators:
    :return:
    """

    def _predicate(driver, locator):
        try:
            return _element_if_visible(driver.find_element(*locator))
        except StaleElementReferenceException:
            return False

    def multi_predicate(driver):
        for locator_ in locators:
            elem = _predicate(driver, locator_)
            if elem:
                return elem
        return False

    return multi_predicate
