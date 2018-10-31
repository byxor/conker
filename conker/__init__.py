class ConkerError(Exception):
    pass


def pre(condition):
    def decorated(function):
        def when_called(arg):
            locals()["name"] = arg
            locals()["n"] = arg
            code = f"if not ({condition}):\n    raise ConkerError()"
            exec(code)
            return function(arg)
        return when_called
    return decorated
