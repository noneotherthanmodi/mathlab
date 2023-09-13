
expression = "not ((p or q) and (not p or r) and (not q or r)) or r"
expression = expression.replace("and","&")
expression = expression.replace("or","|")
expression = expression.replace("not","~")
print("logical expression")
print("  X=  ")
display(expression)
X = []
print("Truth table: ")
print(" --------- ")
print(" | p | q | r | X ")
print(" --------- ")
for p in range(0,2):
    for q in range(0,2):
        for r in range(0,2):
            x = abs(eval(expression))
            X.append(x)
            print(" | " + str(p) + " | " + str(q) + " | " + str(r)+ " | " + str(x)+ " | ")
            print(" ------- ")
check = all(i == X[0] for i in X)
if check:
    if X[0]==0:
        print("contradiction")
    else:
        print("Tautology") 
else:
    print("Neither tautology nor contradiction")
