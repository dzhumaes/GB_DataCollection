import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    search = 'бизнес-аналитик'
    start_urls = [f'https://hh.ru/search/vacancy?area=1&search_field=name&search_field=company_name&search_field=description&text={search}&clusters=true&no_magic=true&ored_clusters=true&items_on_page=20&enable_snippets=true',
                  f'https://hh.ru/search/vacancy?area=2&search_field=name&search_field=company_name&search_field=description&text={search}&clusters=true&no_magic=true&ored_clusters=true&items_on_page=20&enable_snippets=true']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@data-qa='vacancy-serp__vacancy-title']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)



    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1/text()").get()
        salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        url = response.url
        city = response.xpath("//span[@data-qa='vacancy-view-raw-address']//text()").get()
        metro_name = response.xpath("//span[@class='metro-station']//text()").get()
        yield JobparserItem(name=name, salary=salary, url=url, city=city, metro_name=metro_name)
