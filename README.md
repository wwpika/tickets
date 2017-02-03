# tickets
python实现火车票查询工具，抓取的是12306的信息

用到的库：

requests，使用 Python 访问 HTTP 资源的库。

docopt，Python3 命令行参数解析工具。

prettytable， 格式化信息打印工具。

colorama，命令行着色工具

 注意 :
 
 1.如果是在windows环境，编译工具是sublime，你需要生成一个字典stations，用来存储{key=地名，values=代号}，不要把该字典重定向到stations.py中，
 不然全是乱码，直接拿来用就行
 
 2.请求接口，得到json数据，但json的格式已经改变了，今天抓取时(2017-02-02)，格式为：r.json()['data'][index]['queryLeftNewDTO']
 
 3.由于12306自身服务器的原因，当出现json EncodeError错误时，可以登录网站，看下能否查询票
 
 4.https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8994 
 
 5.yield 的作用就是把一个函数变成一个 generator,执行该函数就会返回一个可迭代对象；这样做，可以增强该函数的复用性，节省内存空间
