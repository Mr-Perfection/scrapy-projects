import scrapy
from scrapy_splash import SplashRequest

class QuotesToScrapeSpider(scrapy.Spider):
    name = 'quotes_to_scrape'
    allowed_domains = ['quotes.toscrape.com']
    url = 'http://quotes.toscrape.com'
    script = '''
    function main(splash, args)
        url = args.url
        assert(splash:go(url))
        splash:set_viewport_full()
        return splash:html()
    end

    '''
    def start_requests(self):
        yield SplashRequest(url='http://quotes.toscrape.com/js',endpoint="execute", args={
            'lua_source': self.script
        })
    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            yield {
                'text': quote.xpath(".//span[@class='text']/text()").get(),
                'author': quote.xpath(".//small/text()").get(),
                'tags': quote.xpath(".//a[@class='tag']/text()").getall(),
            }
        
        relative_href = response.xpath("//ul/li/a/@href").get()
        if relative_href:
            # absolute_url = f"{self.url}{relative_href}"
            yield SplashRequest(url=response.urljoin(relative_href), callback=self.parse, args={
            'lua_source': self.script
            })

        
