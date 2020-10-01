import requests
import json


def send_single_sms(apikey, code, mobile):
    url = 'https://sms.yunpian.com/v2/sms/single_send.json'
    text = '您的验证码是{}'.format(code)
    res = requests.post(url, data={
        'apikey': apikey,
        'mobile': mobile,
        'text': text
    })

    # 用于实际发送短信
    # re_json = json.loads(res.text)
    # return re_json

    # 用于测试
    r = {'code': 0}
    return r
