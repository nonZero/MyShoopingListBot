# TDD: Test Driven Development

from mongo_storage import MongoStorage
from test_dict_storage import run_storage_tests


def test_add_itmes_and_list():
    storage = MongoStorage(is_test=True)

    run_storage_tests(storage)
