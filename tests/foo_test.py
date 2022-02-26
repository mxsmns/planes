from hypothesis import given
from hypothesis.strategies import integers

from planes import foo


@given(integers(), integers())
def test_add(x, y):
    assert foo.add(x, y) == x + y
