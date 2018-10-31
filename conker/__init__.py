class ConkerError(Exception):
    pass


def pre(s):
    def internal(f):
        def when_called(n):
            if n < 0:
                raise ConkerError()
            return f(n)
        return when_called
    return internal
