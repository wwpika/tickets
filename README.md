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
