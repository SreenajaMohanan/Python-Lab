color = []
n = int(input("Enter total NUmber of colours : "))
print ("Enter colours")
for i in range (n):
    ch = input()
    color.append(ch)
print(f"first colour is : {color[0]}\n Last colour is : {color[-1]}")
