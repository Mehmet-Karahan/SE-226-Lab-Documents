def remove_duplicates(data_list):
    unique_list = []
    for x in data_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def strip_whitespaces(string_list):
    return [s.strip() for s in string_list]