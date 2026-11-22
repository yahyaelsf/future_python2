# list1 = ("ahmed" ,"mohammed" , "yahya")

# for index ,item in enumerate(list1) :
#     print(f"{index} is => {item}")
# count = 0
# while count < len(list1):
#     print(list1[count])
#     count +=1
user = {
    "email" : "yahya@gmail.com",
    "age" : 25
}
print(user.get("name","Anon"))
# print(user.items())
# for key , value in user.items():
#     print(f"key is {key} => value is {value}")

# for num in range(2,11):
#     if num == 5:
#         break
#     print(num)

# text = "i love python and python is cery esay to learn and fast in execution"
# my_list = text.split()
# print(my_list)
# my_dec ={}
# for item in my_list:
#    my_dec[item] = my_dec.get(item , 0) + 1

# print(my_dec)

# for num in range(1,101):
#     if  num % 3 == 0 and num % 5 == 0 :
#         print("FuzzBuzz")
#     elif num % 5 == 0 :
#         print("Buzz")
#     elif num % 3 == 0 : 
#         print("Fuzz")
#     else:
#         print(num)
# text = "i i i love python and python is cery esay to learn and fast in execution"
# my_list = text.split()
# print(my_list)
# my_dec ={}
# # for item in my_list:
# #    my_dec[item] = my_dec.get(item , 0) + 1


# """
# ['i', 'love', 'python', 'and', 'python', 'is', 'cery',
# 'esay', 'to', 'learn', 'and', 'fast', 'in', 'execution']
# my_dec["i"] = my_dec.get("i" , 0) + 1
# """

# num = int(input("Enter your number :"))
# count = 1
# while count <= 10 :
#     if count == 5 : 
#         count += 1
#         print("Skip number 5")
#         continue
#     print(f"{count} * {num} => {count * num }")
#     count += 1

text = """
1- add to list
2- print all item
3- exist
"""
sport = []
while True :
    print(text)
    choise = input("Enter Your choise :")
    if choise == "1" :
        new_item = input("Enter new sport")
        sport.append(new_item)
    elif choise == "3":
        print("Good Buy ")
        break
    else : 
        print("Error , wrong choise")



print(sport)