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

### Kinesis Library

#### Batcher

Creates optimum batches for sending data to the target Kinesis stream. This might be useful in an application that continuously reads large numbers of records from a data source and writes them to Kinesis data stream. The records are assumed to be strings of variable length. These records are passed through intact without messing up the order of the records.

Rebatch function takes in an array of records of variable size and splits the input to batches of records (array of arrays) suitably sized for delivery to a system which has adjustable thresholds or limits for

- maximum size of output record (default 1 MB), larger records should be discarded
- maximum size of output batch (default 5 MB)
- maximum number of records in an output batch (default 500)

Example.
```
# input_array = [<str>, <str>, , <str>,... ]
# output_array = [[<str>,<str>,<str>,...], [...], [...],... ]
output_array = rebatch(input_array)
```

## Authors

- Hans Ahrenberg