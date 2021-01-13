# scrapy-projects

### Setup
- brew install --cask anaconda
```sh
# add this in your .bash_profile or .zshrc
export PATH="/usr/local/anaconda3/bin:$PATH"
```

```console
$ conda install -c conda-forge scrapy pylint autopep8 -y
```

### CSS Debugger
https://try.jsoup.org/


### CSS Selector Examples
```console
// this selects <li data-identifier="5">
.css([data-identifier]) 
// this selects prefix of 'https' in href of <a>
.css(a[href^='https']) 
// this selects all <a> that contains 'google' in href
.css(a[href*='google']) 
// this selects ends with'.fr' in href
.css(a[href$='.fr']) 
// this selects inbetween string with 'goog' in href
.css(a[href~='goog']) 

// this selects p and span id='section' in <div class="google"><p></p><span id="section"></span></div>
.css(div.google p, #section)

// gets p that are the direct children of div
.css(div > p)

// gets p that is immediately after div
// <div class="mama"></div><p> hello </p>
.css(div.mama + p)

// gets the 1st and 3rd elements
.css(li:nth-child(1), li:nth-child(3))
.css(li:nth-child(odd)

// ~ (general sibling) will get all the <p>s inside corgi class as well as p immediately after corgi class.
.css(div.corgi ~ p)
```

### XPath Debugger
https://scrapinghub.github.io/xpath-playground/

```
.xpath(//div[@class='intro' or @class='outro']/p/text())
//a[ends-with(@href, 'fr')] # only supports in xpath 2.0
//a[contains(@href, 'amazon')]
//ul[@id='items']/li[1 or 4] # get all li 4 elements
//ul[@id='items']/li[position()=1 or position()=4] # get 1st and 4th elements
//ul[@id='items']/li[position()>1] # get all li greater than 1st in order
//p[@id='hola']/parent::node() # get the parent node of p
//p[@id='hola']/ancestor::node()
//p[@id='hola']/preceding::node() # all the elements that don't include ancestor
//p[@id='hola']/preceding-sibling::node()

# descendents
//p[@id='hola']/following::node()
//p[@id='hola']/following-sibling::node()
//p[@id='hola']/decendent::node()
```

- Run this command to get the output
```console
scrapy crawl countries -o covid_cases.[json | csv | xml...]
```

### How to get project started?
- `scrapy startproject [project-name]`
- `cd [project-name] && scrapy genspider [spider-name] url (without https:// or http://)`

### How to Debug
https://docs.scrapy.org/en/latest/topics/debug.html

```sh
scrapy parse --spider=special_offers -c [method_name] [URL] # check scrapy parse -help for more details
```

inspect_response(response, self)

* Create a runner file, set break points in spider file, and Run > Start Debugging
```py
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from worldometers.spiders.countries import CountriesSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(CountriesSpider)
process.start()
```