

def header(text,level):
    level=max(1,level)
    level=min(6,level)
    result='#'*level + ' ' + text
    return result;
