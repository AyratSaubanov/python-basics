from ayrat.autotest.test_runner import Runner
from ayrat import autotest

def one_is_equal_1_test():
    autotest.assert_equal(1, 1)


def one_is_equal_2_test():
    autotest.assert_equal(1, 2)

testRunner = Runner()
testRunner.add_test(one_is_equal_1_test)
testRunner.add_test(one_is_equal_2_test)

print(testRunner.run())
