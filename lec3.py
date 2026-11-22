# name = ['yahya', 'el', 'saftawi'] #"yahya el saftawi"
# # index is from 0 to n-1 , n=> length
# # slicing name[start : end ]
# # print(name[0:len(name)])
# # print(name.center(30," "))
# # print(email)
# students = ["yahya" , "marah" , "ali" , "farah" , "omar"]
# # print(students[1])
# # print(name.split())
# new_name = " ".join(name)
# print(new_name)
# yahyaelsafatwi@gmail.com
# email = input("Enter Your Email :")
# first_split = email.split("@")
# username = first_split[0]
# second_split = first_split[1].split(".")
# company = second_split[0]
# extention = second_split[1]
# print(f"the user name is {username}")
# print(f"the company is {company}")
# print(f"the extention is {extention}")
# yahya-wael-elsafawti
# name = "yahya-wael-elsafawti"
# name_split = name.split("-")
# print(f"my name is {name_split[0]}")
# print(f"my father name is {name_split[1]}")
# print(f"my family name is {name_split[2]}")

names = ["yahya" , "aya" , "ahmed"]
names.append("lana")
names.append("abou alabd")
names.insert(1 , "samar")
names.pop(0)
names[0] = "yahya el saftawi"
print(names.index("aya"))
names[1] = "aya batch"