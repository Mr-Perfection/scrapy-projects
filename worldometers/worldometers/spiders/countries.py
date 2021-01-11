import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info'] 
    start_urls = ['https://www.worldometers.info/coronavirus/#countries/']

    def parse(self, response):
        countries = response.xpath("//td/a").css(".mt_a::text").getall() # alternatively you can do //tr/td/a[contains(@href, "country")] for fun
        yield {
            'countries': countries,
        }
