# Numba: Tell those C++ bullies to get lost

This is the repository for the Scipy 2017 tutorial. The tutorial will be
presented as a set of Jupyter notebooks with exercises sprinkled throughout.

1. [Installation](#installation-instructions)
2. [Optional extras](#optional-extras)
3. [Check your installation](#check-installation)


# Installation Instructions

We _strongly_, *strongly*, __strongly__ encourage you to use `conda` to install
the required packages for this tutorial.  There are non-Python dependencies
required that make manual installation or installing with `pip` very involved.

Note also that this tutorial is written for Python 3.6. Most things will still
work on Python 3.4+.

*No guarantees of any kind are made that it will be
compatible with Python 2.*

## Installing with `conda`

### Option a) Create a new environment
Download the `environment.yml` file in the root of this repository, e.g.

```console
wget https://raw.githubusercontent.com/gforsyth/numba_tutorial_scipy2017/master/environment.yml
```

and then create the environment with

```console
conda env create -f environment.yml
```

This will create a conda environment named `numbatutorial` with all of the required packages.

You can activate the environment with

```console
source activate numbatutorial
```
or on Windows:

```console
activate numbatutorial
```

### Option b) Install the required packages

```console
conda install jupyter ipython numpy numba line_profiler matplotlib
```

# Optional extras

No hands-on work requires these, but if you want to play with some of the
examples. If you installed using either `environments.yml` or `requirements.txt`
these are already installed.

```console
conda install cython
```

```console
pip install cython
```

We recommend you also install the Jupyter notebook extensions.

```console
pip install https://github.com/ipython-contrib/IPython-notebook-extensions/archive/master.zip --user
```

Once they are installed, start a notebook server

```console
jupyter notebook
```

and (assuming port 8888) navigate to `http://localhost:8888/nbextensions` where
you can choose which extensions to enable. One that is helpful (for us!) when
using Numba in the notebook is the `Skip-Traceback` extension. You're welcome to
enable whichever extensions you like (we're also fans of `Codefolding` and the
`Comment/Uncomment Hotkey`).

# Check Installation

Once you have downloaded all of the requires libraries/packages, you can run the
`check_install.py` script to confirm that everything is working as expected.
Either download the file directly or clone this repository and then run

```console
python check_install.py
```
