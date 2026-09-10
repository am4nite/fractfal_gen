import ctypes

module = ctypes.CDLL('./f.so')

# Define the function signature
module.iterate_point.argtypes = (
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_int
)
module.iterate_point.restype = ctypes.c_double

def iterate_point(X, Y, CX, CY, N):
    return module.iterate_point(X, Y, CX, CY, N)

"""
result = module.iterate_point(1.0, 0.0, 0.0, 1.0, 2)
print(result)
"""