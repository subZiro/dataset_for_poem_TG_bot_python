#!/usr/bin/python
# -*- coding: utf-8 -*-


# read txt book 
import os
import re
#import pandas as pd




def f_read_files_in_folder(foldername:str):
	# read txt files in folder
	
	if not os.path.exists(foldername):
		os.makedirs(foldername)
		
	folder = os.listdir(foldername)
	files_list = []
	for f in folder:
			if f[-4:] == '.txt':
				f = os.path.join(foldername, f)
				files_list.append(f)
		
	return files_list


def f_read_txt(file_name:str):
	# read txt book 

	book_list = []

	with open(file_name, encoding="utf8", errors='ignore') as file:
		for line in file:
			
			if line[:22] == '                      ':
				#line = str(line).rstrip().split('\n')
				line = ' '*4 + line[22:-1]
			else:
				line = re.sub("^\s+|\n|\r|\t|\s+$", '', line)

			if line:
				book_list.append(line)
		
	return book_list


def f_correct_book(array:list):
	# приведение считанных данных к формату 
	# ['name_book', 'author', 'title_stih', 'stih', 'date_stih', 'title_stih', 'stih', 'date_stih',...]
	result = []
	sum_s = ''
	array[0],array[1] = array[1], array[0]
	#result.append(array[0])

	for i in range(len(array)):

		line = array[i]
		line_d = len([x for x in line if x.isdigit()])
	
		if line.isupper() or line == '* * *' or line_d >= 4:
			if sum_s:
				result.append(sum_s[:-1])
				sum_s = ''
			result.append(line)

		else:
			sum_s += line + '\n'

	if sum_s:
		result.append(sum_s)


	return result


def f_array_to_BATSD(array:list):
	# принимает список и возвращает 
	# списки 'name_book', 'author', 'title_stih', 'date_stih', 'stih_list'
	name_book, author, title_stih, date_stih, stih_list = [], [], [], [], []
	
	#--add stih_list--#
	stih_list = [elem for elem in array[3:] if len(elem) > 50]

	#--add name_book--#
	name_book = [array[0] for _ in range(len(stih_list))]

	#--add author_stih--#
	author = [array[1] for _ in range(len(stih_list))]


	'''
	name_book = [array[0] for _ in range(len(stih_list))]
	author = [array[1] for _ in range(len(stih_list))]
	title_stih = [array[array.index(elem) - 1] for elem in stih_list]
	'''

	#--add title--#
	for i in range(len(stih_list)):
		stih_index = array.index(stih_list[i])
			
		if array[stih_index-1] in stih_list:
			title_stih.append('* * *')
		
		else: 
			d_line = len([x for x in array[stih_index-1] if x.isdigit()]) >= 4
			if d_line:
				title_stih.append('* * *')
			else:
				title_stih.append(array[stih_index-1])


	#--add date to stih--#
	for i in range(len(stih_list)):
		stih_index = array.index(stih_list[i])
		
		if stih_index+1 >= len(array):
			date_stih.append('19**')
		
		else:
			if array[stih_index+1] in title_stih or array[stih_index+1] in stih_list:
				date_stih.append('19**')
			else:
				date_stih.append(array[stih_index+1])
	
	#--replace <> in date_stih--#
	date_stih = [x.replace('>', '').replace('<', '') for x in date_stih]


	return name_book, author, title_stih,  date_stih, stih_list


def f_array_stih(array:list):
	# array of stih

	#--add stih_list--#
	stih_list = [elem for elem in array[3:] if len(elem) > 50]
	print(len(stih_list))
	#poem_book = ['name_book', 'author', 'title_stih', 'stih', 'date_stih']
	result = [['', '', '', '', '']] * len(stih_list)

	for i in range(len(stih_list)):
		for j in range(len(result[i])):
			result[i][j] = 

	print(result)










# add txt file in folder to read list
files_list = f_read_files_in_folder('txt_books')

print(files_list)
name_book = []
author = []
title_stih = []
date_stih = []
stih_list = []


# read txt file in files list
for file in files_list:
	txt_l = f_read_txt(file)
	txt_l = f_correct_book(txt_l)

	f_array_stih(txt_l)

	'''
	if txt_l[0] not in name_book:
		n, a, t, d, s = f_array_to_BATSD(txt_l)

	name_book.extend(n)
	author.extend(a)
	title_stih.extend(t)
	date_stih.extend(d)
	stih_list.extend(s)
	'''

	#os.remove(file)





#print(name_book)
#print(author)
#print(title_stih)
#print(date_stih)

'''
for stih in stih_list:
	print(stih, end='\n\n')
'''






#book = f_correct_book(book_li)

#name_book, author, title_stih, date_stih, stih_list = f_array_to_BATSD(book)



'''
poem_book = ['name_book', 'author', 'title_stih', 'date_stih', 'stih']

'''



