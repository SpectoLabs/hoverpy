from .hp import HoverPy

class capture(object):

    def __init__(self, dbpath="requests.db", **kwargs):
        self.arg1 = dbpath
        self.kwargs = kwargs

    def __call__(self, f):
        def wrapped_f(*args):
            with HoverPy(capture=True, dbpath=self.arg1, **self.kwargs):
                return f(*args)
        return wrapped_f

class simulate(object):

    def __init__(self, dbpath="requests.db", **kwargs):
        self.arg1 = dbpath
        self.kwargs = kwargs

    def __call__(self, f):
        def wrapped_f(*args):
            with HoverPy(capture=False, dbpath=self.arg1, **self.kwargs):
                return f(*args)
        return wrapped_f


class modify(object):

    def __init__(self, middleware, **kwargs):
        self.middleware = middleware
        self.kwargs = kwargs

    def __call__(self, f):
        def wrapped_f(*args):
            with HoverPy(modify=True, middleware=self.middleware, **self.kwargs):
                return f(*args)
        return wrapped_f