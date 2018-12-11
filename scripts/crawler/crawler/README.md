
simple crawler using scrapy framework . scrapy have useful features like : avoiding duplicate urls, limitation on depth , defining request rate and ... . \n
you need to install scrapy :
`pip install scrapy`
and run the crawlers : 
<ul>
<li>`scrapy crawl hamshahri -o ham.json`</li>
<li>`scrapy crawl blogspider -o ham.json`</li>
<li>`scrapy crawl blogfa -o ham.json`</li>
<li>`scrapy crawl blogsky -o ham.json`</li>
<li>`scrapy crawl dorsablog -o ham.json`</li>
<li>`scrapy crawl mihanblog -o ham.json`</li>
<li>`scrapy crawl persianblog -o ham.json`</li>
</ul>

settings can be found in :'crawler/settings.py'  <br />
spiders are available in 'crawler/spiders'


