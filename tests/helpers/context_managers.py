from contextlib import contextmanager

import pytest


@contextmanager
def not_raises(exception=Exception):
    try:
        yield
    except exception:
        raise pytest.fail(f"DID RAISE {exception}")
