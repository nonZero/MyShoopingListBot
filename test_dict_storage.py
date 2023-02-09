from dict_storage import add_item_for_chat, DB


def test_add_item_to_db():
    add_item_for_chat("123x", "milk")
    add_item_for_chat("123x", "cookies")
    add_item_for_chat("123x", "coffee")
    add_item_for_chat("456", "apples")
