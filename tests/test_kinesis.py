import random
import string
import pytest
from awsutils.kinesis import Batcher 


test_data = [
    ''.join(random.choice(string.ascii_lowercase)
            for _ in range(random.randint(1, 10))) for _ in range(520)
    ]

test_data_with_oversized_records = test_data + \
        [''.join(random.choices(string.ascii_lowercase, k=2000000))] + \
        [''.join(random.choices(string.ascii_lowercase, k=1000001))] + \
        [''.join(random.choices(string.ascii_lowercase, k=1000000))] + \
        [''.join(random.choices(string.ascii_lowercase, k=900000))]

test_data_with_oversized_batches = test_data + \
        [''.join(random.choices(string.ascii_lowercase, k=2000000))] + \
        [''.join(random.choices(string.ascii_lowercase, k=1000000))] + \
        [''.join(random.choices(string.ascii_lowercase, k=1000000))] + \
        [''.join(random.choices(string.ascii_lowercase, k=1000000))] + \
        [''.join(random.choices(string.ascii_lowercase, k=1000000))] + \
        [''.join(random.choices(string.ascii_lowercase, k=1000000))] + \
        [''.join(random.choices(string.ascii_lowercase, k=1000000))]

@pytest.mark.parametrize("test_data, expected_output", [
    (test_data, [500, 20]),
    (test_data_with_oversized_records, [500, 22]),
    (test_data_with_oversized_batches, [500, 24, 2])
    ])
def test_batching_constraints(test_data, expected_output):
    """
    Test that batching constraints are satisfied.
    1) Each batch must not contain more than 500 records
    2) Records greater than 1 MB in size are discarded
    3) Single batch must not be greater than 5 MB in size
    """
    array_lengths = []
    for i in Batcher(test_data).rebatch():
        array_lengths.append(len(i))

    assert array_lengths == expected_output

def test_record_similarity_and_ordering(test_data=test_data):
    """
    Test that strings remain unchanged and are ordered similarly
    both in input array and output array(s).
    """
    first_index = 0
    for i in Batcher(test_data).rebatch():
        assert i == test_data[first_index:first_index+len(i)]
        first_index += len(i)
