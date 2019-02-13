simple crawler using scrapy framework . scrapy have useful features like : avoiding duplicate urls, limitation on depth , defining request rate and ... . \n
you need to install scrapy :
`pip install scrapy`
and run the crawlers :  <br />

`scrapy crawl hamshahri -o hamshahri.json`  <br />
`scrapy crawl blog `  <br />
`scrapy crawl blogfa `  <br />
`scrapy crawl blogsky `  <br />
`scrapy crawl dorsablog `  <br />
`scrapy crawl mihanblog `  <br />
`scrapy crawl persianblog `  <br />
your corpus will be ready in standard format in corpus_{spider_name}.txt file.
settings can be found in :'crawler/settings.py'  <br />
spiders are available in 'crawler/spiders'



