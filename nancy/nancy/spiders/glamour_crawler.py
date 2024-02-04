from urllib.parse import urlparse
from urllib.request import Request
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from pathlib import Path, PurePosixPath


class GlamourImageSpider (scrapy.Spider):
    name = "glamour_crawler"
    allowed_domains = ["www.glamour.com/gallery/best-valentines-day-nail-ideas"]
    # allowed_domains = ["www.glamour.com"]
    start_urls = ["https://www.glamour.com/gallery/best-valentines-day-nail-ideas/"]
    # start_urls = ["https://www.glamour.com/"]
    custom_settings = {
            'FEEDS': { 'data/vals_nails.json': { 'format': 'json', 'overwrite':True}},
            # 'FEED_URI' : 'data/vals_nails.json',
        }
    
    def parse(self, response, **kwargs):
        title = response.css(".GallerySlideCaptionHedText-iqjOmM.jwPuvZ::text").extract() #image titles
        img = response.css(".responsive-image__image::attr(src)").extract() #image source
        
        for item in zip(title, img):
            scraped_info = {
                "title": item[0],
                "image_urls": [item[1]]
            }
            
            yield scraped_info
        
class MyImagesPipeline(ImagesPipeline):
    
    def file_path(self, request, response=None, info=None, item=None):
        # return request.meta.get('title')
        return "full/" + item['title'] + ".jpg"
    # def get_media_requests(self, item, info):
    #     image_urls = item['image_urls']
    #     meta = {'filename': item['title']}
    #     yield Request(url=image_urls, meta=meta)
        