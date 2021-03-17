Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> labels='USA','India','Brazil','Russia','UK'
>>> sizes=[29862124,11285561,11205972,4360823,4234924]
>>> plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
([<matplotlib.patches.Wedge object at 0x0000014C927BD640>, <matplotlib.patches.Wedge object at 0x0000014C927BDD30>, <matplotlib.patches.Wedge object at 0x0000014C947D2400>, <matplotlib.patches.Wedge object at 0x0000014C947D2A90>, <matplotlib.patches.Wedge object at 0x0000014C947DF160>], [Text(-1.099451710559182, 0.03472659137446427, 'USA'), Text(0.5451894135676241, -0.9553891894583015, 'India'), Text(1.0937008663664955, 0.1175517541731187, 'Brazil'), Text(0.6755988980089375, 0.8680818676882438, 'Russia'), Text(0.2382122613174141, 1.073897070746561, 'UK')], [Text(-0.599700933032281, 0.018941777113344146, '49.0%'), Text(0.29737604376415855, -0.5211213760681644, '18.5%'), Text(0.5965641089271794, 0.06411913863988292, '18.4%'), Text(0.36850848982305673, 0.47349920055722383, '7.2%'), Text(0.12993396071858948, 0.5857620385890332, '6.9%')])
>>> plt.axis('equal')
(-1.1088333497688243, 1.1161251640944942, -1.1108454942379393, 1.1005164592505174)
>>> plt.show()
>>> 