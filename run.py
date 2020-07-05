from urllib import parse
from urllib.request import urlopen,Request
from urllib.parse import urlencode
import json

base_url = 'https://www.sonkwo.com/api/search/skus.json'
ua = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
url_dic={
	'per':10,
	'page':1,
	'q[where][cate]':'game',
	'q[where][_or][][area]':'native',
	'q[where][_or][][area]':'abroad',
	'q[order][wishes_count]':'desc',
	'locale':'js',
	'sonkwo_version':1,
	'sonkwo_client':'mobile',
	'_':1593929161023
}

url = '{}?{}'.format(base_url,parse.urlencode(url_dic))

req = Request(url,headers={
		'User-agent':ua
})

with urlopen(req) as res:
	result_first = json.loads(res.read())
	result_second = result_first['skus']

	print('目前杉果游戏上，大家都想要的游戏榜单如下：\n')
	for i in range(len(result_second)):
		temp = dict(result_second[i])
		a = i+1
		print(str(a)+':'+temp['sku_names']['default']+'\n')
