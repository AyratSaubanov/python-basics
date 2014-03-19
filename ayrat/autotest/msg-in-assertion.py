def assert_equal(a, b, msg = "{} must be equal to {}"):
    assert a==b, msg.format(a,b)


def assert_not_equal(a, b, msg='{} is equal to {}'):
    if a==b:
        raise AssertionError(msg.format(a,b))
    else:
        return True

#assert_equal(1,2)
print("________________")
assert_not_equal(1,1)
        