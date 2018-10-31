class ConkerError(Exception):
    pass


def pre(s):
    def internal(n):
        def when_called(n):
            raise ConkerError()
        return when_called
    return internal
