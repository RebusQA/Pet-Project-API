import json

from utils.api import Google_maps_api
from utils.checking import Checking

"""Создание, изменение и удаление новой локации"""
class Test_create_place():
    
    def test_create_new_place(self):

        print("\nМетод POST")
        result_post = Google_maps_api.create_new_place()    # Переменная, хранит экземпляр класса из которой вызываю необходимый метод.
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        token = json.loads(result_post.text)
        print(list(token))

        print("Метод GET POST")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ["location", "accuracy", "name", "phone_number",
                                               "address","types", "website", "language"])

        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ["msg"])

        print("Метод GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ["location", "accuracy", "name", "phone_number",
                                   "address", "types", "website", "language"])

        print("Метод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ["status"])

        print("Метод GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ["msg"])

        print("\nТестирование создание, изменение и удаление новой локации, прошло успешно.")
