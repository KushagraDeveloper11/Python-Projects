# file= open("Day 15+\Day 24 File\my_file.txt")
# contents= file.read()
# print(contents)
# file.close()

with open("Day 15+\Day 24 file\my_file.txt") as file:
    contents= file.read()
    print(contents)
    
with open("Day 15+\Day 24 file\\new_file.txt", mode="w") as file:
    file.write('Hello My World')