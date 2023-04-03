outfp = open("D:\\202003302\\test8.txt","r")
inStr = outfp.readlines()
outfp.close()
count =0
infp = open("D:\\202003302\\test8_5.txt","w")
for i in inStr:
    if len(i.replace("\n","")) <=5:
        count +=1
        infp.write(i)
print("5글자 이하인 단어 개수 :", count)


infp.close()