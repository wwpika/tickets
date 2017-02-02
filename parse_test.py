import re
import requests
from pprint import pprint

url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8994'
response=requests.get(url,verify=False)
sta=re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
stations=dict(sta)
#pprint(dict(sta),indent=4)
#print(stations)