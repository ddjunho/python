
outfp = open("D:\\202003302\\test5.txt","w")

infp = input()
outfp.write(infp)
outfp = open("D:\\202003302\\test5.txt","r")
inlist = outfp.readlines()
print(inlist)
outfp.close()
