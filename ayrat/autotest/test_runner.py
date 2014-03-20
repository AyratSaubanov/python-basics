class Runner(object):

    def __init__(self):
        self._pending_tests_list = []
        self._ran_tests_list = []
        self._passed_tests_list = []
        self._failed_tests_list = []

    def add_test(self, fn):
        self._pending_tests_list.append(fn)

    def pending_tests(self):
        return [t.__name__ for t in self._pending_tests_list]

    def run(self):
        for t in self._pending_tests_list:
            try:
                t()
            except:
                self._failed_tests_list.append(t)
            else:
                self._passed_tests_list.append(t)
            finally:
                self._pending_tests_list.remove(t)
                self._ran_tests_list.append(t)
        return (len(self._ran_tests_list), len(self._passed_tests_list), len(self._failed_tests_list))

    def ran_tests(self):
        return [t.__name__ for t in self._ran_tests_list]

    def passed_tests(self):
        return [t.__name__ for t in self._passed_tests_list]

    def failed_tests(self):
        return [t.__name__ for t in self._failed_tests_list]

    def clear_state(self):
        self._pending_tests_list = []
        self._ran_tests_list = []
        self._passed_tests_list = []
        self._failed_tests_list = []
