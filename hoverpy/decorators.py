from .hp import HoverPy

class capture(object):

    def __init__(self, dbpath="requests.db", capture=True, **kwargs):
        self.dbpath = dbpath
        self.capture = capture
        self.kwargs = kwargs

    def __call__(self, f):
        def wrapped_f(*args):
            with HoverPy(capture=self.capture, dbpath=self.dbpath, **self.kwargs):
                return f(*args)
        return wrapped_f

class simulate(object):

    def __init__(self, dbpath="requests.db", capture=False, **kwargs):
        self.dbpath = dbpath
        self.capture = capture
        self.kwargs = kwargs

    def __call__(self, f):
        def wrapped_f(*args):
            with HoverPy(capture=self.capture, dbpath=self.dbpath, **self.kwargs):
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

