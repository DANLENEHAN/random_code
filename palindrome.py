import math

def is_pal(string: str) -> bool:
    for index in range(math.floor(len(string)/2)):
        if string[index] != string[len(string) - index - 1]:
            return False
    return True

if __name__ == "__main__":
    print(is_pal('11211'))
