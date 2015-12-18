def find_string(text):

    return text

def find_all_words():

    text = find_string('dawdw8a dwa wqr uye')
    new_text = ''
    new_text2 = ''
    list_of_words = []
    for c in text:
        if c.isalpha():
            new_text += c
        else:
            new_text2 = new_text
            new_text = ''
            list_of_words.append(new_text2)

    return list_of_words

def check_if_longer(length):

    my_list = find_all_words()
    my_new_list = []
    my_new_list2 = []
    for item in my_list:
        for i in item:
            my_new_list2.append(i)
        my_new_list.append(my_new_list2)
        my_new_list2 = []

    for item in my_new_list:
        if len(item)+1 > length:
            for i in range(0, len(item)):
                if i+1 > length:
                    item[i] = '.'
    for item in my_new_list:
        print(''.join(item))



    #return(my_new_list)

print(check_if_longer(2))



