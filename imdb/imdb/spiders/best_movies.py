import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm']

    rules = (
        # restrict_xpaths={}
        Rule(LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        subtext = response.xpath("//div[@class='subtext']/a/text()").getall()
        genre = ','.join(subtext[:-1]) if len(subtext) > 1 else ''
        item = {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'duration': response.xpath("normalize-space((//time)[1]/text())").get(), # or ("//div[@class="subtext"]/time").strip()
            'genre': genre,
            'release_date': subtext[-1].strip()
        }
        return item
