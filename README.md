This repository contains a minimal working example of a package implementing
a simple C library and a `ctypes` wrapper.
The package is built with the `meson-python` backend. 
You can find a simple demo script in `example/test.py`.

To use it, move to this repo folder from terminal and run:

1. `python3 -m venv .`
2. `pip install .`
3. `source bin/activate`
4. `python example/test.py`

If you are using anaconda:
1. `conda create -n meson-test python`
2. `conda activate meson-test`
3. `pip install .`
4. `python example/test.py`