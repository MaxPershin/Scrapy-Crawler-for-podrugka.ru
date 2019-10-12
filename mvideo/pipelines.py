# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class MvideoPipeline(object):

	def __init__(self):
		print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW INIT!!!! \n \n \n \n \n')
		self.connect_to_database()
		self.create_table()

	def connect_to_database(self):
		self.conn = sqlite3.connect('podruzhka.db')
		self.curr = self.conn.cursor()

	def create_table(self):
		self.curr.execute('DROP TABLE IF EXISTS podruzhka_table')
		self.curr.execute('CREATE TABLE podruzhka_table(name text, price text, pic text)')

	def put_to_database(self, item):
		self.curr.execute('INSERT INTO podruzhka_table VALUES (?,?,?)',(
			item['item_name'],
			item['item_price'],
			item['item_pic']
			))

		self.conn.commit()

	def process_item(self, item, spider):
		self.put_to_database(item)
		return item