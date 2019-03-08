import scrapy
import re
import json


class ClawlVNExpress(scrapy.Spider):
    name = "VNExpressImagePage"

    def start_requests(self):
        urls = [
            'https://vnexpress.net/thoi-su/khi-tai-hien-dai-tren-hai-tau-chien-nhat-ban-den-da-nang-3890650.html']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_artilce)


    def parse_artilce(self, response):
        artilce = {}
        artilce['TITLE'] = response.xpath('//*[@id="col_sticky"]/h1/text()').extract()[0].encode(
            'utf-8').strip()
        artilce['DESCRIPTION'] = response.xpath('//*[@id="col_sticky"]/p/text()').extract()[
            0].encode('utf-8').strip()


        # handle content with a set of <p> tag
        index = 1
        for content in response.xpath('//*[@class="sidebar_1"]'):
            artilce[index] = content.extract().encode('utf-8').strip()
            #artilce[index] = re.sub(re.compile('<.*?>'), "", artilce[index])
            artilce[index] = re.compile(r'<[^>]+>').sub('', artilce[index])

            index += 1


        for key, text in artilce.iteritems():
            print("\n")
            if type(key) is int:
                print("{key} : {text}".format(key=key, text=text))
            else:
                print("{key} : {text}".format(key=key.upper(), text=text))
            print("")
            #print(type(key))
            #print(type(text))


        #print(json.dumps(artilce, indent=4, sort_keys=True))