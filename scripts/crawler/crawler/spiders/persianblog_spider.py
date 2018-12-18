import scrapy


class QuotesSpider(scrapy.Spider):
    name = "persianblog"
    start_urls = [
        'https://persianblog.ir/'
    ]
    allowed_domains=["persianblog.ir"]
    def parse(self, response):
        for quote in response.css('p::text').extract():
            yield quote
            yield {
                'text': quote.strip()
            }
        for href in response.css('a::attr(href)').extract():
            yield response.follow(href, callback=self.parse)
