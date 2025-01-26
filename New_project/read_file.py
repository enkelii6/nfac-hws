file_name = 'example.txt'

with open(file_name, 'r') as file:
    for line in file:
        print(line.strip())