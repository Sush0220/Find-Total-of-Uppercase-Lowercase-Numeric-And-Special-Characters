str1=input("12345AbCd@#$%")
print(str)

count1=0
count2=0
count3=0
count4=0

for i in str1:
    if(i.islower()):
        count1+=1
    elif(i.isupper()):
        count2+=1
    elif(i.isdigit()):
        count3+=1
    else:
        count4+=1

print("Total Lowercase letters= ",count1)
print("Total Uppercase letters= ",count2)
print("Total Numeric values= ",count3)
print("Total Special Characters= ",count4)
