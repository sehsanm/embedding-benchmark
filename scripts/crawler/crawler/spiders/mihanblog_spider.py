import scrapy


class QuotesSpider(scrapy.Spider):
    name = "mihanblog"
    start_urls = [
        'http://mihanblog.com/'
    ]
    allowed_domains=["mihanblog.com"]
    def parse(self, response):
        for quote in response.css('p::text').extract():
            yield quote
            yield {
                'text': quote.strip()
            }
        for href in response.css('a::attr(href)').extract():
            yield response.follow(href, callback=self.parse)
