def makedict(text)
    uniquedict = {}
    for i in text.lower().split():
        j = i.strip('.')
        if j in uniquedict:
            uniquedict[j]+=1
        else:
            uniquedict.update({j:1})
​

#    text_file = open("Output.txt", "w")
    for i in uniquedict:
        print str(i)+" "+str(uniquedict[i])
        text_file.write(str(i)+" "+str(uniquedict[i]))
        text_file.write('\n')
        text_file.close()

    return
​
