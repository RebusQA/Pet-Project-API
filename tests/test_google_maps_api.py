from requests import Response

from utils.api import Google_maps_api

"""Создание, изменение и удаление новой локации"""
class Test_create_place():
    
    def test_create_new_place(self):

        print("Метод POST")
        result_post: Response = Google_maps_api.create_new_place()