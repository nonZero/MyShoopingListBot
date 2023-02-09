class DictStorage:
    def __init__(self):
        self.db = {}

    def add_item_for_chat(self, chat_id: str, item: str):
        if chat_id not in self.db:
            self.db[chat_id] = []
        self.db[chat_id].append(item)

    def list_items_for_chat(self, chat_id: str):
        return self.db.get(chat_id, [])
