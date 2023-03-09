for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

# #Задан массив из n чисел. Напишите программу, которая считает и выводит количество чисел равных нулю.8
# a=0
# N=int(input("размер массива "))
# A=[0]*N
# for i in range(N):
#     print("A[",i,"]=", sep="", end="")
#     A[i]=int(input())
#     if A[i]==0:a=a+1
# #     a+=A[i]
# print("нулей = ", a)

## Задан массив из 10 чисел. Напишите программу, которая выводит их сумму.
# a=0
# N=10
# A=[0]*N
# for i in range(N):
#     print("A[",i,"]=", sep="", end="")
#     A[i]=int(input())
#     a+=A[i]
# print("сумма элементов = ", a)