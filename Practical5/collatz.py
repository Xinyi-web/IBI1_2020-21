# 13	values	for	the	Fibonacci	sequence
count=13
x=1
y=1
print(x)
print(y)
# use loop to finish this task
while count>2:
  count=count-1
  z=y
  y=x+y
  x=z
  print(y)
