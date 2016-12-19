from scrapy import cmdline
cmdline.execute("scrapy crawl jianshu".split()).encode('utf-8')