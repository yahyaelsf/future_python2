# user = {
#     "id" : "20161595",
#     "name" : "yahya",
#     "skills" : ["css" , "html" , "js" , "python"],
#     "info" : {
#         "phone" : "0599141212",
#         "addres" : "gaza",
#         "age" : 25,
#     }
# }
# print(user["skills"][1])

# currencies = {
#     "usd" : 3.22,
#     "jod" : 4.56,
#     "eur" : 3.8,
#     "tls" : 1.0,
# }
# additional_currency = {
#     "sur" : 0.95,
#     "jen" : 0.0001
# }
# currencies.update(additional_currency)
# print(currencies)
# cureency = input("Enter Your currency (usd , jod , eur , tls) :")
# amount = float(input("Enter Your Amount :"))
# result  = currencies[cureency] *amount
# print(f"amount {amount} in {cureency} equal {result} in TLS")
# name = "yahya"
# age = "25"
# email = "yahya@gmail.com"
# user = {
#     "name" : name,
#     "age" : age , 
#     "email" : email
# }
# user.pop("name")
# print(user.items())

# if(condition){

# }
# grade = 85
# if grade >= 90 and grade <=100 :
#     print("You are Excellent")
# elif grade >= 80 and grade < 90 :
#     print("You are very good")
# elif grade >= 70 and grade < 80 :
#     print("You are good")
# else :
#     print("You are not good")
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
operation = input("Enter operation (+ , - , * , / , %) ")
if operation == "+":
    result = num1 + num2
    print(f"the final result is {result}")
elif operation == "-":
    result = num1 - num2
    print(f"the final result is {result}")
elif operation == "*":
    result = num1 * num2
    print(f"the final result is {result}")
elif operation == "/":
    result = num1 / num2
    print(f"the final result is {result}")
elif operation == "%":
    result = num1 % num2
    print(f"the final result is {result}")
else :
    print("Error operation not found :")




