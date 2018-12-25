import scrapy


class QuotesSpider(scrapy.Spider):
    name = "blogfa"
    start_urls = [
        'https://blogfa.com/members/'
    ]
    allowed_domains=["blogfa.com"]
    def parse(self, response):
        for quote in response.css('p::text').extract():
            yield quote
            yield {
                'text': quote.strip()
            }
        for href in response.css('a::attr(href)').extract():
            yield response.follow(href, callback=self.parse)
