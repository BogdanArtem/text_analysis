Python script for text analysis

DEPENDENCIES
Simple 'pip install pymorphy2' does not support ukrainian language. You shoud use 'pip install git+https://github.com/kmike/pymorphy2.git' instead in order to install pymorphy.

To add ukrainian dictionary run 'pip install pymorphy2-dicts-uk'

HOW TO USE IT
You can use this file as library or as a standalone software.
For library use you can simply run 'from text_analysis import *' to start using Text class of the library.
Or you can run the file via 'python3 text_analysis.py' and follow the instructions to analyse text in a standart mode.


NAME
    text_analysis

DESCRIPTION
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

DOCS
    class Text(builtins.object)
     |  Text(abs_path)
     |  
     |  Methods defined here:
     |  
     |  __init__(self, abs_path)
     |      At initialization creates list of ukraninian words and list of sentences. Takes absolute path to the file as an argument
     |  
     |  analyse(self)
     |      Returns number of words, number of sentences, average word length and average sentence length in tuple
     |  
     |  freq_dict(self, list_of_words=None)
     |      Returns key value pair of all ukrainian words and relative frequency if no other list is given
     |      {key(str):value(float)}
     |  
     |  get_parts_of_speach_freq(self)
     |      Returns key value pair of parts of speach frequency
     |  
     |  get_relative_lemma_freq(self)
     |      Returns key value pair of lemmas and relative frequency
     |      {key(str):value(float)}
     |  
     |  ----------------------------------------------------------------------
