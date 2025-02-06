import scrapy
import json


class ShoesScrapeSpider(scrapy.Spider):
    name = "scrapy_shoes"
    allowed_domains = ["academy.com"]
    start_urls = ["https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes"]

    def parse(self, response):
        product_data = {}
        product_data["name"] = response.css("#pdp240TitleWrapper > h1::text").get().strip()
        product_data['price'] = response.css("#pdpContentWrapper > section.stickySectionWrapper--UWcmx > div.d-flex.flex-row.justify-content-between.flex-wrap-reverse.align-items-center.priceRatingSpacing--how5h > div.d-flex.flex-column > div > div > span::text").get()
        product_data["colour"] = response.css("#pdpContentWrapper > section:nth-child(2) > div > div.headerWrapper--ycKHq.horizontalBorder--Npbxe > div > div.swatchWrapperText--XtAXQ > span > span.swatchName--KWu4Q::text").get()
        product_data['availableColours'] = response.css('#swatch-drawer-content::text').getall()
        product_data["reviews_count"] = response.css("#pdpContentWrapper > section.stickySectionWrapper--UWcmx > div.d-flex.flex-row.justify-content-between.flex-wrap-reverse.align-items-center.priceRatingSpacing--how5h > div.ratingWrapper--KQppb > span > button").get()
        product_data["reviews_score"] = response.css("span[data-auto-id='#pdpContentWrapper > section.stickySectionWrapper--UWcmx > div.d-flex.flex-row.justify-content-between.flex-wrap-reverse.align-items-center.priceRatingSpacing--how5h > div.ratingWrapper--KQppb > span > button']").get()

        with open("output.json", "w") as f:
            json.dump(product_data, f, indent=4)

        yield product_data
