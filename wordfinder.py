"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    
    """
    Counts words found in a file and returns a random word that is read from the file
    
    
    >>> wf = WordFinder('words.txt')
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
       
    
    """
    
    
    
    def __init__(self, file_path):
        
        
        self.file = open(file_path, 'r')
        
        self.text = self.file.read()
        
        self.file.close()
        
        self.text = self.text.replace("\n", " ")
        
        self.text_list = list(self.text.split(" "))
        
        return f"{len(list)} words read"
        
        
    def random(self):
        return choice(self.text_list)
        
        
    
    