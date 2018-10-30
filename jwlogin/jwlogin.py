#encoding=utf8
import requests
###
url = 'https://sso5x.laosiji.com/sso/login?clientid=9998'
### 登录需要提交的表单
form_data = {'username':'18503711', #填入网站的上网帐号
              'password':'11220',  #填入网站密码（加密后的）
    }
s = requests.session()
response = s.post(url,data = form_data,)
print   (response.text)
