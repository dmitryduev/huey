import datetime
import sys
import time
import imp
import os


class EmptyData(object):
    pass


def load_class(s):
    path, klass = s.rsplit('.', 1)
    if '/' not in path:
        __import__(path)
        mod = sys.modules[path]
    else:
        # import from anywhere:
        mod = imp.load_source(os.path.basename(path), '{:s}.py'.format(path))

    return getattr(mod, klass)


def wrap_exception(new_exc_class):
    exc_class, exc, tb = sys.exc_info()
    raise new_exc_class('%s: %s' % (exc_class.__name__, exc))

def local_to_utc(dt):
    return datetime.datetime(*time.gmtime(time.mktime(dt.timetuple()))[:6])
