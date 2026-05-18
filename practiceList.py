initial_list = []

while True:
    my_input = input()
    if my_input == "":
        break
    initial_list.append(my_input)

if initial_list !=[] and len(initial_list) >=3 :
    initial_list[1] = 200
    print(f"Updated (Changed) : {initial_list}")
    initial_list.append(600)
    print(f"Updated (Append) : {initial_list}")
    initial_list.insert(2,300)
    print(f"Updated (Insert) : {initial_list}")
    initial_list.remove(600)
    print(f"Updated (Remove 600) : {initial_list}")
    initial_list.pop(0)
    print(f"Updated (Remove Index 0) : {initial_list}")

# append, clear, copy, count, extend, index, insert
# pop, remove, reverse, sort

