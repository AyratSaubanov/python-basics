from practice_2.ayrat_assertions import assert_equal

pending_tests_list = []
ran_tests_list = []
passed_tests_list = []
failed_tests_list = []


def add_test(fn):
    pending_tests_list.append(fn)

    
def pending_tests():
    return [t.__name__ for t in pending_tests_list]


def run():
    for t in pending_tests_list:
        try:
            t()
        except:
            failed_tests_list.append(t)
        else:
            passed_tests_list.append(t)
        finally:
            pending_tests_list.remove(t)
            ran_tests_list.append(t)
    return (len(ran_tests_list), len(passed_tests_list), len(failed_tests_list))


def ran_tests():
    return [t.__name__ for t in ran_tests_list]


def passed_tests():
    return [t.__name__ for t in passed_tests_list]


def failed_tests():
    return [t.__name__ for t in failed_tests_list]


def one_is_equal_1_test():
    assert_equal(1, 2)

add_test(one_is_equal_1_test)
print(run())