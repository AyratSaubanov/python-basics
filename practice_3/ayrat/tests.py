from practice_2 import ayrat_assertions
import test_runner

def one_is_equal_1_test():
    ayrat_assertions.assert_equal(1, 2)

test_runner.add_test(one_is_equal_1_test)
print(test_runner.run())