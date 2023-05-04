import requests

def refresh(access_token):
    api_version = "5.131"
    extend = 1
    response = requests.post(
        "https://api.vk.com/method/auth.refreshToken",
        data={
            "access_token": access_token,
            "v": api_version,
            "extend": extend   } )

    response_json = response.json()
    new_access_token = response_json["response"]["token"]
    # expires_in = response_json["response"]["expires_in"]
    return new_access_token