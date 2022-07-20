str1=str(input("Enter the word"))
reverse=""
for i in range(len(str1)):
    reverse=str1[i]+reverse
print(reverse)