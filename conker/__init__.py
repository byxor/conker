import inspect


class ConkerError(Exception):
    pass


def pre(*conditions):
    def decorator(function):
        names = inspect.getargspec(function).args

        def decorated(*args):
            parameters = dict(zip(names, args))

            try:
                for condition in conditions:
                    exec(f"assert {condition}", parameters)
            except AssertionError:
                raise ConkerError()

            return function(*args)

        return decorated
    return decorator
