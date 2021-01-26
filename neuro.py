import os
import numpy as np

def edit_text(text):
    punctuation = "!@#$%^&*()<>:/?:;' "
    for char in punctuation:
        text = text.replace(char, ' ')
    lower_text = text.lower()

    return lower_text

def add_full(path, full_dict, full_list):
    file_names = os.listdir(path) # возвращает в виде массива все файлы в пути

    count = 0
    for file_name in file_names:
        file_path = os.path.join(path, file_name)
        try:
            file = open(file_path,'r')
            text = file.read()
        except:
            continue
        text = edit_text(text)
        words = text.split()

        text_dict = {}
        for word in words:
            if word in full_dict.keys():
                full_dict[word] += 1
            else:
                full_dict[word] = 1
            if word in text_dict.keys():
                text_dict[word] += 1
            else:
                text_dict[word] = 1
        full_list.append(text_dict)
        count += 1
    return full_dict, full_list, count

def delete_keys(full_dict, n = 20):
    for key, value in list(full_dict.items()):
        if value < n:
            full_dict.pop(key)
    return full_dict

def get_matrices():
    path = os.getcwd()
    path = os.path.join(path,'movies')
    pos_path = os.path.join(path, 'pos')
    neg_path = os.path.join(path, 'neg')

    full_dict = {}
    full_list = []

    full_dict, full_list, pos_count = add_full(pos_path, full_dict, full_list)
    full_dict, full_list, neg_count = add_full(neg_path, full_dict, full_list)

    full_dict = delete_keys(full_dict)

    print(full_dict)
get_matrices() # тестовой вызов

