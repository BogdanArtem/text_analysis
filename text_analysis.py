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
import re

ukrainian_letters = ['й','ц','у','к','е','н','г','ш','щ',
	'з','х','ї','ґ','є','ж','д','л','о','р','п','а','в','i',
	'ф','я','ч','с','м','и','т','ь','б','ю',]

class Text(object):
	"""docstring for Text"""
	def __init__(self, abs_path):
		"""At initialization creates list of ukraninian words and list of sentences. Takes absolute path to the file as an argument"""
		self.path = abs_path

		#Set current dirrectory
		os.curdir = self.path

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
			letters = list(word.strip())
			for letter in letters:
				if letter.lower() in ukrainian_letters:
					letter = letter.lower()
				else:
					letters.remove(letter)
			return "".join(letters)


		# Open file for reading
		with open(self.path, mode='r', encoding='utf-8') as f:
			file_content = f.read()

			#Split file into sentences

			sentences = re.split('\.\s|\n|\?|\!',file_content)
			self.sentences = [sentence for sentence in sentences if sentence != '']

			#Split file into words
			all_words = []
			for sentence in self.sentences:
				words = sentence.split(' ')
				all_words.extend(words)

			# Creates a new list of cleaned words
			self.ukr_words = []
			for word in all_words:
				if is_ukr_word(word):
					self.ukr_words.append(clean_word(word))


		# Create pymorphy2 instance for methods that use pymorphy2
		self.morph = pymorphy2.MorphAnalyzer(lang='uk')


	def analyse(self):
		"""Returns number of words, number of sentences, average word length and average sentence length in tuple """

		#Num of words
		num_words = len(self.ukr_words)

		#Num of sentences
		num_sent = len(self.sentences)

		#Average length of word
		total_length = 0
		for word in self.ukr_words:
			total_length += len(word)
		av_word_len = total_length/num_words

		#Average length of sentence
		total_length = 0
		for sentence in self.sentences:
			total_length += len(sentence)
		av_sent_len = total_length/num_words

		#Save num_words for get_parts_of_speach_freq()
		self.num_words = num_words

		return num_words, num_sent, av_word_len, av_sent_len


	def freq_dict(self, list_of_words = None):
		"""Returns key value pair of all ukrainian words and relative frequency if no other list is given
		{key(str):value(float)}
		"""
		if not list_of_words:
			list_of_words = self.ukr_words

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


	def get_relative_lemma_freq(self):
		"""Returns key value pair of lemmas and relative frequency
		{key(str):value(float)}
		"""
		lemmas = []
		for word in self.ukr_words:
			p = self.morph.parse(word)[0]
			lemmas.append(p.normal_form)


		lemmas_dict = self.freq_dict(list_of_words = lemmas)
		return lemmas_dict


	def get_parts_of_speach_freq(self):
		"""Returns key value pair of parts of speach frequency"""
		parts_of_speech = {}
		for word in self.ukr_words:
			p = self.morph.parse(word)[0]

			if p.tag.POS in parts_of_speech:
				parts_of_speech[p.tag.POS] += 1
			else:
				parts_of_speech[p.tag.POS] = 0

		for keyvalue in parts_of_speech:
			parts_of_speech[keyvalue] = (parts_of_speech[keyvalue]/self.num_words)*100
		return parts_of_speech



if __name__ == '__main__':

	path = input('Please, enter absolute path to your .txt file > ')
	text = Text(path)

	print((text.analyse()))
	num_words, num_sent, av_word_len, av_sent_len = text.analyse()

	print("="*100)
	print(f"Number of words: {num_words}, number of sentences: {num_sent}, average word length: {av_word_len}, average sentence length {av_sent_len}")
	print("="*100)

	print(text.freq_dict())
	print("="*100)

	print(text.get_relative_lemma_freq())
	print("="*100)

	print(text.get_parts_of_speach_freq())
	print("="*100)









