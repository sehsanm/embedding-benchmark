import scrapy


class QuotesSpider(scrapy.Spider):
    name = "blog"
    start_urls = [
        'http://blog.ir/topblogs/96'
    ]
    allowed_domains=["blog.ir"]
    def parse(self, response):
        for quote in response.css('p::text').extract():
            yield quote
            yield {
                'text': quote.strip()
            }
        for href in response.css('a::attr(href)').extract():
            yield response.follow(href, callback=self.parse)
