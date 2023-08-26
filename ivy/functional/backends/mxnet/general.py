import mxnet as mx
from typing import Union, Optional, Tuple
import numpy as np

from ivy.utils.exceptions import IvyNotImplementedException


def current_backend_str() -> str:
    return "mxnet"


def is_native_array(
    x: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    exclusive: bool = False,
) -> bool:
    if exclusive:
        return isinstance(x, mx.ndarray.NDArray)
    else:
        return isinstance(x, (mx.ndarray.NDArray, np.ndarray))


def to_numpy(x: mx.ndarray.NDArray, /, *, copy: bool = True) -> np.ndarray:
    if not copy:
        return x.asnumpy()
    return x.asnumpy() if x.shape == () else x.copy().asnumpy()


def itemsize(x: mx.ndarray.NDArray, /) -> int:
    return x.asnumpy().itemsize


def strides(x: mx.ndarray.NDArray, /) -> Tuple[int]:
    return x.asnumpy().strides


def container_types():
    return []


def gather(
    x: mx.ndarray.NDArray,
    indices: mx.ndarray.NDArray,
    /,
    *,
    axis: int = -1,
    batch_dims: int = 0,
    out: Optional[mx.ndarray.NDArray] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()
