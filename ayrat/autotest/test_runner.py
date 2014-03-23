class Runner(object):
    
    
    _pending_tests_list = []
    _ran_tests_list = []
    _passed_tests_list = []
    _failed_tests_list = []

    def __init__(self, test_class):
        self._test_class = test_class()
        for t in dir(self._test_class):
            if t.startswith('test'):
                self._pending_tests_list.append(t)
                print('pending_list: {}'.format(self._pending_tests_list))

    def add_test(self, test):
        self._pending_tests_list.append(test)

    def pending_tests(self):
        return [t for t in self._pending_tests_list]

    def run(self):
        print('pppending_list: {}'.format(self._pending_tests_list))
        for t in self._pending_tests_list:
            if t.startswith('test'):
                print(t)
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
        return [t for t in self._ran_tests_list]

    def passed_tests(self):
        return [t for t in self._passed_tests_list]

    def failed_tests(self):
        return [t for t in self._failed_tests_list]

    def clear_state(self):
        self._pending_tests_list = []
        self._ran_tests_list = []
        self._passed_tests_list = []
        self._failed_tests_list = []
