
simple crawler using scrapy framework . scrapy have useful features like : avoiding duplicate urls, limitation on depth , defining request rate and ... . \n
you need to install scrapy :
`pip install scrapy`
and run the crawlers :  <br /> <br />

`scrapy crawl hamshahri -o ham.json`  <br />
`scrapy crawl blogspider -o ham.json`  <br />
`scrapy crawl blogfa -o ham.json`  <br />
`scrapy crawl blogsky -o ham.json`  <br />
`scrapy crawl dorsablog -o ham.json`  <br />
`scrapy crawl mihanblog -o ham.json`  <br />
`scrapy crawl persianblog -o ham.json`  <br /> <br />

settings can be found in :'crawler/settings.py'  <br />
spiders are available in 'crawler/spiders'


