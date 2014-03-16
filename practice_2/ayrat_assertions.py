def assert_equal(a, b):
    if a!=b:
        raise AssertionError('{} is not equal to {}'.format(a,b))
    else:
#        print('\'assert_equal\' passed. {} is equal to {}'.format(a,b))
        return True
    


result = False
x, y = 1, 2
try:
    result = assert_equal(x,y)
except AssertionError as e:
    print('Exception received during test \'assert_equal({}, {})\': {}'.format(x,y,e.message))
finally:
    print('\'assert_equal\' result: %r' %result)
    