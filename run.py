import ctypes
import os
import os.path
import sys
import time

curr_dir = os.path.dirname(__file__)
default_lib_path = os.path.join(curr_dir, "builds/lib.so.local")
lib_path = os.environ.get("RUNPY_LIB_PATH", default_lib_path)
lib = ctypes.cdll.LoadLibrary(lib_path)

lib.cNoop.argtypes = []
lib.cNoop.restype = ctypes.c_void_p

started = time.time()
for i in range(1000000):
    lib.cNoop()

took = time.time() - started
print(f'made {i + 1} calls in {took:.2f}s', file=sys.stderr)
