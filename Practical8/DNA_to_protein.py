import re
seq = 'ATGCGACTACGATCGAGGGCC'
Len = len(seq)
a = Len/3
d = ''
while a>0:
    #Read forward along the fragment 3 by 3
    b = seq[:3]
    #Use dictionary to replace
    dict = {}
    protein = {'TTT':'F','TTC':'F','TTA':'L','TTG':'L','CTT':'L','CTC':'L','CTA':'L','CTG':'L','ATT':'I','ATC':'I','ATA':'J','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P','ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A','TAT':'Y','TAC':'Y','TAA':'O','TAG':'U','CAT':'H','CAC':'H','CAA':'Q','CAG':'Z','AAT':'N','AAC':'B','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E','TGT':'C','TGC':'C','TGA':'X','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
    c = protein[b]
    d = d+c
    seq = seq[3:]
    a = a-1
print(d)


