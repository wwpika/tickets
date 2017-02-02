# -*- coding:utf-8 -*-
"""命令行火车票查看器

Usage:
	tickets [-gdtkz] <from> <to> <date>

Options:
	-h,--help	显示帮助菜单
	-g          高铁
	-d 			动车
	-t 			特快
	-k			快速
	-z			直达

Example:
	tickets 北京 上海 2017-02-04
	tickets -dg  成都 南京 2017-02-04

"""

import requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init,Fore
import re
from pprint import pprint
from parse_test import stations
import json

init()

class TrainsCollection:
	header='车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()
	def __init__(self,available_trains,options):
		#available_trains:一个列表，包含可获得的火车班次，每个班次是一个字典
		#options:查询的选项，如高铁，动车。。。
		self.available_trains=available_trains
		self.options=options

	def _get_duration(self):
		duration=self.available_trains.get('lishi').replace(':','小时')+'分'
		if duration.startswith('00'):
			return duration[4:]
		if duration.startswith('0'):
			return duration[1:]
		return duration

	@property
	def trains(self):
		
			train_no=self.available_trains['station_train_code']
			
			initial=train_no[0].lower()
			if not self.options or initial in self.options:
				train=[
					train_no,
					'\n'.join([Fore.GREEN+self.available_trains['from_station_name']+Fore.RESET,
								Fore.RED+self.available_trains['to_station_name']+Fore.RESET]),
					'\n'.join([Fore.GREEN+self.available_trains['start_time']+Fore.RESET,
								Fore.RED+self.available_trains['arrive_time']+Fore.RESET]),
					self._get_duration(),
					self.available_trains['zy_num'],
					self.available_trains['ze_num'],
					self.available_trains['rw_num'],
					self.available_trains['yw_num'],
					self.available_trains['yz_num'],
					self.available_trains['wz_num'],

				]
				yield train


	def pretty_print(self):
		pt=PrettyTable()
		pt._set_field_names(self.header)
		for train in self.trains:
			pt.add_row(train)
		print(pt)




def cli():
	arguments=docopt(__doc__)
	from_station=stations.get(arguments['<from>'])
	print(from_station)
	to_station=stations.get(arguments['<to>'])
	print(to_station)

	date=arguments['<date>']
	print(date)
	url=('https://kyfw.12306.cn/otn/leftTicket/queryZ?'
		'leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&'
		'leftTicketDTO.to_station={}&purpose_codes=ADULT').format(
			date,from_station,to_station
		)

	options=''.join([
			key for key, value in arguments.items() if value is True
		])

#	url2='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2017-02-04&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
	r=requests.get(url,verify=False)
#	print(r.text)
	result=json.loads(r.text)
	print(len(result['data']))
	print(result['data'][1]['queryLeftNewDTO']['station_train_code'])

	#hjson=json.loads(content)
	#print(hjson['data'])
	for index in range(len(result['data'])):
		available_trains=r.json()['data'][index]['queryLeftNewDTO']
		print(available_trains)
		TrainsCollection(available_trains,options).pretty_print()


	


if __name__=='__main__':
	cli()