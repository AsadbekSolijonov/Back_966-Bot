from utils.db_api.db import UsersFunctionality
import json
uf = UsersFunctionality()


class Translater:
    def get_data_by_language(self, chat_id):
        language_code = uf.get_language(chat_id)
        with open(f'locals/{language_code}/dictionary.json', 'rb') as data:
            datas = json.load(data)
            return datas

