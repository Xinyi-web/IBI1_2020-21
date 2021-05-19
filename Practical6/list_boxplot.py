gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
print(gene_lengths)#test

average_exon_lengths=[a/b for a,b in zip(gene_lengths,exon_counts)]#from the internet
average_exon_lengths.sort(reverse=False)#sort them in ascending order
print(average_exon_lengths)

import numpy as np
import matplotlib.pyplot as plt
n=10
score=average_exon_lengths
plt.boxplot(score,vert=True,whis=1.5,patch_artist=True,meanline=True,showbox=True,showcaps=True,showfliers=True,
notch=False)
plt.show()
