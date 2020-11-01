print("hi! let's begin!")
import scrapy
from bs4 import BeautifulSoup
class AppleCrawler(scrapy.Spider):
    name='apple'
    start_urls=['https://hk.appledaily.com']
    def parse(self,response):
        res=BeautifulSoup(response.body)
        for news in res.select('html'):
            print(news.select('lang')[0].text)

