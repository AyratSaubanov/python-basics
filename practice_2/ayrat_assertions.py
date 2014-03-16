def assert_equal(a, b):
    if a!=b:
        raise AssertionError('{} is not equal to {}'.format(a,b))
    else:
        return True
    
def assert_not_equal(a, b):
    if a==b:
        raise AssertionError('{} is equal to {}'.format(a,b))
    else:
        return True

def assert_true(a):
    if a!=True:
        raise AssertionError('{} is not True'.format(a))
    else:
        return True
    
def assert_false(a):
    if a!=False:
        raise AssertionError('{} is not False'.format(a))
    else:
        return True

def assert_is(a,b):
    if a is not b:
        raise AssertionError('{} is not {}'.format(a,b))
    else:
        return True
    
def assert_is_not(a,b):
    if a is b:
        raise AssertionError('{} is {}'.format(a,b))
    else:
        return True

def assert_is_none(a):
    if a is not None:
        raise AssertionError('{} is not None'.format(a))
    else:
        return True

def assert_is_not_none(a):
    if a is None:
        raise AssertionError('{} is None'.format(a))
    else:
        return True

def assert_in(a,b):
    if a not in b:
        raise AssertionError('{} not in {}'.format(a,b))
    else:
        return True

def assert_not_in(a,b):
    if a in b:
        raise AssertionError('{} in {}'.format(a,b))
    else:
        return True


result = False
x, y = 1, 1
try:
    result = assert_equal(x,y)
except AssertionError as e:
    print('Exception received during test \'assert_equal({}, {})\': {}'.format(x,y,e.message))
finally:
    print('\'assert_equal({}, {})\' result: {}'.format(x,y,result))
print('_________________')
result = False
x, y = 1, 2
try:
    result = assert_equal(x,y)
except AssertionError as e:
    print('Exception received during test \'assert_equal({}, {})\': {}'.format(x,y,e.message))
finally:
    print('\'assert_equal({}, {})\' result: {}'.format(x,y,result))
print('_________________')
result = False
x, y = 1, 1
try:
    result = assert_not_equal(x,y)
except AssertionError as e:
    print('Exception received during test \'assert_not_equal({}, {})\': {}'.format(x,y,e.message))
finally:
    print('\'assert_not_equal({}, {})\' result: {}'.format(x,y,result))
print('_________________')
result = False
x, y = 1, 2
try:
    result = assert_not_equal(x,y)
except AssertionError as e:
    print('Exception received during test \'assert_not_equal({}, {})\': {}'.format(x,y,e.message))
finally:
    print('\'assert_not_equal({}, {})\' result: {}'.format(x,y,result))
print('_________________')
result = False
x = True
try:
    result = assert_true(x)
except AssertionError as e:
    print('Exception received during test \'assert_true({})\': {}'.format(x,e.message))
finally:
    print('\'assert_true({})\' result: {}'.format(x, result))
print('_________________')
result = False
x = False
try:
    result = assert_true(x)
except AssertionError as e:
    print('Exception received during test \'assert_true({})\': {}'.format(x,e.message))
finally:
    print('\'assert_true({})\' result: {}'.format(x, result))
print('_________________')
result = False
x = False
try:
    result = assert_true(x)
except AssertionError as e:
    print('Exception received during test \'assert_true({})\': {}'.format(x,e.message))
finally:
    print('\'assert_true({})\' result: {}'.format(x, result))
print('_________________')
