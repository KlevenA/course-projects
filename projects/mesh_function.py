import numpy as np
from collections.abc import Callable


def mesh_function(f: Callable[[float], float], t: float) -> np.ndarray:
    f_mesh = np.zeros(len(t)) # initializing f_mesh
    t_mesh = np.linspace(0,t) # initialize t-mesh
    for n in range (len(t_mesh)):
        f_mesh(n) = f(n)
    return f_mesh


def func(t: float) -> float:
    if t >= 0 and t <= 3:
        return np.exp(-t)
    elif t > 3 and t <= 4:
        return np.exp(-3*t)
   else 
        raise  RuntimeError("Outside of function range, t = {t}")

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)

if __name__ == "__main__":
    test_mesh_function()
