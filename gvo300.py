#!/usr/bin/python
# -*- coding: utf-8-*-

import urllib2, urllib, sys, random, time
import cookielib

captcha_url = "http://appapns.www.gov.cn/govdata/captcha.php"
mission_url = "http://appapns.www.gov.cn/govdata/info_gather.shtml"
ref_url = "http://app.www.gov.cn/govdata/html5/2017cyc/?_source=govapp"

starttime = time.time()
timeout=10
iphone = str(raw_input("phone="))

_cookie = cookielib.CookieJar()
cookie = urllib2.build_opener(urllib2.HTTPCookieProcessor(_cookie))
urllib2.install_opener(cookie)

user_agent = "GovCnAndroid(yingyongbao;8)"

#headers = { 'User-Agent' : user_agent , "Cache-Control" : "no-cache" , "Connection" : "keep-alive" , \
#            'referer':ref_url , "Content-Type": "application/x-www-form-urlencoded",  }

headers = { 'User-Agent' : user_agent , 'referer':ref_url , "Content-Type": "application/x-www-form-urlencoded",  }

req = urllib2.Request(captcha_url, headers=headers)
captcha_time = str(int(time.time()))
try:
    fin = urllib2.urlopen(req,timeout=timeout).read()
except:
    sys.exit('error, captcha')

f = open("captcha.jpg", 'wb')      
f.write(fin)
f.close()  

#http://appapns.www.gov.cn/govdata/info_gather.shtml?jsoncallback=phone_cb&phone={captcha={֤_mats={ʱ()}&callback=phone_cb

#input_captcha = raw_input("captcha=")
raw_input("captcha")

f = open("captcha.txt", 'rb') 
input_captcha = f.read()
f.close()  

postdata = urllib.urlencode({"jsoncallback" : "phone_cb", "phone": iphone, "captcha": str(input_captcha), \
                               "_mats": captcha_time, "callback": "phone_cb", })

#captcha_time = str(int(time.time()))
#postdata = "jsoncallback=phone_cb&phone=" + iphone + "&captcha=" + str(input_captcha) + "&_mats=" + captcha_time + "&callback=phone_cb"

print postdata
post_respo = urllib2.Request(mission_url, data=postdata, headers=headers)

#mission_url = mission_url + "?" + str(postdata)
#post_respo = urllib2.Request(mission_url, data="", headers=headers)

try:
    post_response = urllib2.urlopen(post_respo,timeout=timeout).read()
except:
    sys.exit('error, post_response')

print post_response
#phone_cb({"status":0,"error":"OK"})
