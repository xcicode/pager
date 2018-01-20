from string import Template

def header(text,level=2):
    level=max(1,level)
    level=min(6,level)
    result='#'*level+' '+text
    return result;

def bold(text):
    result='**'+text+'**'
    return result

def italic(text):
    result='*'+text+'*'
    return result

def delline(text):
    result='~~'+text+'~~'
    return result

def b(text):
    return bold(text)

def i(text):
    return italic(text)

def d(text):
    return delline(text)

def quote(text):
    result='> '+text
    return result

def qcodes(text):
    result='`'+text+'`'
    return result

def qcodem(text):
    result="```\n"+text+"\n```"
    return result

def link(text,link):
    result=Template('[$text]($link)')
    return result

def sublist(texts,level):
    if level > 5:#迭代上限
        return ""
    result=""
    prefix=' '*((level*2)+5)
    level+=1
    for text in texts:
        if type(text)==list:
            result=result+sublist(text,level)
            continue
        result=result+prefix+"- "+str(text)+'\n'
    return result

def lists(texts,ordered=False):
    i=1
    result=""
    for text in texts:
        if type(text)==list:
            result=result+sublist(text,0)
            continue
        if ordered==True:
            result=result+str(i)+'. '+str(text)+'\n'
        else:
            result=result+"- "+str(text)+'\n'
        i=i+1
    return result

def tlists(texts,checks):
    result=""
    for i in range(0,min(len(texts),len(checks))):
        if checks[i]==True:
            result=result+'[x]'+' '+str(texts[i])+'\n'
        else:
            result=result+'[ ]'+' '+str(texts[i])+'\n'
    return result
