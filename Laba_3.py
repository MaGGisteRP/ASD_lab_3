def find_numbers(x):
    result = []
    for k in range(x):
        for l in range(x):
            for m in range(x):
                if (3 ** k) * (5 ** l) * (7 ** m) == x:
                    result.append((k, l, m))
    return result

x = int(input("Enter a value for x: "))  # Get the input value for x
output = find_numbers(x)

if output:
    print("Values of K, L, M that satisfy the condition:")
    for values in output:
        k, l, m = values
        print(f"K: {k}, L: {l}, M: {m}")
else:
    print("No values of K, L, or M found that satisfy the condition.")