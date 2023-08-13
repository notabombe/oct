from ivy import moveaxis
from ivy.functional.frontends.paddle.func_wrapper import to_ivy_arrays_and_back

@to_ivy_arrays_and_back
def moveaxis(x, source, destination):
    """
    Move axes of an array to new positions.
    
    Parameters
    ----------
    x : paddle.Tensor
        The input array.
    source : int or sequence of int
        Original positions of the axes to move. These must be unique.
    destination : int or sequence of int
        Destination positions for each of the original axes. These must also be unique.
        
    Returns
    -------
    result : paddle.Tensor
        Array with moved axes. This array is a view of the input array.
    """
    retur

