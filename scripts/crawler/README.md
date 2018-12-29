# simple crawler by scrapy


simple crawler using scrapy framework . scrapy have useful features like : avoiding duplicate urls,limitation on depth , defining request rate and ... .

you can make your corpus in standard format(each sentence in one line) just by running below commands :

you need to install scrapy :

`pip install scrapy`

and run the crawler :

`scrapy crawl hamshahri -o ham.json`

{your_spider_name}_corpus.txt  will be maked in this directory after running second command.
settings can be found in :'crawler/settings.py' and 'crawler/spiders/hamshahri_spider.py'.sample hamshahri_corpus.txt maked by this command. in piplines.py we used hazm sentence segmentor to segment crawled text to sentences.


