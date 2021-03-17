Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
>>> exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
>>> print(gene_lengths)#test
[9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981]
>>> average_exon_lengths=[a/b for a,b in zip(gene_lengths,exon_counts)]#from the internet
>>> print(average_exon_lengths)
[184.50980392156862, 345.1322241681261, 105.76190476190476, 487.6759259259259, 765.96, 118.12153846153846, 3.8898964128730826, 636.7719298245614, 842.0, 30.55640535372849]
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> n=10
>>> score=average_exon_lengths
>>> plt.boxplot(score,
	    vert=True,
	    whis=1.5,
	    patch_artist=True,
	    meanline=True,
	    showbox=True,
	    showcaps=True,
	    showfliers=True,
	    notch=False
	    )
{'whiskers': [<matplotlib.lines.Line2D object at 0x0000018262374A90>, <matplotlib.lines.Line2D object at 0x0000018262374DF0>], 'caps': [<matplotlib.lines.Line2D object at 0x000001826238E190>, <matplotlib.lines.Line2D object at 0x000001826238E4F0>], 'boxes': [<matplotlib.patches.PathPatch object at 0x0000018262374730>], 'medians': [<matplotlib.lines.Line2D object at 0x000001826238E850>], 'fliers': [<matplotlib.lines.Line2D object at 0x000001826238EBB0>], 'means': []}
>>> plt.show()
>>> 