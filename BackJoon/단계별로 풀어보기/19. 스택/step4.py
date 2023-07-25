# 균형잡힌 세상, 4949번

while(True):
    sentence = input()
    
    if sentence == ".":
        break
    
    check = ""
    for c in sentence:
        if c == '(' or c == ')' or c == '[' or c == ']':
            check += c
    
    while(check.find("()") != -1 or check.find("[]") != -1):
        if check.find("()") != -1:
            check = check.replace("()", "")
        if check.find("[]") != -1:
            check = check.replace("[]", "")
        
        print(check)
    
    if len(check) <= 1:
        print("yes")
    else:
        print("no")