# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) 
def recaman(n):
    seq = [0]

    for k in range(1, n):
        prev = seq[-1]
        candidate = prev - k

        if candidate > 0 and candidate not in seq:
            seq.append(candidate)
        else:
            seq.append(prev + k)

    return seq

length = int(input("Enter the length of the Recaman sequence: "))
sequence = recaman(length)

print("Recaman sequence:")
for num in sequence:
    print(num)
