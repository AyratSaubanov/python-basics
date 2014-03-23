from ayrat.autotest.assertions import *

class TestClass(object):
    
    def __init__(self):
        pass
        
    def set_up(self):
        print("This is the \'set_up\' function.")
    
    def tear_down(self):
        print("This is the \'tear_down\' function.")
        
    def test_1_is_equal_1(self):
        assert_equal(1, 1)


    def test_1_is_equal_2(self):
        assert_equal(1, 2)