import inspect


class ConkerError(Exception):
    pass


def pre(*conditions):
    def decorator(function):
        arg_spec = inspect.getargspec(function)
        arg_names = arg_spec.args

        def decorated(*args, **kwargs):
            arg_values = args
            if arg_spec.defaults:
                arg_values += arg_spec.defaults

            parameters = dict(zip(arg_names, arg_values))
            parameters.update(kwargs)

            print(parameters)

            try:
                for condition in conditions:
                    exec(f"assert {condition}", parameters)
            except AssertionError:
                raise ConkerError()

            return function(*args)

        return decorated
    return decorator
