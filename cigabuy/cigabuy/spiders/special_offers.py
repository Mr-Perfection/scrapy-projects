import scrapy
import logging

DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}
class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html']
    def start_requests(self):
        yield scrapy.Request(url='https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html', callback=self.parse, headers=DEFAULT_HEADERS)
        
    def parse(self, response):
        items = response.xpath("//div[@class='p_box_wrapper']/div")
        for item in items:
            yield {
                'title': item.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(item.xpath(".//a[@class='p_box_title']/@href").get()),
                'discounted_price': item.xpath(".//div[@class='p_box_price cf']/span[1]/text()").get(),
                'original_price': item.xpath(".//div[@class='p_box_price cf']/span[2]/text()").get(),
                'user_agent': response.request.headers['User-Agent'],
            }

        next_page = response.xpath("//a[@class='nextPage']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers=DEFAULT_HEADERS)
            
