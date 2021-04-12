# How-to-scrawl-ZhiHu.com-by-selenium

谢谢百度的小钟同学给的技术支持

记录一下这个爬虫的坑.
首先 cookie 要知道,他是不跨浏览器的.
第二点是通过代码debug知道,  selium和chrome不是一个浏览器, 他们获取的cookie不同. 没法用chrome的直接贴过来用.
第三个是反爬虫设置.options.add_experimental_option('excludeSwitches', ['enable-automation'])
