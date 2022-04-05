input_list = ['cat','dog','act','god','atc','cta','ogd']
for j in range(len(input_list)-1):
    new_list = []
    new_list.append(input_list[0])
    input_list.remove(input_list[0])
    len1 = len(input_list)
    for i in range(0,len1):
        if sorted(new_list[0]) == sorted(input_list[i]):
            new_list.append(input_list[i])
            input_list.remove(input_list[i])
        if i >= len(input_list):
            break
    if j > len(input_list):
        print(new_list)
        break
    print(new_list)
