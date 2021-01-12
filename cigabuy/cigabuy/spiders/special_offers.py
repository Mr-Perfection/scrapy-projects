import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html']
    start_urls = ['https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html']

    def parse(self, response):
        items = response.xpath("//div[@class='p_box_wrapper']/div")
        for item in items:
            yield {
                'title': item.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(item.xpath(".//a[@class='p_box_title']/@href").get()),
                'discounted_price': item.xpath(".//div[@class='p_box_price cf']/span[1]/text()").get(),
                'original_price': item.xpath(".//div[@class='p_box_price cf']/span[2]/text()").get(),
            }
