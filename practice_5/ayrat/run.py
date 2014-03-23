from ayrat.autotest import Runner
from ayrat.autotest import TestClass
# from ayrat import autotest

# def one_is_equal_1_test():
#     autotest.assert_equal(1, 1)
# 
# 
# def one_is_equal_2_test():
#     autotest.assert_equal(1, 2)

# testRunner = Runner()
# testRunner.add_test(one_is_equal_1_test)
# testRunner.add_test(one_is_equal_2_test)
# 
# print(testRunner.run())

runner = Runner(TestClass)
print(runner.run())
print(runner.pending_tests())