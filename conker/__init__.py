import inspect


class ConkerError(Exception):
    pass


def pre(condition):
    def decorated(function):
        def when_called(arg):
            name = inspect.getargspec(function).args[0]

            def real(arg):
                locals()[name] = arg

                try:
                    exec(f"assert {condition}")
                except AssertionError:
                    raise ConkerError()

                return function(arg)

            return real(arg)
        return when_called
    return decorated
