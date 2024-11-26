import xnor as x


def main():
    # myset = []

    # get_set(myset)

    # # print_set(myset)

    # myset = set(myset)

    # pset = get_subsets(myset)
    

    # print_set(pset)
    d = x.mfloor(12.54)
    b = x.xnor(1, 1)
    print(d)


def get_subsets(input_set):
    
    result = [[]]  # Start with the empty set

    for element in input_set:
        # Create new subsets by adding the current element to each existing subset
        # for subset in result:
        #     print(subset + [element])
        result += [subset + [element] for subset in result]
    
    return result
            




def get_set(s):

    inp = input("set = ")

    inp = inp.replace(" ", "").split(",")

    for element in inp:
        s.append(element)
    

def print_set(s):
    print("[", end="")
    print(*s, end="", sep=",")
    print("]", end="")
    print()

if __name__ == "__main__":
    main()