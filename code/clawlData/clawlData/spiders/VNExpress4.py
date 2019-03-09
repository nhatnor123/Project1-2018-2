import scrapy
import re

class VNExpressCollectLink(scrapy.Spider):
    name = "VNExpressFinal"

    def start_requests(self):

        urlBase = 'https://vnexpress.net/thoi-su-p1'

        totalPage = 3
        for page in range(totalPage):
            url =urlBase.replace(str(1), str(page+1))       #the reason why must use  (page + 1) is range(x) from 0 to (x-1)
            yield scrapy.Request(url=url, callback=self.getLink)


    #get the real link to the page we want crawl data from https://vnexpress.net/thoi-su
    def getLink(self, response):
        for newLink in response.xpath('//*[@class="sidebar_1"]//*[@class="title_news" and not(i)]/a[1]/@href'):
            yield scrapy.Request(url= newLink.extract().encode('utf-8').strip(), callback= self.parse_article )
            #print(newLink.extract().encode('utf-8').strip())


    #crawl data from link
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


        #directory of file txt which be writen crawl data
        file = open('/home/nhatnor123/Desktop/test.txt', 'a')

        for key, text in article.iteritems():

            if type(key) is int:
                print("{key} : {text}".format(key=key, text=text))
            else:
                print("{key} : {text}".format(key=key.upper(), text=text))

            #write data to the extenal file txt
            #file.write("\n")
            file.write(text)

        file.close()