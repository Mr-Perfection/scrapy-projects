import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0'
    rules = (
        # restrict_xpaths={}
        Rule(LinkExtractor(restrict_xpaths=["//td[@class='titleColumn']/a", "//h3[@class='lister-item-header']/a"]), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[1]"))
    )

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&title_type=tvShort&ref_=adv_explore_rhs', headers={
            'User-Agent': self.user_agent,
        })
    
    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent

    def parse_item(self, response):
        print(response.url)
        subtext = response.xpath("//div[@class='subtext']/a/text()").getall()
        genre = ','.join(subtext[:-1]) if len(subtext) > 1 else ''
        item = {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'duration': response.xpath("normalize-space((//time)[1]/text())").get(), # or ("//div[@class="subtext"]/time").strip()
            'genre': genre,
            'release_date': subtext[-1].strip(),
            'user-agent': self.user_agent,
        }
        return item
