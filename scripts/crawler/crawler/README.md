
simple crawler using scrapy framework . scrapy have useful features like : avoiding duplicate urls, limitation on depth , defining request rate and ... . \n
you need to install scrapy :
`pip install scrapy`
and run the crawlers :  <br />

`scrapy crawl hamshahri -o hamshahri.json`  <br />
`scrapy crawl blog -o blog.json`  <br />
`scrapy crawl blogfa -o blogfa.json`  <br />
`scrapy crawl blogsky -o blogsky.json`  <br />
`scrapy crawl dorsablog -o dorsablog.json`  <br />
`scrapy crawl mihanblog -o mihanblog.json`  <br />
`scrapy crawl persianblog -o persianblog.json`  <br />

settings can be found in :'crawler/settings.py'  <br />
spiders are available in 'crawler/spiders'


