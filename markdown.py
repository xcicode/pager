

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
