import importlib
import sys
from warnings import warn

try:
    assert sys.version_info >= (3,0)
except AssertionError:
    warn('This tutorial is written for Python 3.  Legacy Python is not explicitly supported.')

required_modules = ['numpy', 'matplotlib', 'jupyter',
                    'numba', 'llvmlite', 'line_profiler', 'IPython',]
missing_modules = []
for mod in required_modules:
    try:
        importlib.import_module(mod)
    except ImportError:
        missing_modules.append(mod)

if missing_modules:
    print('The following modules are required but not installed:')
    print('    {}'.format(', '.join(missing_modules)))
    print('\nYou can install them using conda by running:')
    print('\n    conda install {}'.format(' '.join(missing_modules)))
    print('\nOr you can install them using pip by running:')
    print('\n    pip install {}'.format(' '.join(missing_modules)))
else:
    print('Everything looks good!')
