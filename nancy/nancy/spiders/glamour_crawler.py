import scrapy
from pathlib import Path


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
                "img": [(item[1])]
            }
            
            yield scraped_info
        
        