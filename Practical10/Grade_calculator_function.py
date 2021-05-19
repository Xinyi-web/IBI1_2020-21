# code for introduce a function for writing name
def g(first_name,last_name):
    name = first_name + "," + last_name
    return(name)
# code for introduce a function for calculating grade
def f(gra_code,gra_poster,gra_exam):
    total = gra_code*0.4 + gra_poster*0.3 + gra_exam*0.3
    return(total)

# give an example
first_name = "Cai"
last_name = "xinyi"
gra_code = 75
gra_poster = 80
gra_exam = 77
print("Here is an example:  "+"name: "+g(first_name,last_name)+"  final grade: "+str(f(gra_code,gra_poster,gra_exam)))
# code for input
first_name = input('please write the first name here:')
last_name = input('please write the last name here:')
gra_code = float(input('please write the code grade here:'))
gra_poster = float(input('please write the poster grade here:'))
gra_exam = float(input('please write the exam grade here:'))
print("name: "+g(first_name,last_name)+"  final grade: "+str(f(gra_code,gra_poster,gra_exam)))


