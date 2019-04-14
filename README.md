这个版本的漫画下载器添加了MySQL数据库，只要数据库中含有了下载地址，就可以直接下载，不用再次构造下载链接，也就不用模拟浏览器了，如果数据库里没有的话，还是会去构造下载地址的，构造完了后会将地址存入到数据库里再进行下载

目前只支持动漫狂网站的漫画下载，网址为 https://www.cartoonmad.com，以后会添加对更多网站的支持
且只支持一本一本下载，不支持同时下载多本，速度为两三秒一张图片，没办法，速度快了会被封ip
等之后添加代理的功能后速度会有大幅度的提升

要求
需要安装python最新版本，即3.x，安装的时候记得把添加到环境变量和pip这两个选项勾上
需要安装requests,lxml,BeautifulSoup4，selenium及pymysql模块,需要配置好MySQL数据库
电脑上需要安装chrome，且需要配置好chromedriver,把chromedriver下载下来放到程序所在目录即可

使用方法
运行download.py文件即可开始下载，动漫狂网站不翻墙的话下载速度会比较慢
已经添加了用户界面，只要根据界面上的提示输入即可
