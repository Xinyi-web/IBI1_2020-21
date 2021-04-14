import re
import os
os.chdir("C:/Users/Administrator/Desktop/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
file1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
file2 = open('unknown_function.fa','w')
a = file1.read()
x = re.split('>',a)#use list to store
for i in x:
    if 'unknown function' in i:
        gene_name = re.findall(r'gene:(.+?)\s',i)[0]#abstract the gene name
        full_seq = re.sub(r'.+]','',i)
        final_seq = re.sub(r'\n','',full_seq)#abstract and deal with the sequence
        L = len(final_seq)#calculate the length
        file2.write(f'{gene_name:20}'++str(L)+'\n'+final_seq)#output the results

file1.close()
file2.close()


