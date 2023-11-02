def convertirTexto (text):
    return text.lower().replace(" ","")
    
def es_polindormo(text):
    pharse =text
    pharse_reverse = ''.join(reversed(pharse))
    if pharse == pharse_reverse :
        print(True)
    else:
        print (False)    

test = convertirTexto("A mama Roma le aviva el amor a papa y a papa Roma le aviva el amor a mama")

es_polindormo(test)