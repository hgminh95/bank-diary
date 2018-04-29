def expect_str(real, expect=None):
    if expect is not None and expect != real:
        raise Exception("expect '{}', found '{}'".format(expect, real))
