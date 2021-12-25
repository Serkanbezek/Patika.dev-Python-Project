# Flattening function
def flatten(alist):
    flattenedlist = []
    for item in alist:
        if type(item) != type([]):
            flattenedlist.append(item)
        else:
            flattenedlist.extend(flatten(item))
    return flattenedlist


# Reversing a list
def reversing_list(alist):
    reversed_list = [elem[::-1] for elem in alist ][::-1]
    return reversed_list



