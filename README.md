# AWS stream utils

## Getting started

These instructions will get you to know how to run and test the application.

### Prerequisites

### Build and install the package

Go to the working directory /path/to/awsutils-library

- Create a binary distribution package which then can be installed with pip

`python setup.py bdist_wheel --universal`

- Install the package

`pip install dist/$PACKAGE_NAME.whl`

- After installation import the package

```
import awsutils
from awsutils import kinesis
```

## Running tests

Pytest is required to run tests locally. It is recommended to use Pipenv to install the dependencies as instructed below.

To run the unit tests locally use the following commands:

```
pipenv install pytest
pipenv run pytest -vv
```

## Usage

### Kinesis Utilities

#### Batcher

Creates optimum batches for sending data to the target Kinesis stream. This might be useful in an application that continuously reads large numbers of records from a data source and writes them to Kinesis data stream. The records are assumed to be strings of variable length. These records are passed through intact without messing up the order of the records.

Rebatch function takes in an array of records of variable size and splits the input into new batches of records `[ <var>, <var>, , <var>, ... ] -> [ [<var>, <var>, <var>,...], [...], [...], ... ]` suitably sized for delivery to a system which has adjustable thresholds or limits for

- maximum size of output record (default 1 MB) 
    - max_object_size=1000000
- maximum size of output batch (default 5 MB)
    - max_batch_size=5000000
- maximum number of records in an output batch (default 500)
    - max_objects_per_batch=500

A single record will be discarded if maximum size threshold is exceeded.

```
>>> from awsutils.kinesis import Batcher
>>> input = ["aa","bbb","cccc","ddddd"]
>>> Batcher(input, max_objects_per_batch=3).create()
[['aa', 'bbb', 'cccc'], ['ddddd']]
```

## Authors

- Hans Ahrenberg
