
f = open("datos", "r")

c = f.read(1)
res = ""
i = 0
while c != "":
    if c=="\n":
        res+=","
    else:
        if c == "-":
            i+= 1
        res+=c
    c = f.read(1)

res = f"heuristica[{i}] = [ "+ res
res+="]"
print(res)