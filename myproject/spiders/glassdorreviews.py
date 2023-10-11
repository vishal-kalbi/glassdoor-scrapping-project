import scrapy
from myproject.items import *
from itertools import cycle

class GlassdorreviewsSpider(scrapy.Spider):
    name = "glassdorreviews"
    allowed_domains = ["glassdoor.com"]
    start_urls = ['https://www.glassdoor.co.in/Reviews/TCS-Technologies-Reviews-E434965.htm']
    
   
    
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67',
        }

        for url in self.start_urls:
          
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        for review in response.css('.noBorder'):
            item = GlassdoorTcsReview()
            item['review_title'] = review.css('h2 a::text').get()
            item['rating'] = review.css('span.review-details__review-details-module__overallRating::text').get()
            item['pros'] =  review.css('p.review-details__review-details-module__green::text').get()
            item['cons'] = review.css('p.review-details__review-details-module__red::text').get()
            item['date'] = review.css('span.review-details__review-details-module__reviewDate::text').get()

            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
           
           # Set the proxy in the meta field
            yield response.follow(next_page, self.parse)
