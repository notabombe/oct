import numpy as np
import numpy as np
import pytest
from ivy.functional.frontends.paddle.tensor.manipulation import moveaxis

@pytest.mark.parametrize("x, source, destination, expected", [
    (np.array([[1, 2, 3], [4, 5, 6]]), 0, 1, np.array([[1, 4], [2, 5], [3, 6]])),
    (np.array([[1, 2, 3], [4, 5, 6]]), 1, 0, np.array([[1, 4], [2, 5], [3, 6]])),
    (np.array([[1, 2, 3], [4, 5, 6]]), 0, 0, np.array([[1, 2, 3], [4, 5, 6]])),
])
def test_moveaxis(x, source, destination, expected):
    """
    Test the moveaxis function with different inputs.
    """
    assert np.array_equal(moveaxis(x, source, destination), expected)

