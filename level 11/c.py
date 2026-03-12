# 1)მომხარებელს შემოატანინეთ რიცხვი, და შეამოწმეთ თუ ეს რიცხვი მეტია 18 ზე დაპრინტოს adult, სხვა შემთხვევაში kid

# 2)მომხარებელს შემოატანინე რიცხვი, და თუ ეს რიცხვი  მეტია 15 ზე, 1 დან ან რიცხვამდე ყველა რიცხვი დაპრინტეთ  ფორ ლუპით

# 3)მომხარებელს შემოატანინე სახელი, თუ ეს სახელი უდრის aleksandre ს, დაპრინტეთ "mentor" სხვა შემთხვევაში ამ ასოში თითოეული ასო ცალ ცალკე გამოიტანეთ ფორ ლუპებით


gg = input("enter your number:")


if gg == 18:   
    print("adult")
else:
    print("kid")

name = input("enter your name:")
if name =="aleksandre":
    print("mentor")
else:
    for i in name:
        print(i)






































# # conditional statements -> პირობითი განცხადებები

# name = input("Enter your name: ")

# # თუ name უდრის "aleksandre" ს მაშინ დავპრინტოთ "mentor", სხვა შემთხვევაშო დავპრინტოთ "student"
# # if, else, elif -> თუ, სხვა შემთხვევაში, სხვა შემთხვევაში თუ
# if name == "aleksandre":
#     print("mentor")
# elif name == "luka":
#     print("assistant")
# else:
#     print("student")