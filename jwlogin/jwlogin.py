#encoding=utf8
import requests
### 登录页的url
url = 'https://sso5x.laosiji.com/sso/login?clientid=9998'
### 登录需要提交的表单
form_data = {'username':'18503718321', #填入网站的上网帐号
    'password':'1122080!@',  #填入网站密码（加密后的）
    }
s = requests.session()
response = s.post(url,data = form_data,)
print   (response.text)
