import requests
import pytest


person1 = {
    "name": "Ivanov",
    "address": "Moscow",
    "work": "IBM",
    "age": 32
}

person2 = {
    "name": "Smirnov",
    "address": "Parish",
    "work": "Google",
    "age": 20
}

patch_name = {"name": "Alex"}
patch_address = {"address": "London"}
patch_work = {"work": "Architector"}
patch_age = {"age": 21}


@pytest.mark.parametrize("persons", [person1, person2])
def test_post_get(persons):
    r = requests.post(url="http://localhost:8080/api/v1/persons", json=persons)
    assert r.status_code == 201
    redirected_urd = r.headers['Location']
    person_id_dict = {"id": int(redirected_urd.split("/")[-1])}
    r = requests.get(redirected_urd)
    assert r.status_code == 200
    assert r.json() == persons | person_id_dict


@pytest.mark.parametrize("persons, patch_var", [(person1, patch_name), (person1, patch_address),
                                                (person2, patch_work), (person2, patch_age)])
def test_post_patch(persons, patch_var):
    r = requests.post(url="http://localhost:8080/api/v1/persons", json=persons)
    redirected_urd = r.headers['Location']
    r = requests.patch(url=redirected_urd, json=patch_var)
    print(r.content)
    print(r.json())
    assert r.status_code == 200
    assert patch_var.items() <= r.json().items()


@pytest.mark.parametrize("persons", [person1, person2])
def test_post_delete(persons):
    r = requests.post(url="http://localhost:8080/api/v1/persons", json=persons)
    redirected_urd = r.headers['Location']
    r = requests.delete(redirected_urd)
    assert r.status_code == 204
    r = requests.get(redirected_urd)
    assert r.status_code == 400

