def find_position(spysok, novyy_element):
    for i in range(len(spysok)):
        if spysok[i] >= novyy_element:
            return i
    return len(spysok)

sorted_list = [1, 2, 4, 6, 8]
new_val = 3

pos = find_position(sorted_list, new_val)
print(f"Початковий список: {sorted_list}")
print(f"Число {new_val} потрібно вставити на індекс: {pos}")

sorted_list.insert(pos, new_val)
print(f"Список після вставки: {sorted_list}")