A = 0
B = 1 
C = 8

A = 6
B = 1 
C = 1

dic = {
    "A": A*"a",
    "B": B*"b",
    "C": C*"c"
}

def all_zero(dic):
    for key in dic:
        if len(dic[key]) != 0:
            return False
    return True


def get_biggest(dic, exclude=None):
    max_ = 0
    max_char = ""
    for key in dic:
        if key == exclude:
            continue
        if len(dic[key]) > max_:
            max_ = len(dic[key])
            max_char = key
    return max_char


def check_one_left(dic):
    count = 0
    for key in dic:
        if len(dic[key]) == 0:
            count += 1
    if len(dic) - 1 == count:
        return True
    else:
        return False


char = ""
count = 0
skip = False
while not all_zero(dic):

    if not skip:
        stack = get_biggest(dic)
    else:
        stack = get_biggest(dic, skip)

    if stack == "":
        stack = get_biggest(dic)
        count = 0

    char += dic[stack][-1]
    dic[stack] = dic[stack][:-1]
    count += 1

    if count == 2:
        skip = stack
        count = 0
    else:
        skip = False

    if len(dic[stack]) == 0:
        count = 0

    if check_one_left(dic):
        stack = get_biggest(dic)
        char += (dic[stack][-1] + dic[stack][-1])
        break


print(char)




