import scrapy
import re

class VNExpressCollectLink(scrapy.Spider):
    name = "VNExpressFinal"

    def start_requests(self):

        urlBase = ['https://vnexpress.net/thoi-su-p1', 'https://vnexpress.net/the-gioi-p1', 'https://vnexpress.net/y-kien-p2' ]
        #
        listUrls = {'https://vnexpress.net/thoi-su-p2' : 3500, 'https://vnexpress.net/the-gioi-p2' : 3000, 'https://vnexpress.net/kinh-doanh/p2' : 850, 'https://vnexpress.net/the-thao/p2' : 1000, 'https://vnexpress.net/phap-luat-p2' : 2000, 'https://vnexpress.net/giao-duc-p2' : 1000, 'https://vnexpress.net/doi-song/p2' : 700, 'https://vnexpress.net/du-lich/p2' : 800, 'https://vnexpress.net/khoa-hoc-p2' : 1000, 'https://vnexpress.net/so-hoa/p2' : 500, 'https://vnexpress.net/oto-xe-may-p2' : 1000, 'https://vnexpress.net/tam-su-p2' : 1000}

        # totalPage = 10
        # for page in range(totalPage):
        #     url =urlBase[0].replace(str(1), str(page+1))       #the reason why must use  (page + 1) is range(x) from 0 to (x-1)
        #     yield scrapy.Request(url=url, callback=self.getLink)

        print(listUrls)
        maxPageNumber = 0
        for url in listUrls:
            print(listUrls[url])
            maxPageNumber = listUrls[url]
            #print(maxPageNumber)
            for page in range(1, maxPageNumber+1, 1):
                urlTemp = url.replace(str(2), str(page))
                print(urlTemp)
                print(page)
                yield scrapy.Request(url=urlTemp, callback=self.getLink)


    #get the real link to the page we want crawl data from https://vnexpress.net/thoi-su
    def getLink(self, response):
        for newLink in response.xpath('//*[@class="sidebar_1"]//*[@class="title_news" and not(i)]/a[1]/@href'):
            yield scrapy.Request(url= newLink.extract().encode('utf-8').strip(), callback= self.parse_article )
            #print(newLink.extract().encode('utf-8').strip())


    #crawl data from link
    def parse_article(self, response):
        article = []
        article.append( response.xpath('/html/body/section[2]/section[1]/section[1]/h1/text()').extract()[0].encode('utf-8').strip())
        article.append( response.xpath('/html/body/section[2]/section[1]/section[1]/p[1]/text()').extract()[0].encode('utf-8').strip())

        # handle content with a set of <p> tag
        for content in response.xpath('/html/body/section[2]/section[1]/section[1]/article/p[@class="Normal"]'):
            temp = content.extract().encode('utf-8').strip()
            # artilce[index] = re.sub(re.compile('<.*?>'), "", artilce[index])
            article.append( re.compile(r'<[^>]+>').sub('', temp))


        #directory of file txt which be writen crawl data
        file = open('/home/nhatnor123/Desktop/test2.txt', 'a')

        # for key, text in article.iteritems():
        #
        #     if type(key) is int:
        #         print("{key} : {text}".format(key=key, text=text))
        #     else:
        #         print("{key} : {text}".format(key=key.upper(), text=text))
        #
        #     #write data to the extenal file txt
        #     #file.write("\n")
        #     file.write(text.replace("\n", " "))
        # file.write("\n")
        # file.close()


        for line in range(len(article)):
            #print(article[line])
            #write data to the extenal file txt
            #file.write("\n")
            file.write(article[line].replace("\n", " "))
            if line == 0 :
                file.write(" . ")
        file.write("\n")
        file.close()