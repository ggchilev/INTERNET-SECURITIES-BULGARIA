def take_list(my_list):

    return my_list


def check_last(my_list, last, big_list, new_list):
    my_list = take_list(my_list)
    if my_list[len(my_list) - 1] > my_list[len(my_list) - 2] > my_list[len(my_list) - 3] or my_list[len(my_list) - 1] < my_list[len(my_list) - 2] < my_list[len(my_list) - 3]:
        new_list.append(my_list[len(my_list) - 1])
        big_list.append(new_list)
    else:
        last.append(my_list[len(my_list) - 1])
        big_list.append(new_list)
        big_list.append(last)


def seq():

    my_list = take_list([4, 5, 6, 2, 3, 4, 5, 7, 5, 1, 10, 9, 2, 3, 1, 0, 2])
    new_list = [my_list[0]]
    big_list = []
    is_incr = False
    is_all = False
    last = []

    for i in range(0, len(my_list) - 2):

        if i == len(my_list) - 3:
            break

        if my_list[i] < my_list[i + 1]:
            new_list.append(my_list[i + 1])
            is_incr = True

        else:
            if is_incr:
                if is_all == False:
                    big_list.append(new_list)
                    new_list = []
                is_incr = False
                new_list.append(my_list[i + 1])
            else:
                new_list.append(my_list[i + 1])
                if my_list[i + 2] > my_list[i + 1]:
                    big_list.append(new_list)
                    new_list = []
                    is_all = True

    check_last(my_list, last, big_list, new_list)

    return big_list

print(seq())
