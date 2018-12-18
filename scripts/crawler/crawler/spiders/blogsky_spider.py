import scrapy


class QuotesSpider(scrapy.Spider):
    name = "blogsky"
    start_urls = [
        'http://www.blogsky.com/posts'
    ]
    allowed_domains=["blogsky.com"]
    def parse(self, response):
        for quote in response.css('p::text').extract():
            yield quote
            yield {
                'text': quote.strip()
            }
        for href in response.css('a::attr(href)').extract():
            yield response.follow(href, callback=self.parse)
