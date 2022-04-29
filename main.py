import requests


def test_get_request():
    response = requests.get("https://hbs-ob-stage.herokuapp.com/status")
    response_body = response.json()
    assert response.status_code == 200


def test_post_request():
    payload = {
        "name": "user",
        "phone": "+91xxxxxxxxxx",
        "email": "user@hashedin.com",
        "password": "admin",
        "otp": 111111
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    response = requests.post(url=endpoint, data=payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 201


def test_get_otp():
    payload = {
        "phone": "+91xxxxxxxxxx"
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/get_register_otp"
    response = requests.post(url=endpoint, data=payload)
    assert response.status_code == 201


def test_delete_user():
    payload = {
        "phone": "+91xxxxxxxxxx",
        "otp": 111111
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    response = requests.delete(url=endpoint, data=payload)
    assert response.status_code == 201


def test_edit_user():
    payload = {
        "name": "user",
        "phone": "+91xxxxxxxxxx",
        "email": "user@hashedin.com",
        "password": "admin",
        "otp": 111111
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    response = requests.put(url=endpoint, data=payload)
    assert response.status_code == 201


def test_login_otp():
    payload = {
        "phone": "+91xxxxxxxxxx"
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/get_otp"
    response = requests.post(url=endpoint, data=payload)
    assert response.status_code == 201


def test_authenticate():
    payload1 = {
        "phone": "+91xxxxxxxxxx",
        "LoginType": "password",
        "password": "admin"
    }
    payload2 = {
        "phone": "+91xxxxxxxxxx",
        "LoginType": "OTP",
        "otp": 111111
    }
    endpoint = "https://hbs-ob-stage.herokuapp.com/authenticate"
    response1 = requests.post(url=endpoint, data=payload1)
    response2 = requests.post(url=endpoint, data=payload2)
    assert response1.status_code == 201
    assert response2.status_code == 201





