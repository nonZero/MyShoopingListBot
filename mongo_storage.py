from pymongo import MongoClient


class MongoStorage:
    def __init__(self, is_test=False):
        self.client = MongoClient()
        db_name = "shooping_list_bot"
        if is_test:
            db_name += "_test"
            self.client.drop_database(db_name)
        self.db = self.client.get_database(db_name)
        self.lists = self.db.get_collection("lists")
        self.lists.create_index("chat_id", unique=True)

    def add_item_for_chat(self, chat_id: str, item: str):
        self.lists.update_one({"chat_id": chat_id}, {
            '$push': {'items': item}
        }, upsert=True)

    def list_items_for_chat(self, chat_id: str):
        d = self.lists.find_one({"chat_id": chat_id})
        if d is None:
            return []
        return d['items']
