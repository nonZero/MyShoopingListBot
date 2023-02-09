# TDD: Test Driven Development

from dict_storage import add_item_for_chat, DB, list_items_for_chat


def test_add_itmes_and_list():
    add_item_for_chat("123x", "milk")
    add_item_for_chat("123x", "cookies")
    add_item_for_chat("123x", "coffee")
    add_item_for_chat("456", "apples")

    assert list_items_for_chat("123x") == ["milk", "cookies", "coffee"]
    assert list_items_for_chat("456") == ["apples"]
