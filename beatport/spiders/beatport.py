import scrapy

class BeatportSpider(scrapy.Spider):
    name = 'beatport_spider'
    allowed_domains = ['beatport.com']
    start_urls = ['https://www.beatport.com/top-100']

    def start_requests(self):
        url = 'https://www.beatport.com/top-100'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for i in range(1,101):
            yield {
            'title': response.xpath('//*[@id="pjax-inner-wrapper"]/section/main/div/div[2]/ul/li[{}]/div[3]/p[1]/a/span[1]/text()'.format(i)).extract_first(),
            'remix': response.xpath('//*[@id="pjax-inner-wrapper"]/section/main/div/div[2]/ul/li[{}]/div[3]/p[1]/a/span[2]/text()'.format(i)).extract_first(),
            'genre': response.xpath('//*[@id="pjax-inner-wrapper"]/section/main/div/div[2]/ul/li[{}]/div[3]/p[5]/a/text()'.format(i)).extract_first(),
            'artist': response.xpath('//*[@id="pjax-inner-wrapper"]/section/main/div/div[2]/ul/li[{}]/div[3]/p[2]/a/text()'.format(i)).extract_first(),
            'link': 'https://www.beatport.com' + (response.xpath('//*[@id="pjax-inner-wrapper"]/section/main/div/div[2]/ul/li[{}]/div[3]/p[2]/a/@href'.format(i)).extract_first()),
            'release': response.xpath('//*[@id="pjax-inner-wrapper"]/section/main/div/div[2]/ul/li[{}]/div[3]/p[6]/text()'.format(i)).extract_first(),
            'price': response.xpath('//*[@id="pjax-inner-wrapper"]/section/main/div/div[2]/ul/li[{}]/div[4]/div/div[2]/button[1]/text()'.format(i)).extract_first()[1:]
                    }
