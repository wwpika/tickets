import certifi
import urllib3
import requests
'''
http=urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
url2='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2017-02-04&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
r=http.request('GET',url2)
print(r.text)
'''
url2='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2017-02-04&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
r=requests.get(url2,verify=False)
print(r.text)