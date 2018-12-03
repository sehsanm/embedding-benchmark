import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.hamshahrionline.ir/'
    ]
    allowed_domains=["hamshahrionline.ir"]
    def parse(self, response):
        for quote in response.css('p::text').extract():
            yield {
                'text': quote
            }
        for href in response.css('a::attr(href)').extract():
            yield response.follow(href, callback=self.parse)
