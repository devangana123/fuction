def greatestLen(word1,word2):
    if len(word1)==len(word2):
        return (word1+"\n"+word2)
    if len(word1)>len(word2):
        return word1
    else:
        return word2
# x=greatestLen("hello","welcome")
x=greatestLen("sonu","monu")
print(x)




