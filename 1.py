"""
Basic Python practice
"""

# print("Hello World")

# x, y, z = "Orange", "Banana", "Cherry"
# print(x, y, z)

# def fun(y):
#   x = "hello"
#   print(x,y)

# fun("Rupesh")

# x = range(6)

# print(x);

# x = set(("apples", "banana", "cherry"))
# print(x)

# x = bool(5)
# print(x)

# x = 5+7j
# print(x)
# print(type(x))
# x=55
# print(x)
# print(type(x))


# x = 1.0005
# print(x)
# x = int(x)
# print(x)

# x = """ .... 
# Hello world,
# How are you.
# """
# print(x)

# x = "Helllllllllllllllooo worldddddddddddddddd"
# print(x)
# print(x[0])
# print(x[1:3])

# print("H".lower())

# print("  dfkjadkf dakfjk afjdkla      ".strip())

# x = "Tehe rain in spain stays mainly in plain "
# ans = "plain" in x
# print(ans)
# ans = "The" in x
# print(ans)
# ans = "ran" not in x
# print(ans)
# ans = "rain" not in x
# print(ans)


# age = 36
# txt = "My name is xyx and my age is {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price =  49.65

# myorder = "I want to pay {} dollars for {} pieces of item {}"

# print(myorder)

# print(myorder.format(price, quantity, itemno))

# myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
# print(myorder.format(quantity, itemno, price))

# print(10>9)
# print(10 == 9)
# print(10<9)

# a = 10
# b = 25
# if (b>a):
#   print(b, "is greater than", a)
# else:
#   print(a, "is greater than", b)


# thislist = ["apple", "banana", "mango"]
# print(thislist)
# print(thislist[0])
# print(thislist[-1])
# print(thislist[1:3])
# print(thislist[1:])
# print(thislist[:3])

# thislist[1] = "ajdfklaj"
# print(thislist)

# for x in thislist:
#   print(x)

# if "apple" in thislist:
#   print("yes")

# print(len(thislist))

# thislist.append("zomato")
# print(thislist)

# thislist.insert(1, "swiggy")
# print(thislist)

# thislist.remove("banana")
# print(thislist)

# thislist.pop()
# print(thislist)

# del thislist[0]
# print(thislist)

# # del thislist
# # print(thislist)

# thislist.clear()
# print(thislist)

# newlist = thislist.copy()
# print(newlist)

# newlist = list(thislist)
# print(newlist)

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple)
# print(thistuple[0])
# print(thistuple[-1])
# print(thistuple[2:5])


# # to change a value of tuple
# y = list(thistuple)
# y[0] = "mapple"
# thistuple = tuple(y)
# print(thistuple)

# for x in thistuple:
#   print(x)

# if "mango" in thistuple:
#   print("yes")

# print(len(thistuple))

# print(type(thistuple))

# # del thistuple
# # print(thistuple)

# t2 = ("a", "b", "c")

# t3 = thistuple + t2
# print(t3)


# thiset = {"apple", "banana", "cherry"}
# print(thiset)

# for x in thiset:
#   print(x)

# if "banana" in thiset:
#   print("yes")

# thiset.add("mango")
# print(thiset)

# thiset.update(["orange", "grapes"])
# print(thiset)

# print(len(thiset))

# thiset.discard("apple")
# print(thiset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# set1.update(set2)
# print(set1)


# thisdict = {
#   "brand" : "ford",
#   "model": "mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)

# print(thisdict["model"])

# print(thisdict.get("brand"))

# for x,y in thisdict.items():
#   print(x, "->" ,y)

# if "model" in thisdict:
#   print("yes")

# print(len(thisdict))

# thisdict["color"] = "red"
# print(thisdict)

# thisdict.pop("model")
# print(thisdict)

# thisdict.popitem()
# print(thisdict)

# del thisdict["year"]
# print(thisdict)

# newdict = thisdict.copy()
# print(newdict)

# family = {
#   "child1" : {
#     "name" : "Rupeee",
#     "year": 2000
#   },
#   "child2" : {
#     "name" : "Rishu",
#     "year": 2000
#   }
# }
# print(family)

# a = 32
# b = 200 

# if b>a:
#   print("greater")
# elif a==b:
#   print("equal")
# else:
#   print("smaller")

# if a<b: print("b is greater")

# print("a") if a>b else print("b")

# a = 200
# b = 33
# c = 500

# if a>b and c>b:
#   print("both greater than b")

# if a>b or c>b:
#   print("atleast one greater than b")

# if 10>20:
#   pass

# i=0
# while(i<10):
#   i = i+1
#   if i == 9:
#     pass
#     # break
#   if i == 2:
#     continue
#   print(i)
# else:
#   print("while loop ended")


# fruits = ["apple", "mango", "banana", "orange"]
# for x in fruits:
#   print(x)

# for x in range(6):
#   print(x)

# for x in range(2, 6):
#   print(x)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)


# def myfun():
#   print("hello from the function")

# myfun()

# def fun(fname):
#   print("hello "+ fname)

# fun("riya")
# fun("rupesh")


# def myfun(*args):
#   print("good one is", args[1]);

# myfun("rupesh", "rishi")


# def myfun(c1, c2, c3):
#   print(c1, c2, c3)

# myfun(c3="hero", c1="superhero", c2="superheropro")


# def fun(**kid):
#   print(kid["c1"],kid["c2"],kid["c3"])

# fun(c3="hero", c1="superhero", c2="superheropro")

# def fun(country="India"):
#   print("I am from country ", country)

# fun()
# fun("US")

# def myfun(food):
#   for x in food:
#     print(x)

# fruits = ["mango", "papaya", "cherry"]
# myfun(fruits)

# def myfun(x):
#   return 5*x

# print(myfun(100))

# def fun():
#   pass

# fun()


# def factorial(n):
#   if n<=1:
#     return 1
#   else:
#     return (n*factorial(n-1))

# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))


# x = lambda a: a+10
# print(x(5))

# x = lambda a,b,c: (a+b)*c
# print(x(1,2,3))

# def fun(n):
#   return lambda a: a*n

# d = fun(2)

# print(d(3))
# print(d(2))



# class Myclass:
#   x=5

# p1 = Myclass()
# print(p1.x)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def fun(self):
#     print("Hello",self.name)

# p1 = Person("John",36)
# p1.fun()

# p1.name = "Rupesh"
# print(p1.name)

# del p1.age
# print(p1.age)


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname,self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)


# x = Student("rupesh", "garhwal")
# x.printname();

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname,self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year


# x = Student("rupesh", "garhwal", 2023)
# x.printname()
# print(x.graduationyear)


# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# str = "hello world"
# myit = iter(str)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


# class myNum:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a<=5:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration    

# ob = myNum()
# it = iter(ob)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


username = input("Enter username : ")
print("username is : ",username)