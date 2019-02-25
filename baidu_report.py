import unittest,HTMLTestRunner
from  baidu import  Baidu
if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Baidu))
    suite.addTest(Baidu('test_baidu'))
    #  定义生成测试报告的名称
    filename1 = "result.html"
    fp = open(filename1, 'wb')
    # 定义测试报告的路径，标题，描述等内容
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'自动化测试报告')
    runner.run(suite)