#!/usr/bin/env python

from distutils.core import setup
from main import cc

def main():
    """The main entry point."""
    skw = dict(
        name='ppe',
        license='MIT',
        ext_modules=[cc.distutils_extension()],
        )
    setup(**skw)


if __name__ == '__main__':
    main()
