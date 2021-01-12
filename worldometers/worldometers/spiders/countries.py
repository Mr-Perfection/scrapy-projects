import scrapy
import logging

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info'] 
    start_urls = ['https://www.worldometers.info/coronavirus/#countries/']

    def parse(self, response):
        for row in response.xpath("//td/a[@class='mt_a']/ancestor::tr"):
            country_name = row.xpath(".//a/text()").get()
            data = {
                'country_name': country_name,
                'country_link': row.xpath(".//a/@href").get(),
                'total_covid_cases': row.xpath(".//td[3]/text()").get(),
            }
            # absolute_url = f"https://www.worldometers.info/coronavirus/{data['country_link']}"
            # absolute_url = response.urljoin(data['country_link'])
            # yield scrapy.Request(url=absolute_url)
            # yield data
            yield response.follow(url=data['country_link'], callback=self.parse_country,meta={'country_name': country_name})
    
    def parse_country(self, response):
        # logging.info(response.url)
        for row in response.xpath("//td/a[@class='mt_a']/ancestor::tr"):
            yield {
                'country_name': response.request.meta['country_name'],
                'city_name': row.xpath(".//a/text()").get(),
                'country_link': row.xpath(".//a/@href").get(),
                'total_covid_cases': row.xpath(".//td[3]/text()").get(),
            }



