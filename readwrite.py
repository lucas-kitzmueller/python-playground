
# open name.txt and save it as my_name
with open('name.txt') as f:
    my_name = f.read()

# check if correctly read
print(my_name)

with open('hello.txt', 'w') as f:
    f.write('hello, my name is ')
    f.write(my_name)
    f.write('\n')

