import inspect


class ConkerError(Exception):
    pass


def pre(condition):
    def decorated(function):
        names = inspect.getargspec(function).args

        def real(*args):
            parameters = list(zip(names, args))
            for k, v in parameters:
                locals()[k] = v

            try:
                exec(f"assert {condition}")
            except AssertionError:
                raise ConkerError()

            return function(*args)

        return real
    return decorated
