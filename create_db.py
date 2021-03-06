#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import os


def f_create_table_db(file_db:str):
	#
	# Создание таблицы
	# name_book - название книги, author - автор стихов, 
	# title_stih - название стиха, stih_list - стихотворение, date_stih - дата написания стиха
	
	if not os.path.exists(file_db):  # провенрка существует ли файл
		try:
			conn = sqlite3.connect(file_db, check_same_thread=False)  # создание db
			cursor = conn.cursor()
			cursor.execute("""CREATE TABLE poems
				(poem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				book text, 
				author text, 
				title_stih text, 
				stih text, 
				date_stih text)""")
			conn.commit()
			print('database created!!!')

		except sqlite3.Error as e:
			print(f'Error: {e}')
			
		finally:
			if conn:
				conn.close()





if __name__ == '__main__':
	print('(-_-)')
else:
	name_db = 'poems_db.db'
	cur_dir = 'sqlite_db'
	file_db = os.path.join(cur_dir, name_db)

	f_create_table_db(file_db)
