def isValid(s):
    import re
    pattern = "a.(aa)*b*(c|d)"
    if re.match(pattern, s):
        return True
    else:
        return False
for t in ["aad", "ac", "a c", "abc"," aad","a aad","a ad"]:
    print( isValid(t) )