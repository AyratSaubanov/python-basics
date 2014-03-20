#from ayrat.autotest.assertions import *
#from ayrat.autotest.runner import *

from ayrat import autotest


def one_is_equal_1_test():
    autotest.assert_equal(1, 1)


def one_is_equal_2_test():
    autotest.assert_equal(1, 2)

if __name__ == '__main__':
    autotest.add_test(one_is_equal_1_test)
    autotest.add_test(one_is_equal_2_test)
    print(autotest.run())
