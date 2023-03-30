def list_diferecne_for(list_a, list_b):
    new_list = []
    for i in list_a:
        if not (i in list_b or i in new_list):
            new_list.append(i)

    return new_list