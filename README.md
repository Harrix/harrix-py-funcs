# harrix-pylib

Common functions for working in Python.

![GitHub](https://img.shields.io/github/license/Harrix/harrix-pylib) ![PyPI](https://img.shields.io/pypi/v/harrix-pylib)

## Quick start

```py
import harrixpylib as h

h.clear_directory("C:/temp_dir")
```

## Install

Pip:

```console
pip install harrix-pylib
```

Pipenv:

```console
pip update harrix-pylib
```

## Update

Pip:

```console
pipenv install harrix-pylib
```

Pipenv:

```console
pipenv update harrix-pylib
```

## Development

If you don't have [pipenv](https://pipenv.pypa.io/en/latest/) installed, then you can install it via the commands:

```console
python -m pip install virtualenv
python -m pip install pipenv
```

Installing packages by file `Pipfile`:

```console
pipenv install --dev
pipenv shell
```

Generate docs:

```console
pdoc --docformat="google" src\harrixpylib\
```

Example of installing a package under development in a test project:

```console
pipenv install -e C:/GitHub/harrix-pylib
```
