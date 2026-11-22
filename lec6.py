# # # email = True
# # # password = True 

# # # if email == True :
# # #     if password == True :
# # #         print("Login Successfully")
# # #     else : 
# # #         print("Error In Password")
# # # else : 
# # #     print("Error In Email")

# # dirnks = ["coffe" , "Tee" , "IceMoka" , "cptchino" ]
# # print("""
# # 1- add To List
# # 2- edit from list
# # 3- delete from list
# # """)
# # choise = input("Enter Your choise :")
# # if choise == "1" :
# #     new_item = input("Enter new drink :")
# #     dirnks.append(new_item)
# #     print("item add successfully :")
# # elif choise == "2" :
# #     drink = input("Enter edit drink :")
# #     if drink in dirnks :
# #         index = dirnks.index(drink)
# #         new_item = input("Enter new drink :")
# #         drink[index] = new_item
# #         print("drink updated successfully")
# #     else : 
# #         print("drink not exist :")
# # elif choise == "3":
# #     drink = input("Enter deleted drink :")
# #     dirnks.remove(drink)
# #     print("drink deleted successfully")
# # else : 
# #     print("error in choise :")

# # match choise :
# #     case "1" :
# #         print("case 1")
# #     case "2":
# #         print("case 2")
# #     case "3" :
# #         print("case 3")
# #     case _:
# #         print("Error")

# # starter = 0
# # items = []
# # while starter <= 4 :
# #     item = input("Enter your value :")
# #     items.append(item)
# #     starter = starter + 1 #starter += 1

# # print(items)
# # attemps = 3
# # passeprd = "1234"
# # while attemps > 0 :
# #     value = input("Enter Your password :")
# #     if value == passeprd :
# #         print("login successfully ")
# #         break
# #     else : 
# #         print("Error in password , try agin")
# #         attemps -= 1

# # count = 0
# # while count < 50 :
# #     if count == 5 :
# #         break
# #     print(count)
# #     count +=1

# text = "welcome in python world"
# count = 0
# vaoial = "aeiou"
# vouel_counter = 0
# while count < len(text) :
#     if text[count] in vaoial :
#         vouel_counter += 1
#     print(text[count])
#     count += 1

# print(f"the total number of vaoul is {vouel_counter}")
