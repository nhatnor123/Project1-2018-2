import scrapy
import re
import json


class ClawlVNExpress(scrapy.Spider):
    name = "VNExpressTextPage"

    def start_requests(self):
        urls = [
            'https://vnexpress.net/thoi-su/bo-truong-giao-thong-de-nghi-ai-mat-giay-phep-lai-xe-deu-phai-thi-lai-3890474.html']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_artilce)


    def parse_artilce(self, response):
        artilce = {}
        artilce['TITLE'] = response.xpath('/html/body/section[2]/section[1]/section[1]/h1/text()').extract()[0].encode('utf-8').strip()
        artilce['DESCRIPTION'] = response.xpath('/html/body/section[2]/section[1]/section[1]/p[1]/text()').extract()[0].encode('utf-8').strip()


        # handle content with a set of <p> tag
        index = 1
        for content in response.xpath('/html/body/section[2]/section[1]/section[1]/article/p[@class="Normal"]'):
            artilce[index] = content.extract().encode('utf-8').strip()
            # artilce[index] = re.sub(re.compile('<.*?>'), "", artilce[index])
            artilce[index] = re.compile(r'<[^>]+>').sub('', artilce[index])

            index += 1


        for key, text in artilce.iteritems():
            print("\n")
            if type(key) is int:
                print("{key} : {text}".format(key=key, text=text))
            else:
                print("{key} : {text}".format(key=key.upper(), text=text))
            print("")
            print(type(key))
            print(type(text))


        #print(json.dumps(artilce, indent=4, sort_keys=True))