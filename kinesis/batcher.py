"""
 Kinesis Batcher
 Description: Creates optimum batches for sending data to the target service.
 Author: Hans Ahrenberg
"""
from typing import Generator

def generate_batches(array_to_split: list, max_object_size: int,
                     max_batch_size: int, max_objects_per_batch: int) -> Generator[str, None, None]:
    """
    Generates batches from an array of string objects by retaining the original values
    intact and preserving the order of the objects. The maximum size of a single string
    object is set according to max_object_size and larger records are discarded. Batch
    sizes can be configured based on the max_batch_size and max_objects_per_batch
    threshold limits. The number of objects in a single batch is limited based on
    the max_objects_per_batch.

    :param array_to_split: array of string objects to split into batches
    :param max_object_size: maximum size of an object in bytes
    :param max_batch_size: maximum size of a single batch in bytes
    :param max_objects_per_batch: maximum number of objects in a single batch
    :returns: a generator object representing batches
    """
    batch = []
    batch_size = 0
    for item in array_to_split:
        record_size = len(item)

        # Larger objects than 'max_object_size' are discarded.
        if record_size <= max_object_size:
            # A batch size cannot grow over the 'max_batch_size' limit.
            # If it does, the object is handled over to the next batch.
            if batch_size + record_size <= max_batch_size:
                batch.append(item)
                batch_size += record_size
            else:
                yield batch
                batch = []
                batch_size = 0
                batch.append(item)
                batch_size += record_size

        # If batch has become full generate a batch.
        if len(batch) == max_objects_per_batch:
            yield batch
            batch = []
            batch_size = 0

    # Generate batch for left over items.
    if batch:
        yield batch

def rebatch(input_array: list, max_object_size: int = 1000000,
            max_batch_size: int = 5000000, max_objects_per_batch: int = 500) -> list:
    """
    Rebatches an array of string objects using a batch generator.

    :param input_array: a list of string objects
    :returns: a list of batches where each batch is an array of records
    """
    output_array = []

    for batch in generate_batches(input_array, max_object_size,
                                  max_batch_size, max_objects_per_batch):
        output_array.append(batch)

    return output_array
