import requests
from lxml import etree

class Spider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "https://www.mzitu.com/xinggan/"
        }

    def start_request(self):
        for i in range(1,204):
            print("======正在抓取%s页========" %i)
            response = requests.get("https://www.mzitu.com/page/" + str(i) + "/", headers = self.headers)
            html = etree.HTML(response.content.decode())
            self.xpath_data(html)

    def xpath_data(self,html):
        src_list = html.xpath('//ul[@id="pins"]/li/a/img/@data-original')
        alt_list = html.xpath('//ul[@id="pins"]/li/a/img/@alt')
        for src, alt in zip(src_list, alt_list):
            file_name = 'D://pic//' + alt + '.jpg'
            response = requests.get(src, headers = self.headers)
            print('正在抓取图片' + file_name)
            try:
                with open(file_name,"wb") as f:
                    f.write(response.content)
            except:
                print("文件名有误!")

spider = Spider()
spider.start_request()