import time
from nitshe import quots
import random
import vk_api
import requests
from refresh import refresh
# def set_user_post(text):
#     vk.wall.post(owner_id=9064632, friends_only=0, message =text, attachments = photo)
#
# token1='vk1.a.Udr2tDhFN01bBzu6KLionmJlTNaQ91MwQCHZMvWEhYgvulPi-pKERYHHMWUodH1mfERupCk3YwjkADIJI5rYZMGtbTKq1pHix535muWfNVd5XnFR8CM_exqsAU2m8_JumHE75ZU59X0IGe5G8Ld-Cr_2W00UkLDDBS-5eZdIJ5CgvNn_GqoxqMd_9BIQN9AaFuHXGI2hiVtDlsKygvwqTA'
#
# session = vk_api.VkApi( token=token1)
# vk = session.get_api()
#
# q=len(quots)-1
# while True:
#     try:
#         x = random.randint(0, q)
#         set_user_post(quots[x])
#         time.sleep(100)
#     except:
#         token2=refresh(access_token=token1)
#         session = vk_api.VkApi(token=token2)
#         vk = session.get_api()



# создаем объект VkApi
vk_session = vk_api.VkApi(login='+375298692442', password='778899lol')

# авторизируемся
vk_session.auth()

# создаем объект для работы с методами API
vk = vk_session.get_api()
rand_phot=random.randint(1,5)
# загружаем фотографию на сервер ВКонтакте
upload_url = vk.photos.getWallUploadServer()['upload_url']
photo_path = f'{rand_phot}.jpg'
with open(photo_path, 'rb') as file:
    photo = file.read()
# response = vk_api.upload.VkUpload(upload_url, {'photo': photo})

# with open(photo_path, 'rb') as file:
#     files = {'photo': file}

    # Отправляем POST-запрос на сервер VK API, передавая файл в параметре files
response = requests.post(upload_url,  {'photo': photo} )  #+

# Получаем данные о загруженной фотографии
photo_data2 = response.json()

print(photo_data2)

# photo_data = vk.photos.saveWallPhoto(photo_data2)
# q=len(quots)-1
# x = random.randint(0, q)
# 
#
# # # публикуем пост на стене пользователя с загруженной фотографией
# owner_id = '9064632'
# message = quots[x]
# attachments = f"photo{photo_data[0]['owner_id']}_{photo_data[0]['id']}"
# vk.wall.post(owner_id=owner_id, message=message, attachments=attachments)
#



