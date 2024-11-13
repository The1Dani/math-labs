from prettytable import PrettyTable

def main():
    
    input_text = input("Enter the expression: ")

    # input_text = "(!x + y) * z + (!z * y * k)"

    expression, variables, _ = parse_expression(input_text)
    
    arr = generate_expression(expression, variables)

    variables.append(input_text)

    table = PrettyTable(field_names=variables)
    
    table.add_rows(arr)

    print(table)
    
def generate_expression(expression, variables):
    arr = generate_combinations(len(variables))
    for e in arr:
        ex = expression
        for v in range(len(variables)):
            ex = ex.replace(variables[v], "True" if e[v] == True else "False")
        e.append(int(eval(ex)))    
    return arr

def generate_combinations(n):
    combinations = []
    for i in range(2**n):  # Loop from 0 to 2^n - 1
        binary = bin(i)[2:]  # Convert to binary and remove '0b'
        binary = '0' * (n - len(binary)) + binary  # Pad with leading zeros
        combinations.append([int(bit) for bit in binary])  # Convert each character to an integer
    return combinations

def parse_expression(input_text):
    """
    returns: ft, vArr, t \n
    ft = final text
    vArr = variables array
    t = transformed text 
    """
    t, vArr = make_boolean(input_text)
    ft = transform(input_text)
    t = transform(t)
    vArr = list(set(vArr))
    return ft, vArr, t

def make_boolean(input_text):
    arr = []
    for l in input_text:
        if l.isalpha():
            input_text = input_text.replace(l, "True")
            arr.append(l)
    return input_text, arr

def transform(input_text):
    input_text = input_text.replace("+", " or ")
    input_text = input_text.replace("*", " and ")
    input_text = input_text.replace("!", " not  ")
    return input_text



if __name__ == "__main__":
    main()