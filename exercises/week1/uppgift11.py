def checkLongestWord(string):
    word = max(string, key=len)
    word_len = len(word)
    print(f'Ordet {word} är {word_len} tecken långt')

myStr = ["bil", "boll", "tomte", "fotboll", "flygplan", "långpanna"]

checkLongestWord(myStr)
        