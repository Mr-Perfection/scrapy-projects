import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        print(response.body)
        resp = json.loads(response.body)
        quotes = resp.get('quotes')
        for quote in quotes:
            yield {
                'text': quote.get('text'),
                'author': quote.get('author').get('name'),
                'tags': quote.get('tags'),
            }
        has_next = resp.get('has_next')
        if has_next:
            next_page_num = resp.get('page')+1
            yield scrapy.Request(url=f"http://quotes.toscrape.com/api/quotes?page={next_page_num}",callback=self.parse)

