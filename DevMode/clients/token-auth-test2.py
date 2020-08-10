import requests

def client():
    # token_h= "Token 828de994290c206a442a05c6898336f39100a353"
    data = {
        "username": "resttest",
        "email":"test@rest.com",
        "password1": "hello098",
        "password2": "hello098"
        }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

    # headers = {"Authorization": token_h}
    # response = requests.get("http://127.0.0.1:8000/api2/profiles/", headers=headers)
    

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()