import requests
import time
import json
import processing
import Various_Url


# url_import = 'http://bucentertestb.xfanka.com/bucenter/system/emp/import'
# files = {'file': ('员工信息1.xlsx', open('/Users/wang/Downloads/pic/员工信息1.xlsx', 'rb'), 'octet-stream')}
# print(files, '22222222')
#
# # files = {"file":("wx.jpg", open("c:/wx.jpg", "rb"), "image/jpeg",{})
# headers = {'Content-Type': 'form-data', 'xfk-login-token': request.headers['xfk-login-token']}
#
# r = requests.post(url_import, headers=headers, files=files)
#
# print(r.text)
# ---------------------------------------

# def loginData():
#     data = {
#         'email': '13484545195',
#         'icode': '',
#         'origURL': 'http://www.renren.com/home',
#         'domain': 'renren.com',
#         'key_id': 1,
#         'captcha_type': 'web_login',
#         'password': '8d9a71152919613bbe3df9bfa0e1b390eb2b13dd1bdde270c2816cf04dd1b7c5',
#         'rkey': 'b4cdc6acc1d36171e3de73dd4676208e',
#         'f': 'http%3A%2F%2Fname.renren.com%2F'}
#     return data
#
#
# def login():
#     r = requests.post(
#         url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201894216799',
#         data=loginData(),
#         headers={'Content-Type': 'application/x-www-form-urlencoded'})
#     return r.cookies


# def uploadData():
#     data = {
#         "upload": "提交",
#         "__channel": "renren",
#         "privacyParams": '{"sourceControl": 99}',
#         'hostid': '967004081',
#         'requestToken': '-1124080368',
#         '_rtk': '88c0e36a'}
#     return data


def upload_emp():
    r = requests.post(
        Various_Url.emp_import,
        headers={'Conteny-Type': 'multipart/form-data',
                 'xfk-login-token': processing.controller_login().headers['xfk-login-token']},
        files={"file": ("员工信息1.xlsx", open("/Users/wang/Downloads/pic/员工信息1.xlsx", "rb"), "octet-stream", {})},
    )
    print((r.json()['list'])[0]['errorMessage'], '错误信息')
    print(((r.json()['list'][0]).keys()), '你猜')
    for i in (r.json()['list'][0]).keys():
        # print(i, '       都是key啊')
        pass
    r_data = (r.json()['list'])

    data_sh = []
    for i in range(0, len(r.json()['list'])):
        dict = {'accountNo': r_data[i]['accountNo'],
                'email': r_data[i]['email'],
                'idCard': r_data[i]['idCard'],
                'jobNumber': r_data[i]['jobNumber'],
                'name': r_data[i]['name'],
                'orgNo': r_data[i]['orgNo'],
                'parentJobNumber': r_data[i]['parentJobNumber'],
                'password': r_data[i]['password'],
                'phone': r_data[i]['phone'],
                'postNo': r_data[i]['postNo']}
        data_sh.append(dict)

    print( '这个是处理过要上传的数据',data_sh)
    print('这个是没处理过的',r_data)

    r = requests.post(
        url=Various_Url.emp_batchAdd,
        data=json.dumps(data_sh),
        headers=processing.headers_all
    )
    print('--------->>>>>>', r.json())


if __name__ == '__main__':
    upload_emp()
