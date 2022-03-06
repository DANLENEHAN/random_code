
string = "aaBabcDaA"

string = "WeTestCodErs"
string =""


string="qaswedreftt"
dic = {}

for char in string:

    if char.lower() not in dic:
        dic[char.lower()] = [char]
    else:
        if char not in dic[char.lower()]:
            dic[char.lower()].append(char)


max_c = ""
for char in dic:
    if len(dic[char]) == 2:
        if char > max_c:
            max_c = char


if max_c == "":
    print("NO")

else:
    print(max_c.upper())
