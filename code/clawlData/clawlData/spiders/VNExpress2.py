import scrapy

class ClawlVNExpress2(scrapy.Spider):
    name = "VNExpressGetLink"

    start_urls = ['https://vnexpress.net/thoi-su']

    def parse(self, response):
        for paragraph in response.xpath('//*[@class="title_news" and not(i)]/a[1]/@href'):
            print(paragraph.extract().encode('utf-8').strip())