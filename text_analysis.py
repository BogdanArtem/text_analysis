import os, pymorphy2, string
import re

ukrainian_letters = ['й','ц','у','к','е','н','г','ш','щ',
	'з','х','ї','ґ','є','ж','д','л','о','р','п','а','в','i',
	'ф','я','ч','с','м','и','т','ь','б','ю',"'","’"]

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
					pass
				else:
					return False
			return True


		# Open file for reading
		with open(self.path, mode='r', encoding='utf-8') as f:
			file_content = f.read()

			#Split file into sentences

			sentences = re.split('\.\s|\n|\?|\!',file_content)
			self.sentences = [sentence for sentence in sentences if sentence != '']

			#Split file into words
			self.all_words = []
			for sentence in self.sentences:
				words = sentence.split(' ')
				self.all_words.extend(words)

			# Creates a new list of cleaned words
			self.ukr_words = []
			for word in self.all_words:
				word = word.strip(string.punctuation+'«»')
				if is_ukr_word(word):
					self.ukr_words.append(word)


		# Create pymorphy2 instance for methods that use pymorphy2
		self.morph = pymorphy2.MorphAnalyzer(lang='uk')

		#Num of words
		self.num_words = len(self.all_words)

		#Num of sentences
		self.num_sent = len(self.sentences)


	def analyse(self):
		"""Returns number of words, number of sentences, average word length and average sentence length in tuple """

		#Average length of word
		total_length = 0
		for word in self.ukr_words:
			total_length += len(word)
		av_word_len = total_length/self.num_words

		#Average length of sentence
		total_length = 0
		for sentence in self.sentences:
			total_length += len(sentence)
		av_sent_len = total_length/self.num_words

		return self.num_words, self.num_sent, av_word_len, av_sent_len


	def freq_dict(self, list_of_words = None):
		"""Returns key value pair of all ukrainian words and relative frequency if no other list is given
		{key(str):value(float)}
		"""
		if not list_of_words:
			list_of_words = self.ukr_words

		unique_words = set(list_of_words)
		# num_of_un_words = len(unique_words)
		freq_dict = {}
		for un_word in unique_words:
			freq_dict[un_word.lower()] = list_of_words.count(un_word)

		# Sort by frequency
		sorted_words = sorted(freq_dict, key=freq_dict.get)
		sorted_words.reverse()

		new_freq_dict = {}
		for word in sorted_words:
			new_freq_dict[word] = (freq_dict[word]/self.num_words)*100
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

	# Helper functions
	def dict_to_text(dictionary):
		""" Transform dictionary to str for readability """
		text = ''
		for key in dictionary:
			text += f'{key}:{dictionary[key]}% \n'
		return text


	def create_report(root_path, files):
		"""Creates report in the folder"""
		report = ''
		for file in files:

			# Path to the file
			f_path = os.path.join(path, file)

			text = Text(f_path)

			# Get main charcteristics of text
			num_words, num_sent, av_word_len, av_sent_len = text.analyse()

			report += '='*100+'\n'
			report += f'{file}\n'
			report += '='*100+'\n'*2
			report += f"Number of words: {num_words}, number of sentences: {num_sent}, average word length: {av_word_len}, average sentence length: {av_sent_len}\n\n"
			report += f'============================= Frequencies ================================= \n'
			report += dict_to_text(text.freq_dict()) + '\n'
			report += f'============================= Lemma Frequencies ================================= \n\n'
			report += dict_to_text(text.get_relative_lemma_freq()) + '\n'
			report += f'============================= Parts of speach ================================= \n\n'
			report += dict_to_text(text.get_parts_of_speach_freq()) + '\n'

		with open(os.path.join(path,'report.txt'), 'w', encoding='utf-8') as f:
			f.write(report)


	path = os.getcwd()
	# Walk through all leaves in the root tree
	tree = os.walk(path)

	# Create report for each text
	for i in tree:
		path, folders, files = i
		files_c = files[:]
		for file in files_c:
			if not file.endswith('.txt'):
				files.remove(file)

		if len(files):
			create_report(path, files)




