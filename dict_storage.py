DB = {}


def add_item_for_chat(chat_id: str, item: str):
    if chat_id not in DB:
        DB[chat_id] = []
    DB[chat_id].append(item)


def list_items_for_chat(chat_id: str):
    return DB.get(chat_id, [])
