# f=open("abc.txt","w")
# print("File Name:",f.name)
# print("File Mode:",f.mode)
# print("is File Readable:",f.readable())
# print("is File Writable:",f.writable())
# print("is File Closed:",f.closed)
# f.close()
# print("is File Closed:",f.closed)



# f=open("acb.txt","w")
# f.write("my name is surendra\n")
# f.write("i am from hyderabad\n")
# print("data entered successfully")
# f.close()




# f=open("sure.txt","w")
# list=["surendra\n","kwoshik\n","arshad\n","venky\n","pramod"]
# f.writelines(list)
# print("List of lines entered successfully")
# f.close()





# f=open("sure.txt","r")
# data=f.read()
# print(data)
# f.close()


# f=open("sure.txt","r")
# data=f.read(17)
# print(data)
# f.close()


# f=open("sure.txt","r")
# line1=f.readline()
# print(line1,end="")
# line2=f.readline()
# print(line2,end="")
# line3=f.readline()
# print(line3,end="")
# f.close()


# f=open("sure.txt","r")
# print(f.tell())
# print(f.read(3))
# print(f.readline())
# print(f.read(4))
# print("Remaining Data")
# print(f.read())


# with open("sure.txt","w") as f:
#     f.write("Surendra\n")
#     f.write("Kwoshik\n")
#     f.write("Arshad\n")
#     f.write("Venky\n")
#     f.write("Pramod\n")
#     print("is file closed:",f.closed)
# print("is file closed:",f.closed)



# data="all students are Gems"
# f=open("sure.txt","w")
# f.write(data)
# with open ("sure.txt","r+") as f:
#     text=f.read()
#     print(text)
#     print("position of cursor:",f.tell())
#     f.seek(17)
#     print("position of cursor after seek:",f.tell())
#     f.write("Diamonds")
#     f.seek(0)
#     text=f.read()
#     print("Data after Modifications")
#     print(text)