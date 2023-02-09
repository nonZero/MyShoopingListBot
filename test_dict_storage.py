# TDD: Test Driven Development

from dict_storage import DictStorage


def test_add_itmes_and_list():
    storage = DictStorage()

    storage.add_item_for_chat("123x", "milk")
    storage.add_item_for_chat("123x", "cookies")
    storage.add_item_for_chat("123x", "coffee")
    storage.add_item_for_chat("456", "apples")

    assert storage.list_items_for_chat("123x") == ["milk", "cookies", "coffee"]
    assert storage.list_items_for_chat("456") == ["apples"]
