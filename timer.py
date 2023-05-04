import time
from nitshe import quots
import random
import vk_api
from refresh import refresh
def set_user_status(n):
    vk.status.set(text=n)

# token1='vk1.a.Udr2tDhFN01bBzu6KLionmJlTNaQ91MwQCHZMvWEhYgvulPi-pKERYHHMWUodH1mfERupCk3YwjkADIJI5rYZMGtbTKq1pHix535muWfNVd5XnFR8CM_exqsAU2m8_JumHE75ZU59X0IGe5G8Ld-Cr_2W00UkLDDBS-5eZdIJ5CgvNn_GqoxqMd_9BIQN9AaFuHXGI2hiVtDlsKygvwqTA'
token1='vk1.a.ef_5chBofs43PravhAmfSARhgGRrAyrxUVr3CJSgLPfAmM4356E5owMQSVxaYRtkXYKyWHqqNgSuRCaKIV1oOYYMnHMqgmCThRNyZDfN2IGVY2QoTXyIQKI_bf42A3J_mbO7zfYC6W1V0NpRR3U0ScaDrLGio7h2f-RrSfGmlWpYWVxyJXJG7y9qLUH3cV9YMbmtUOPvjkiSLk4BF4MBtg'

session = vk_api.VkApi( token=token1)
vk = session.get_api()

q=len(quots)-1
while True:
    try:
        x = random.randint(0, q)
        set_user_status(quots[x])
        time.sleep(100)
    except:
        token2=refresh(access_token=token1)
        session = vk_api.VkApi(token=token2)
        vk = session.get_api()
        print('exetpt srabotal')



