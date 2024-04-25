
list = [10,55,77,63,21,42,32,96,84,28,76,49,32]
# print("current list : ",list)
# list.sort()
# print("sorted list : ",list)
# print(f"maximum value in the list : {list[-1]}\nminimum value in the list : {list[0]}")

# max = list[0]
# min = list[0]
# for i in list:
#     if i>max:
#         max=i
#     elif i < min:
#         min=i
# print(min)
# print(max)


# a=10
# b=20
#
# a=a+b
# b=a-b
# a=a-b
# print("value of A is : ",a)
# print("value of B is : ",b)


# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print()
#
# for i in range(5):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(i, 5):
#         print("* ", end="")
#     print()
#
#
# for i in range(5):
#     for j in range(5, i, -1):
#         print(" ", end="")
#     for k in range(i + 1):
#         print("* ", end="")
#     print()
# for i in range(5):
#     for j in range(5, i, -1):
#         print(" ", end="")
#     for k in range(i + 1):
#         print("* ", end="")
#     print()
#
#
#
#
# n = 5
#
# # Upper half of the diamond
# for i in range(n):
#     for j in range(n - 1, i, -1):
#         print(" ", end="")
#     for k in range(i + 1):
#         print("* ", end="")
#     print()
#
# # Lower half of the diamond
# for i in range(1, n):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(n - 1, i - 1, -1):
#         print("* ", end="")
#     print()

n = 5

""""
*****
*   *
*   *
*   *
*****

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()"""


# class A():
#     def __init__(self):
#         print("This is constructor of parent A")
# class B(A):
#     def __init__(self):
#         print("This is constructor of parent B")
#         super().__init__() # calls the parent call consrtuctor
#         A.__init__(self)  # calls the parent call consrtuctor
# bobj=B()

# class myclass():
#     __a=10
#     def display(self):
#         print(self.__a)
# obj=myclass()
# obj.display()


# Protected example
# class Company():
#     _project= "banking"
#
# class Employee(Company):
#     def __init__(self, name):
#         self.name = name
#         Company.__init__(self)
#
#     def show(self):
#         print("Employee name :", self.name)
#         # Accessing protected member in child class
#         print("Working on project :", self._project)
#
# c = Employee("Jessa")
# c.show()



# try:
#     a = input("enter number of divide to 100 : ")
#     result = 100 / int(a)
#     print("result : ", result)
#
# except Exception as ex:
#     print("wrong input ",ex)


# iList = [10, 30, 50, 100, 60]
#
# for index in range(4,8):     # [0,1,2]
#     print("List element to be process : ", iList[index])

# a = "s1a2ayan86na3nd"
# sum = 0
# for i in a:
#     if i.isdigit():
#         sum = sum+int(i)
# print(sum)

# names = ["dayanand","akash","anil","haney","john","harley","kedar","saru","dhoni","rudra","kesariya","krusna","shyam","ram","sam","rock","sushil","virat","rohit","jasprit","chahal"]
# index = 1
# for name in names:
#     print(index,":",name)
#     index=index+1
#     if index==10:
#         break








