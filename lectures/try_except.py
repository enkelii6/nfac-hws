def example():
    try:
        ...  # code that we want to be completed, but it does not depend on us or smth

    except AssertionError as e:  # required if we use try construction
        ...  # code that will be completed if we catch specific error
        print(e)

    finally:  # optional
        ...  # code that will be completed in any way
