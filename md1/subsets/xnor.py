import math


bools = ["0", "1", "True", "False"]

def main():
    a = get_input("First")
    b = get_input("Second")

    result = xnor(a, b)

    print(result)

def is_zero(x):
    try:
        return int(x) == 0
    except:
        return 0

def transform_bool(x):
    return False if is_zero(x) or x.capitalize() == "False" else True
    

def get_input(nth):
    
    while True:
        a = input(f"{nth} boolean expression: ")
        if a.capitalize() in bools:
            a = transform_bool(a)
            break
    return a

def xnor(a, b) -> bool:
    """
    This fuctions returns the xnor of two boolean values
    """
    return (a and b) or (not a and not b) 

def mfloor(a):
    return math.floor(a)


if __name__ == "__main__":
    main()

#? Hey