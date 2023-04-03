outfp = open("D:\\202003302\\test7.txt","r")
inStr = outfp.readlines()
print(inStr)
outfp.close()
infp = open("D:\\202003302\\test7.txt", "w")
for i in inStr:
    infp.write(i.replace("java","python"))
infp.close()