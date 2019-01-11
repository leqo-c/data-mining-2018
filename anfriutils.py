# anfri utils

def SPMFin_to_list(filename):
    import numpy as np
    import re
    
    l = list()
    with open(filename, 'r') as f:
        for line in f:
            s = re.sub('<[0-9]+> ', '', line)
            s = re.sub(' -1 -2', '', s)
            s = re.sub(' -1', ',', s)            
            s = s.split(',')
            s = [int(el) for el in s]
            l.append(s)

    return l
            
# GitHub desktop: test modifica
def SPMFout_to_list(filename, reverse=True):
    import re
    
    l = list()
    with open(filename, 'r') as f:
        for line in f:
            s = re.sub('<[0-9]+> ', '', line)
            s = re.sub(' -1', ',', s)
            s = re.sub(' #SUP: ', '', s)
            s = s.split(',')
            s = [int(el) for el in s]
            l.append( (s[:-1], s[-1]) )
        
    return sorted(l, key=lambda (pattern, sup): sup + len(pattern), reverse=reverse)
    
    
def occurrences(seq, pattern):

	seq_list = [val for val in seq]
	occs = [(i, i+len(pattern)) for i in range( len(seq_list) ) if seq_list[i:i+len(pattern)] == pattern]
	
	return occs 
