# -*-coding:utf8-*-
# @auth 小哥哥
# @time 2020/8/24 10:02
from common.globals import g
from common.log import logger
from common.utility import parse, Excel
from sktest.testcase import TestCase


class TestSuit:

    def __init__(self, test_suit):
        # self.work_book = Excel(file_path)
        # self.test_suit = self.work_book.read('case')
        # self.elements_file = file_path
        pass
        self.test_suit = test_suit

    def run(self):
        for test_case in self.test_suit:
            try:
                parse(test_case)
                logger.info("**** 解析用例成功 ****")
            except:
                logger.exception("用例解释失败")
            else:
                try:
                    logger.info("-------- Run The TestCase：%s %s" % (test_case['id'], test_case['title']))
                    tc = TestCase(test_case)
                    tc.run()
                except:
                    logger.exception(f'用例{test_case["id"]}:{test_case["title"]}执行失败')
                else:
                    logger.info("****  用例执行完成  ****")
        # print(g.result) TODO 将用例执行结果写入excel

        g.driver.quit()
