# import scrapy
# from demo.items import DemoItem
# from scrapy.loader import ItemLoader
# class titleSpider(scrapy.Spider):
#     """docstring for titleSpider."""
#     name = 'course'
#     start_urls = [
#     'https://www.edx.org/course/18th-century-opera-handel-mozart'
#     ]
#
#     def parse(self, response):
#         div = response.xpath('//div[@class = "row no-gutters w-100"]')
#         l = ItemLoader(item = DemoItem(), selector = div)
#         l.add_xpath('title', "//div[@class = 'col-lg-7 p-1']/h1")
#         # yield {
#         # 'title': div.xpath("//h1[@class = 'course-intro-heading mb-2']").extract_first()
#         # }
#         yield l.load_item()
#         self.log('saved title')
