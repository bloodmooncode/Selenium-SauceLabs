import requests
import time
from signuptest import KYC_Process_Control
from transfertest import Transfer_Process_Control

baseURL = "https://apitest.mainnetdigital.com/api"


def acquire_permission():
    # 登录管理员权限
    post_url = baseURL + '/auth/local'
    params = {
        "identifier": "xiaoyu@mainnet.digital",
        "password": "123456"
    }

    response = requests.post(post_url, params)
    # 获取jwt_token
    data = response.json()
    token = data["jwt"]
    # print(token)
    return token


def KYC_approve():
    # 修改KYC认证状态
    token = acquire_permission()
    put_url = baseURL + '/users-permissions/status/146'
    auth = 'Bearer ' + token
    # print(auth)
    headers = {'content-type': 'application/json',
               'Authorization': auth}
    body = {
        "action": "APPROVE"
    }
    result = requests.put(put_url, json=body, headers=headers)
    # print(result.json())
    time.sleep(5)


def Process_Control():
    KYC_Process_Control()
    acquire_permission()
    KYC_approve()
    time.sleep(10)
    Transfer_Process_Control()


if __name__ == "__main__":
    Process_Control()
