# simple crawler by scrapy


simple crawler using scrapy framework . scrapy have useful features like : avoiding duplicate urls,limitation on depth , defining request rate and ... .

you can make your corpus in standard format(each sentence in one line) just by running below commands :

you need to install scrapy :

`pip install scrapy`

and run the crawler :

`scrapy crawl hamshahri`

{your_spider_name}_corpus.txt  will be maked in this directory after running second command.
settings can be found in :'crawler/settings.py' and 'crawler/spiders/hamshahri_spider.py'.sample hamshahri_corpus.txt maked by this command. in piplines.py we used hazm sentence segmentor to segment crawled text to sentences. 

also there are many other spiders in crawler/spiders for other websites which you can run them by simply running :

`scrapy crawl {spider_name_property_value}`


and also you can create your spider to crawl other websites.