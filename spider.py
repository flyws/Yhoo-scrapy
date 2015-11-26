import scrapy
import re
from scrapy.selector import Selector
from stockmarket.items import StockmarketItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
import time


class PriceSpider(CrawlSpider):
	name = 'stockmarket'
	allowed_domains = ['nasdaq.com']
	start_urls = ['http://www.nasdaq.com/symbol/yhoo/historical']

	def parse(self,response):
		driver = webdriver.Chrome()
		driver.get(response.url)
		select = Select(driver.find_element_by_id('ddlTimeFrame'))

		# select by visible text
		abc = select.select_by_visible_text('1 Year')
		sites = [] 
		# key step
		time.sleep(10)
		sites = driver.find_elements_by_xpath('//*[@id="quotes_content_left_pnlAJAX"]/table/tbody/tr')
		items = []

		for i in sites:
			item = StockmarketItem()
			try:
				item['stock_date'] = i.find_elements_by_xpath('.//td[1]')[0].text.strip()
				item['stock_open'] = i.find_elements_by_xpath('.//td[2]')[0].text.strip()
				item['stock_high'] = i.find_elements_by_xpath('.//td[3]')[0].text.strip()
				item['stock_low'] = i.find_elements_by_xpath('.//td[4]')[0].text.strip()
				item['stock_close'] = i.find_elements_by_xpath('.//td[5]')[0].text.strip()
				item['stock_volume'] = i.find_elements_by_xpath('.//td[6]')[0].text.strip()

				items.append(item)
			except:
				WebDriverWait(i,10)
				continue

		driver.quit()
		return items
