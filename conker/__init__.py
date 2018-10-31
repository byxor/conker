import inspect


class ConkerError(Exception):
    pass


def pre(condition):
    def decorated(function):
        def when_called(*args):
            name = inspect.getargspec(function).args[0]

            def real(*args):
                locals()[name] = args[0]

                try:
                    exec(f"assert {condition}")
                except AssertionError:
                    raise ConkerError()

                return function(*args)

            return real(*args)
        return when_called
    return decorated
