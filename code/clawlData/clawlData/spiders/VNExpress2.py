import scrapy

class ClawlVNExpress2(scrapy.Spider):
    name = "VNExpress2"

    start_urls = ['https://vnexpress.net/thoi-su/bo-truong-giao-thong-de-nghi-ai-mat-giay-phep-lai-xe-deu-phai-thi-lai-3890474.html']

    def parse(self, response):
        for paragraph in response.xpath('/html/body/section[2]/section[1]/section[1]/article/p[@class="Normal"]'):
            print(paragraph.extract().encode('utf-8').strip())