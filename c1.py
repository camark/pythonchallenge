
def isWord(c):
    return c>='a' and c<='z'
    
def cc(c):
    i = ord(c)+2
    if i>ord('z'):
        i = i - 26
    return chr(i)
    
def cc2(c):
    ret = ""
    for v in c:
        if isWord(v):
            ret = ret + cc(v)
        else:
            ret = ret + v
    return ret
    
myword = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print cc2(myword)
print cc2("map")