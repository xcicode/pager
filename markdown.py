from string import Template

def header(text,level):
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

def lists(texts,ordered):
    i=1
    result=""
    for text in texts:
        if ordered==True:
            result=result+str(i)+str(text)+'\n'
        else:
            result=result+"- "+str(text)+'\n'
        i=i+1
    return result


