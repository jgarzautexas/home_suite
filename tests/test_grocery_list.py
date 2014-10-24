import pytest
import requests
from grocery_list import models

SERVER = "http://localhost:8000"

def test_raise():

    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_grocery_list_model():
    title = "My Test List"
    l = models.GroceryList(title=title)
    assert l.title == title

def test_index():
    api_call = "/"
    api_url = "{0}{1}".format(SERVER, api_call)
    res = requests.get(api_url,
                        data={},
                        auth=None,
                        # headers=self.__test_headers,
                        verify=False
    )

    assert res.ok
    assert res.status_code == 200
    assert "Personal Assistant" in res.text

def test_grocery_list_post():
    api_call = "/grocery_list"
    api_url = "{0}{1}".format(SERVER, api_call)
    data = {'title': "My Test List"}
    res = requests.post(api_url,
                        data=data,
                        auth=None,
                        # headers=self.__test_headers,
                        verify=False
    )
    assert res.ok
    assert res.status_code == 200
    assert data.get("title") in res.json().values()
    assert res.json().get('id')

def test_add_item():
    list_item = 1
    api_call = "/grocery_list/{0}/item".format(list_item)
    api_url = "{0}{1}".format(SERVER, api_call)
    data = {'name': "My Test Item"}

    res = requests.post(api_url,
                        data=data,
                        auth=None,
                        # headers=self.__test_headers,
                        verify=False
    )
    assert res.ok
    assert res.json().get("name") == data.get("name")
    assert res.json().get("active")

def test_update_item():
    list_item = 1
    api_call = "/grocery_list/{0}/item".format(list_item)
    api_url = "{0}{1}".format(SERVER, api_call)
    data = {'name': "My Test Item PUT", 'id': 1, 'active': False}

    res = requests.put(api_url,
                        data=data,
                        auth=None,
                        verify=False
    )
    assert res.ok
    assert res.json().get("id") == data.get("id")
    assert res.json().get("name") == data.get("name")
    assert res.json().get("active") == data.get("active")












