filename=input('Enter a filename: ')
index=0
for i in range(len(filename)):
    if filename[i]=='.':
       index=i
print(filename[index+1: ])
    

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))


fn= input("Enter Filename: ")
f = fn.split(".")
print ("Extension of the file is : " + f[-1])


