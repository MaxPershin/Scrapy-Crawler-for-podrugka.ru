# -*- coding: utf-8 -*-
import scrapy
from ..items import MvideoItem 

class MvideospiderSpider(scrapy.Spider):
	name = 'mvideoSpider'
	start_urls = ['https://www.podrygka.ru/catalog/ukhod/country-is-724e87fa98bf8a6a69816a93f4100878/?gclid=Cj0KCQjw84XtBRDWARIsAAU1aM3rAhxe98pVtYn0WRkLDwJUdc0XePiz7a6MHBCzFCG-dmiHSjOpjgMaAsv_EALw_wcB']
	counter = 2

	def parse(self, response):
		all_items = response.css('.col-md-3')


		items = MvideoItem()


		for each in all_items:
			if each.css('.products-list-item__title::text').get() == None:
				return
				
			items['item_name'] = each.css('.products-list-item__title::text').get()
			items['item_price'] = each.css('.value--current span::text').get()
			items['item_pic'] = 'www.podrygka.ru' + each.css('img::attr(src)').get()

			print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', MvideospiderSpider.counter)

			yield items

		next_page = 'https://www.podrygka.ru/catalog/ukhod/country-is-724e87fa98bf8a6a69816a93f4100878/?gclid=Cj0KCQjw84XtBRDWARIsAAU1aM3rAhxe98pVtYn0WRkLDwJUdc0XePiz7a6MHBCzFCG-dmiHSjOpjgMaAsv_EALw_wcB&PAGEN_1={}'.format(MvideospiderSpider.counter)

		MvideospiderSpider.counter += 1
		yield response.follow(next_page, callback= self.parse)