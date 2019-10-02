dl, db = input().split()
a = int(dl)
b = int(db)
design = '.|.'
j = 1
message = "WELCOME"
for i in range(a): 
    if(j<a):       
        print((design*j).center(b,"-"))
    else:
        j -=2
        print(message.center(b,"-"))
        break
    j +=2
for i in range(a):
    if(j>0):
        print((design*j).center(b,"-"))
    else:
        break
    j -=2
