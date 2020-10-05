import scrapy
from demo.items import DemoItem
from scrapy.loader import ItemLoader
class titleSpider(scrapy.Spider):
    """docstring for titleSpider."""
    name = 'spiderName'
    # start_urls = []

    # f = open("D:\CourseAutomation\scrapy\edx.txt", 'r')
    # for urls in f.readlines():
    #     start_urls.append(urls.strip())
    start_urls = ["https://www.edx.org/course/strategic-social-media-marketing-3"]

    def parse(self, response):
        main = response.xpath('//main[@id = "main-content"]')
        loader = ItemLoader(item = DemoItem(), selector = main)
        loader.add_value('courseLink',  str(response.request.url))
        loader.add_xpath('courseTitle', "//*[@id='course-header']/div[2]/div/div[1]/h1")
        loader.add_xpath('discription', "//*[@id='course-header']/div[2]/div/div[1]/div[1]/p")
        loader.add_xpath('subject', "//div/div/div/div[1]/div/div[1]/ul/li[5]/div[2]/a")
        loader.add_xpath('imageSrc', "//*[@id='course-header']/div[2]/div/div[2]/div/div/button/img/@src")
        loader.add_xpath('price', "//div/div/div/div[1]/div/div[1]/ul/li[3]/div[2]/p/span[1]")
        loader.add_xpath('certificate', "//*[@id='enroll-type-section']/span/h3/div")
        loader.add_xpath('provider', "//div/div/div/div[1]/div/div[1]/ul/li[4]/div[2]/a")
        loader.add_xpath('length', "//div/div/div/div[1]/div/div[1]/ul/li[1]/div[2]/span")
        loader.add_xpath('language', "//div/div/div/div[1]/div/div[1]/ul/li[7]/div[2]")
        loader.add_xpath('level', "//div/div/div/div[1]/div/div[1]/ul/li[6]/div[2]")
        loader.add_xpath('availableDate', '//div[2]/div/div[1]/div[3]/div[2]/div/div/div[2]/div[1]/a/div/span/div/small')
        loader.add_xpath('enrolledNo', "//*[@id='js-number-enrolled-label']/span")

        # yield {
        # 'title': main.xpath("//h1[@class = 'course-intro-heading mb-2']").extract_first()
        # }
        yield loader.load_item()
        self.log('saved title')
