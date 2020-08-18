#!/usr/bin/python

unsortedList = [9, 8, 1, 3, 2, 5, 6, 4, 0, 7]
unsortedList_short = [2,1]

# split
# if splittable, split further
# else merge

def merge( seg1, seg2 ):
    joined = []
    while seg1 and seg2:
        if seg1[0] <= seg2[0]:
            joined.append(seg1[0])
            del seg1[0]
        else:
            joined.append(seg2[0])
            del seg2[0]
    while seg2:
        joined.append( seg2[0] )
        del seg2[0]
    while seg1:
        joined.append( seg1[0] )
        del seg1[0]
    return joined

def sort( _list ):
    print("unsorted: ", _list)
    seg1 = []
    seg2 = []
    for i in range(len(_list)):
        if i < len(_list) / 2:
            seg1.append( _list[i] )
        else:
            seg2.append( _list[i] )
    # print( "seg1", seg1)
    # print( "seg2", seg2)


    if len(seg1) > 1:
        seg1 = sort( seg1 )
    if len(seg2) > 1:
        seg2 = sort( seg2 )

    merged = merge( seg1, seg2)
    # print( "merged: ", merged)
    return merged

# sortedList_short = split( unsortedList_short)
sortedList = sort( unsortedList)

# print("sortedList_short: ", sortedList_short)
print("sortedList: ", sortedList)
