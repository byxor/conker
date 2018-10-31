import inspect


class ConkerError(Exception):
    pass


def pre(condition):
    def decorated(function):
        names = inspect.getargspec(function).args

        def real(*args):
            parameters = dict(zip(names, args))

            try:
                exec(f"assert {condition}", parameters)
            except AssertionError:
                raise ConkerError()

            return function(*args)

        return real
    return decorated
