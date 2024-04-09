from requests import Response

from utils.api import Google_maps_api

"""Создание, изменение и удаление новой локации"""
class Test_create_place():
    
    def test_create_new_place(self):

        print("\nМетод POST")
        result_post = Google_maps_api.create_new_place()    # Переменная, хранит экземпляр класса из которой вызываю необходимый метод.
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Метод GET POST")
        result_get = Google_maps_api.get_new_place(place_id)

        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)

        print("Метод GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)
