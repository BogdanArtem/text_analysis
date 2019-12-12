Python script for text analysis


DEPENDENCIES

Before working with this script you should have Python 3.7 installed.
To install pymorphy2 run 'pip install git+https://github.com/kmike/pymorphy2.git'
To add ukrainian dictionary run 'pip install pymorphy2-dicts-uk'

HOW TO USE IT

You can use this file as library or as a standalone software.
For library use you can simply run 'from text_analysis import *' to start using Text class of the library.
Or you can run the file via 'python3 text_analysis.py' and follow the instructions to analyse text in a standart mode.

Before running the script place it in the root folder of your texts as shown below

    ── Texts
    │   ├── Complex
    │   │   ├── text1.txt
    │   │   ├── text2.txt
    │   │   ├── text3.txt
    │   │   ├── text4.txt
    │   │   └── text5.txt
    │   ├── Easy
    │   │   ├── New_folder
    │   │   │   ├── text1.txt
    │   │   │   └── text2.txt
    │   │   ├── text1.txt
    │   │   ├── text2.txt
    │   │   ├── text3.txt
    │   │   ├── text4.txt
    │   │   └── text5.txt
    │   ├── Moderate
    │   │   ├── text1.txt
    │   │   ├── text2.txt
    │   │   ├── text3.txt
    │   │   ├── text4.txt
    │   │   └── text5.txt
    │   └── text_analysis.py

After script execution you will receive a report for each folder with .txt files like shown below

    ├── Texts
    │   ├── Complex
    │   │   ├── report.txt
    │   │   ├── text1.txt
    │   │   ├── text2.txt
    │   │   ├── text3.txt
    │   │   ├── text4.txt
    │   │   └── text5.txt
    │   ├── Easy
    │   │   ├── New_folder
    │   │   │   ├── report.txt
    │   │   │   ├── text1.txt
    │   │   │   └── text2.txt
    │   │   ├── report.txt
    │   │   ├── text1.txt
    │   │   ├── text2.txt
    │   │   ├── text3.txt
    │   │   ├── text4.txt
    │   │   └── text5.txt
    │   ├── Moderate
    │   │   ├── report.txt
    │   │   ├── text1.txt
    │   │   ├── text2.txt
    │   │   ├── text3.txt
    │   │   ├── text4.txt
    │   │   └── text5.txt
    │   └── text_analysis.py



Example of report for folder with 1 .txt file 

    ====================================================================================================
    File_name.txt
    ====================================================================================================

    Number of words: 3536, number of sentences: 164, average word length: 3.2799773755656108, average sentence length: 6.904694570135747

    ============================= Frequencies ================================= 
    та:2.48868778280543% 
    що:1.9513574660633484% 
    спогади:1.753393665158371% 
    дитинства:1.1312217194570136% 
    на:1.0463800904977374% 
    не:1.0463800904977374% 

    ============================= Lemma Frequencies ================================= 

    з:2.6866515837104075% 
    та:2.48868778280543% 
    у:2.3755656108597285% 
    спогад:2.262443438914027% 
    що:2.007918552036199% 
    вони:1.498868778280543% 
    мати:1.244343891402715% 

    ============================= Parts of speach ================================= 

    NOUN:19.145927601809955% 
    CONJ:6.730769230769231% 
    PRCL:4.581447963800905% 
    ADJF:4.779411764705882% 
    VERB:10.690045248868778% 
    PREP:6.702488687782806% 
    NPRO:5.203619909502263% 
    ADVB:2.516968325791855% 
    None:0.6787330316742082% 
    NUMR:0.19796380090497737% 
    GRND:0.056561085972850686% 
    INTJ:1.0180995475113122% 
    PRED:0.0% 

For standalone usage of Text class you can check the docs 

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
