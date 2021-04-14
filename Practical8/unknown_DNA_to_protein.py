import re
#process the data
file_name = input()
file1 = open(file_name)
file2 = open('unknown_DNA_to_protein.py','w')
a = file1.read()
x = re.split('>',a)
for i in x:
    gene_name = re.findall(r'gene:(.+?)\s',i)[0]#abstract the gene name
    full_seq = re.sub(r'.+]','',i)
    final_seq = re.sub(r'\n','',full_seq)#abstract and deal with the sequence
    Len = len(final_seq)
    b = Len / 3#length of protein
    protein_seq = ''
    while b > 0:
        c = final_seq[:3]
        dict = {}
        protein = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
                   'ATT': 'I', 'ATC': 'I', 'ATA': 'J', 'ATG': 'M', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
                   'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                   'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                   'TAT': 'Y', 'TAC': 'Y', 'TAA': 'O', 'TAG': 'U', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Z',
                   'AAT': 'N', 'AAC': 'B', 'AAA': 'K', 'AAG': 'K', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                   'TGT': 'C', 'TGC': 'C', 'TGA': 'X', 'TGG': 'W', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                   'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
        e = protein[c]
        protein_seq = protein_seq + e
        final_seq = final_seq[3:]
        b = b - 1
#output the results
file2.write(f'{name:20}'+str(b)+'\n'+protein_seq)

file1.close()
file2.close()
