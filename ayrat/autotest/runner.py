_pending_tests_list = []
_ran_tests_list = []
_passed_tests_list = []
_failed_tests_list = []


def add_test(fn):
    _pending_tests_list.append(fn)


def pending_tests():
    return [t.__name__ for t in _pending_tests_list]


def run():
    for t in _pending_tests_list:
        try:
            t()
        except:
            _failed_tests_list.append(t)
        else:
            _passed_tests_list.append(t)
        finally:
            _pending_tests_list.remove(t)
            _ran_tests_list.append(t)
    return (len(_ran_tests_list), len(_passed_tests_list), len(_failed_tests_list))


def ran_tests():
    return [t.__name__ for t in _ran_tests_list]


def passed_tests():
    return [t.__name__ for t in _passed_tests_list]


def failed_tests():
    return [t.__name__ for t in _failed_tests_list]


def clear_state():
    _pending_tests_list = []
    _ran_tests_list = []
    _passed_tests_list = []
    _failed_tests_list = []
