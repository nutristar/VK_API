import requests
import random
from nitshe import quots
import vk_api
API_VERSION = 5.131
ACCESS_TOKEN='vk1.a.ef_5chBofs43PravhAmfSARhgGRrAyrxUVr3CJSgLPfAmM4356E5owMQSVxaYRtkXYKyWHqqNgSuRCaKIV1oOYYMnHMqgmCThRNyZDfN2IGVY2QoTXyIQKI_bf42A3J_mbO7zfYC6W1V0NpRR3U0ScaDrLGio7h2f-RrSfGmlWpYWVxyJXJG7y9qLUH3cV9YMbmtUOPvjkiSLk4BF4MBtg'
group_id = 9064632
owner_id = GROUP_ID = 9064632

vk_session = vk_api.VkApi(login='+375298692442', password='778899lol', token='vk1.a.ef_5chBofs43PravhAmfSARhgGRrAyrxUVr3CJSgLPfAmM4356E5owMQSVxaYRtkXYKyWHqqNgSuRCaKIV1oOYYMnHMqgmCThRNyZDfN2IGVY2QoTXyIQKI_bf42A3J_mbO7zfYC6W1V0NpRR3U0ScaDrLGio7h2f-RrSfGmlWpYWVxyJXJG7y9qLUH3cV9YMbmtUOPvjkiSLk4BF4MBtg')
# авторизируемся
vk_session.auth()
# создаем объект для работы с методами API
vk = vk_session.get_api()

# загружаем фотографию на сервер VK API
upload_url = 'https://api.vk.com/method/photos.getWallUploadServer'
response = requests.get(upload_url, params={'access_token': ACCESS_TOKEN, 'v': 5.131 , 'group_id': 9064632})
upload_url = response.json()['response']['upload_url']
pn=random.randint(1,5)
photo_path = f'{pn}.jpg'
with open(photo_path, 'rb') as file:
    photo = file.read()

response = requests.post(upload_url, files={'photo': ('photo.jpg', photo, 'image/jpeg')})
photo_data = response.json()

# сохраняем фотографию на сервере VK API
save_url = 'https://api.vk.com/method/photos.saveWallPhoto'
response = requests.post(save_url, data={
    'access_token': ACCESS_TOKEN,
    'v': API_VERSION,
    'group_id': GROUP_ID,
    'server': photo_data['server'],
    'photo': photo_data['photo'],
    'hash': photo_data['hash']
})
photo_data = response.json()['response'][0]

print(photo_data)
print(photo_data['owner_id'])
print(photo_data['id'])
# публикуем пост на стене группы с загруженной фотографией
# owner_id = f'-{GROUP_ID}'
# message = 'kkkkkkkkkkkkkkkkkk'
# attachments = f"photo{photo_data['owner_id']}_{photo_data['id']}"
# response = requests.post('https://api.vk.com/method/wall.post', data={
#     'access_token': ACCESS_TOKEN,
#     'v': API_VERSION,
#     'owner_id': owner_id,
#     'message': message,
#     'attachments': attachments
# })

# from REUEST STYLE
# # публикуем пост на стене пользователя с загруженной фотографией
owner_id = '9064632'
x = random.randint(0, len(quots)-1)
message = quots[x]
attachments = f"photo{photo_data['owner_id']}_{photo_data['id']}"
vk.wall.post(owner_id=owner_id, message=message, attachments=attachments)

