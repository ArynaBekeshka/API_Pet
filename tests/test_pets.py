import os

import pytest

from api import Pets

pt = Pets()


@pytest.mark.positive
def test_get_token():
    status = pt.get_token()[1]
    token = pt.get_token()[0]
    my_id = pt.get_token()[2]
    assert token
    assert status == 200
    assert my_id


def test_list_users():
    status = pt.get_list_users()[0]
    my_id = pt.get_list_users()[1]
    assert status == 200
    assert my_id


def test_create_pet():
    status = pt.create_pet()[1]
    pet_id = pt.create_pet()[0]
    assert status == 200
    assert pet_id


def test_get_pet_photo(pet_photo='tests\\photo\\pet.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status = pt.post_pet_photo()[0]
    assert status == 200
    assert pet_photo


def test_get_list_pets():
    status = pt.get_list_pets()[0]
    pets_list = pt.get_list_pets()[1]
    assert status == 200
    assert pets_list


def test_update_pet():
    status = pt.update_pet()
    assert status == 200


def test_put_like_pet():
    status = pt.put_like_pet()
    assert status == 200


def test_put_comment_pet():
    status = pt.put_comment_pet()
    assert status == 200


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200


def test_delete_all_created_pets():
    status = pt.delete_all_created_pets()
    if status == 200:
        print("Success: All created pets were deleted successfully.")
    elif status == 422:
        print("Error: Validation error occurred while deleting pets.")
    else:
        print(f"Error: Unexpected status code received: {status}")
    assert status == 200


@pytest.mark.negative
def test_delete_another_pet():
    status = pt.delete_another_pet()
    assert status != 200
