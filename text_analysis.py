# Задание по обработке корпуса медицинской тематики 
# 1. Создать программу, которая будет позволять: 
# a. Загружать файлы из выбранной директории 
# b. Выводить следующую информацию: количество слов, предложений, 
# средняя длина предложений, средняя длина слов. 
# c. Выводить частоту (относительную частоту) по всем словам, а также 
# по леммам 
# d. Выводить частотные списки слов в зависимости от части речи (сущ, 
# глагол или др) 
# e. Проводить поиск слов в файлах, в результате которого будет 
# показано слово, предложение в котором оно встретилось и в каком 
# файле.

import os, pymorphy2

ukrainian_letters = ['й','ц','у','к','е','н','г','ш','щ',
	'з','х','ї','ґ','є','ж','д','л','о','р','п','а','в','і',
	'ф','я','ч','с','м','и','т','ь','б','ю']


def analyse(file):
	#Perform text analysis
	#Returns dictionary


	#Split file into sentences
	sentences = file.split('.')

	#Split file into words
	all_words = []
	for sentence in sentences:
		words = sentence.split(' ')
		all_words.extend(words)

	def is_ukr_word(word):
		#Check if the word is ukrainian
		#Returns Bool value

		letters = list(word)
		for letter in letters:
			if letter.lower() in ukrainian_letters:
				return True
			else:
				pass
		return False

	def clean_word(word):
		#Remove all symbols except ukr letters
		#Returns string

		letters = list(word)
		for letter in letters:
			if letter.lower() in ukrainian_letters:
				letter = letter.lower()
			else:
				letters.remove(letter)
		return "".join(letters)

	def frequency_dict(list_of_words):
		#Dictionary of words frequency
		unique_words = set(list_of_words)
		num_of_un_words = len(unique_words)
		freq_dict = {}
		for un_word in unique_words:
			freq_dict[un_word] = list_of_words.count(un_word)

		# Sort by frequency
		sorted_words = sorted(freq_dict, key=freq_dict.get)
		sorted_words.reverse()
		new_freq_dict = {}
		for word in sorted_words:
			new_freq_dict[word] = (freq_dict[word]/num_of_un_words)*100
		return new_freq_dict

	# Creates a new list of cleaned words
	new_words = []
	for word in all_words:
		if is_ukr_word(word):
			new_words.append(clean_word(word))

	#Num of words
	num_words = len(new_words)

	#Num of sentences
	num_sent = len(sentences)

	#Average length of word
	total_length = 0
	for new_word in new_words:
		total_length += len(new_word)
	av_word_len = total_length/num_words

	#Average length of sentence
	total_length = 0
	for sentence in sentences:
		total_length += len(sentence)
	av_sent_len = total_length/num_words
	
	words_dict = frequency_dict(new_words)

	#Dictionary of words frequency using lemmas
	morph = pymorphy2.MorphAnalyzer(lang='uk')

	lemmas = []
	for new_word in new_words:
		p = morph.parse(new_word)[0]
		lemmas.append(p.normal_form)

	lemmas_dict = frequency_dict(lemmas)

	#Dictionary of parts of speech
	#/Users/artembogdan/Programming_projects/KhPI_parsing/Moderate - Bogdan Artem 219e

	parts_of_speech = {}
	for word in new_words:
		p = morph.parse(word)[0]

		if p.tag.POS in parts_of_speech:
			parts_of_speech[p.tag.POS] += 1
		else:
			parts_of_speech[p.tag.POS] = 0

	for keyvalue in parts_of_speech:
		parts_of_speech[keyvalue] = (parts_of_speech[keyvalue]/num_words)*100

	print(f'''
		Number of words: {num_words}
		Number of sentences: {num_sent}
		Average word length: {av_word_len}
		Average sentence length: {av_sent_len}
		====================================================
		====================================================
		====================================================

		     Relative frequency of words 

		====================================================
		====================================================
		====================================================

		{words_dict}

		====================================================
		====================================================
		====================================================

		     Relative frequency of words using lemmas 

		====================================================
		====================================================
		====================================================

		{lemmas_dict}

		====================================================
		====================================================
		====================================================

		     Relative frequency of parts of speach 

		====================================================
		====================================================
		====================================================

		{parts_of_speech}
	''')

# Load files from your directory 
texts_path = input("Enter absolute path to folder with your texts > ")
os.curdir = texts_path

filenames = os.listdir(os.curdir)
for file in filenames:
	filepath = os.path.join(os.curdir,file)
	with open(filepath, mode='r', encoding='utf-8') as f:
		file_content = f.read()
		print(file)
		analyse(file_content)
		input()
