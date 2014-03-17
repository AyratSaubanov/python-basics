def assert_equal(a, b, msg = "{} must be equal to {}"):
    assert a==b, msg.format(a,b)


assert_equal(1,2)
assert_equal(1,2, "Assertion failed")
        