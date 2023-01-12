import requests
import pytest

API_URL = "http://127.0.0.1:5000/api/v1"
person1_add = {
    "name": "lev",
    "address": "dom",
    "work": "ne volk",
    "age": 0
}

person2_add = {
    "name": "volk",
    "address": "ne vispupaet",
    "work": "cirk",
    "age": 20
}

patch_name = {"name": "tigr"}
patch_address = {"address": "cirk"}
patch_work = {"work": "vispupaet"}
patch_age = {"age": 10}


@pytest.mark.parametrize("persons", [(person1_add), (person2_add)])
def test_post_get(persons):
    r = requests.post(url="http://127.0.0.1:5000/api/v1/persons", json=persons)
    assert r.status_code == 201
    redirected_urd = r.headers['Location']
    person_id_dict = {"id": int(redirected_urd.split("/")[-1])}
    r = requests.get(redirected_urd)
    assert r.status_code == 200
    assert r.json() == persons | person_id_dict


@pytest.mark.parametrize("persons, patch_var", [(person1_add, patch_name), (person1_add, patch_address),
                                                (person2_add, patch_work), (person2_add, patch_age)])
def test_patch(persons, patch_var):
    r = requests.post(url="http://127.0.0.1:5000/api/v1/persons", json=persons)
    redirected_urd = r.headers['Location']
    r = requests.patch(url=redirected_urd, json=patch_var)
    print(r.content)
    print(r.json())
    assert r.status_code == 200
    assert patch_var.items() <= r.json().items()


@pytest.mark.parametrize("persons", [(person1_add), (person2_add)])
def test_delete(persons):
    r = requests.post(url="http://127.0.0.1:5000/api/v1/persons", json=persons)
    redirected_urd = r.headers['Location']
    r = requests.delete(redirected_urd)
    assert r.status_code == 204
    r = requests.get(redirected_urd)
    assert r.status_code == 404

