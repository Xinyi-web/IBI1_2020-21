#df-r,r=1.2,n=84,after 5 times
count=5
r=1.2
n=84
#Use loop statements to implement functions
while count>0:
  count=count-1
  #Notice the difference between the number of people infected and the number of times you have to multiply
  n=n*(r+1)
print("the number of individuals is "+str(n))
