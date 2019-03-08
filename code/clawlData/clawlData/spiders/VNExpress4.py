import scrapy
import re

class VNExpressCollectLink(scrapy.Spider):
    name = "VNExpressFinal"
    def start_requests(self):


        urls = ['https://vnexpress.net/thoi-su']

        for url in urls:
            yield scrapy.Request(url= url, callback = self.getLink)




    def getLink(self, response):
        for newLink in response.xpath('//*[@class="title_news" and not(i)]/a[1]/@href'):
            yield scrapy.Request(url= newLink.extract().encode('utf-8').strip(), callback= self.parse_article )
            #print(newLink.extract().encode('utf-8').strip())


    def parse_article(self, response):
        article = {}
        article['TITLE'] = response.xpath('/html/body/section[2]/section[1]/section[1]/h1/text()').extract()[0].encode('utf-8').strip()
        article['DESCRIPTION'] = response.xpath('/html/body/section[2]/section[1]/section[1]/p[1]/text()').extract()[0].encode('utf-8').strip()

        # handle content with a set of <p> tag
        index = 1
        for content in response.xpath('/html/body/section[2]/section[1]/section[1]/article/p[@class="Normal"]'):
            article[index] = content.extract().encode('utf-8').strip()
            # artilce[index] = re.sub(re.compile('<.*?>'), "", artilce[index])
            article[index] = re.compile(r'<[^>]+>').sub('', article[index])

            index += 1


        for key, text in article.iteritems():
            print("\n")
            if type(key) is int:
                print("{key} : {text}".format(key=key, text=text))
            else:
                print("{key} : {text}".format(key=key.upper(), text=text))
            print("")
