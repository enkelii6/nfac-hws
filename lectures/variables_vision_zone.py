def outer():
    a = 10
    def inner():
        nonlocal a
        return a

    return inner()


a = 10


def example():
    global a
    a = a + 10
