import logging
from typing import Generator


class Batcher:
    """
    Rebatch a list of events and optimizes batch size for sending data to the target Kinesis stream.
    """
    def __init__(self, input_array=None, max_object_size=1000000, max_batch_size=5000000, max_objects_per_batch=500, logger=None):
        self.init_logging(logger)
        self.input_array = input_array
        self.max_object_size = max_object_size
        self.max_batch_size = max_batch_size
        self.max_objects_per_batch = max_objects_per_batch

    def init_logging(self, logger):
        if not logger:
            logger = logging.getLogger(__name__)
        self.logger = logger

    @staticmethod
    def batch_generator(array_to_split: list, max_object_size: int,
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

    def rebatch(self):
        """
        Rebatches an array of string objects using a batch generator.

        :param input_array: a list of string objects
        :returns: a list of batches where each batch is an array of records
        """
        output_array = []

        for batch in self.batch_generator(self.input_array, self.max_object_size,
                                    self.max_batch_size, self.max_objects_per_batch):
            output_array.append(batch)

        return output_array
