# ini comment
"""
ini juga comment
"""

# ini variable in python
a = 1
abc = 5
A = 'kaya kie tok bee cah sd bisa' #variable string
asds = 0.14

print(a)
print(abc)
print(A)
print(type(asds))

# best variable in python 
my_variable = 2
myVariable = 2

# penamaan kelas
class MyClass:
    pass
#  penamaan function
def my_function():
    pass
def myBoobs():
    pass

#
a , b, c = 1, 2, 3
d = e = f = "cilaka londo"

print(a)
print(b)
print(c)

print(d)
print(e)
print(f)

# convet variable
a = 1.0
print(a)
a = int(a)
print(a)

# contoh penggunaan
# string to int
a = 10
print(a)
b = '2'
print(a + int(b))

# indexing
a = "hallo kids ini \nBapamu remidial project"
print(len(a))
print(a)
print(a[:14])

# boolean python
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool("asd"))
print(bool(""))
print(bool(" "))
print(bool("none"))

# operator
# expontial
a = 11
b = 9
print(a**b)
# pembagian
print(a / b)
# modulus
print (a % b)
if a % 2 == 0:
    print("genap")
else:
    print("ganjil")



# looping python while
# i = 0
# while i < 10:
#     print ('helloworld!', i)
#     i += 1
i = 0
# while True:
#     i += 1
#     if i >= 10:
#         break
#     if i == 5:
#         continue
#     print ('helloworld!', i)
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("mandeg kunyuk")

a = ["muhit", "yasir", "bais"]
b = ["ayas", "budi", "zilong"]
for x in a:
  for y in b:
      print(x, "vs" ,y)


def myFunction(*big):
    for x in big:
        print (x)
myFunction("bais", "ganteng", "banget")


# recurtion
def my_function(a):
    if a == 0:
        return
    print (a)
    a -= 1
    my_function(a)

my_function(10)