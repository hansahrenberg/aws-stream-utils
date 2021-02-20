# AWS utils library

## Getting started

These instructions will get you to know how to run and test the application.

### Prerequisites

### Build locally from source

Go to the working directory /path/to/kinesis-batcher-library

Run `python setup.py bdist_wheel`

then install the library by using `pip install /path/to/wheelfile.whl`

Once you have installed the library, you can import it using, e.g.:

```
import kinesis
from kinesis import batcher
```

## Running tests

Pytest is required to run tests locally. It is recommended to use Pipenv to install the dependencies as instructed below.

To run the unit tests locally use the following commands:

```
pipenv install pytest
pipenv run pytest -vv
```

## Usage

## Authors

- Hans Ahrenberg