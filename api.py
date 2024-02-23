import json
import requests
from settings import URL, RegisterData, PetsData


class Pets:
    def __init__(self):
        self.base_url = URL.BASE_URL

    def get_token(self) -> json:
        """The method POST/login to the site Swagger get a unique user token using the valid email and password"""
        data = {"email": RegisterData.VALID_EMAIL,
                "password": RegisterData.VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self) -> json:
        """The method GET/users to the site Swagger gets a list of users by using a token"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        my_id = res.status_code
        return status, my_id

    def create_pet(self) -> json:
        """The method POST/pet to the site Swagger create a new pet"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"name": PetsData.NAME_DOG, "type": PetsData.TYPE_DOG, "age": PetsData.AGE_DOG,
                "gender": PetsData.GENDER_DOG, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def post_pet_photo(self) -> json:
        """The method POST/pet/{pet_id}/image to the site Swagger upload a photo for the pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': (
            'dog_pic.jpeg', open(r'/Users/arynabekeshko/PycharmProjects/API_Pet/photo_pet/dog_pic.jpeg', 'rb'),
            'image/jpeg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def get_list_pets(self) -> json:
        """The method POST/pets to the site Swagger gets a list of pets in your profile"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"user_id": my_id}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        pets_list = res.json()
        return status, pets_list

    def update_pet(self) -> json:
        """The method PATCH/pet to the site Swagger update a new pet"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id, "name": PetsData.NAME_DOG, "type": PetsData.TYPE_DOG, "gender": PetsData.GENDER_UPDATE,
                "age": PetsData.AGE_UPDATE, "owner_id": my_id}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def put_like_pet(self) -> json:
        """The method PUT/pet/{id}/like add like for pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        return status

    def put_comment_pet(self) -> json:
        """The method PUT/pet/{id}/comment add comment for pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "message": 'HOT! HOT! HOT!:)'
        }
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def delete_pet(self) -> json:
        """The method DELETE/pet/{id} delete pet account in your profile"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status


# Pets().get_token()
# # Pets().get_list_users()
# Pets().create_pet()
# # Pets().post_pet_photo()
# # Pets().get_list_pets()
# Pets().update_pet()
# Pets().put_like_pet()
# Pets().put_comment_pet()
# Pets().delete_pet()
