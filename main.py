def scanword(word:str):
    symbols = {}
    for symbol in word:
        if symbol in symbols:
            symbols[symbol] +=1
        else:
            symbols[symbol] = 1
    print(symbols)

scanword("фффаааффф")
