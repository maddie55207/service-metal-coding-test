import sys

# validate input
if len(sys.argv) < 2:
    print("Usage format: python permutations.py <filename>")
    sys.exit(1)

input_file = sys.argv[1]
strings = []

try:
    with open(input_file, "r") as file:
        for line in file:
            # add each string to a list, removing whitespace
            strings.append(line.strip())
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
except Exception as e:
    print(f"File error: {e}")

def find_permutations(str):
    # base case
    if(len(str) == 0):
        return ['']
    
    perms = []
    for i in range(len(str)):
        current_char = str[i]
        substr = str[:i] + str[i+1:] # remove current_char from string

        for p in find_permutations(substr): # recursively find perms of substr
            perms.append(current_char + p)

    return perms

all_perms = []
for s in strings:
    all_perms.append(find_permutations(s))

print(f"Permutations for file {input_file}:\n")

for set in all_perms:
    set.sort()
    print(", ".join(set))
    

