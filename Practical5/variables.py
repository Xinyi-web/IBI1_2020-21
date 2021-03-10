a=231101
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
if d<e:
  print("d<e")
elif d>e:
  print("d>e")
else:
  print("d=e")


#Booleans
X=True
Y=False
Z=(X and not Y) or (Y and not X)
if Z==True:
  print("True")

W=(X!=Y)
if Z==W:
  print("Z==W")

