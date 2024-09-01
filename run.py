import ctypes
import os.path
import sys
import time

try:
    count = int(sys.argv[1])
except IndexError:
    count = 1000000

curr_dir = os.path.dirname(__file__)
lib = ctypes.cdll.LoadLibrary(os.path.join(curr_dir, "lib.so"))

lib.cNoop.argtypes = []
lib.cNoop.restype = ctypes.c_void_p

started = time.time()
for i in range(count):
    lib.cNoop()

took = time.time() - started
print(f'made {i + 1} calls in {took:.2f}s', file=sys.stderr)
