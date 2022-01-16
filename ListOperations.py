#Program that demonstrate different list operations.....
'''Operations covered in this program are:
1. Append
2. Extend
3. Insert
4. Reverse
5. Index
6. Len
7. Sort
8. Clear
9. Count
10. Pop
11. Del
12. Remove
13. Max
14. Min '''
# using while true loop to execute code infinte time
from pickle import EMPTY_TUPLE


while True:
    # taking list values from user using while loop
    emptylist = []
    i = 0
    listelements = int(input("Enter number of elements in a  list :"))
    while i < listelements:
        list1 = input("Enter the list values : ")
        emptylist.append(list1)
        i += 1
    print("The list is ",emptylist)
    # taking input of different functions in list
    operand = input("Enter the operation\nAppend\nInsert\nReverse\nIndex\nLen\nSort\nClear\nCount\nPop\nDel\nRemove\nMax\nMin : ")
    if operand.lower() == "append":
        appendvalue = input("Enter the value which you want to append in list :")
        emptylist.append(appendvalue)
        print("The appended list is ", emptylist)
    elif operand.lower() == "insert":
        indexvalue = int(input("Enter the indexvalue in which you want to insert :"))
        Object = input("Enter the object to be inserted :")
        emptylist.insert(indexvalue,Object)
        print("The updated list is ", emptylist)
    elif operand.lower() == "reverse":
        emptylist.reverse()
        print("The reversed list is ", emptylist)
    elif operand.lower() == "index":
        listelement = input("Enter the element from the list , it's index value will be generated :")
        a = emptylist.index(listelement)
        
        print("The index value of list's element is ", a)
    elif operand.lower() == "len":
        length = len(emptylist)
        print("The length of list is ", length)
    elif operand.lower() == "sort":
        emptylist.sort()
        print("The sorted list is ", emptylist)
    elif operand.lower() == "clear":
        emptylist.clear()
        print("The list is cleard", emptylist)
    elif operand.lower() == "count":
        occurelement = input("Enter the element of which you want to see the occurence :")
        occurence = emptylist.count(occurelement)
        print("Number of times element occured in list is ", occurence)
    elif operand.lower() == "pop":
        popindex = int(input("Enter the index value of element which you want to delete :"))
        emptylist.pop(popindex)
        print("The updated list is ", emptylist)
    elif operand.lower() == "del":
        delindex = int(input("Enter the index value of element which you want to delete :"))
        del emptylist[delindex]
        print("The updated list is ", emptylist)
    elif operand.lower() == "remove":
        removeobject = input("Enter the element which you want to remove :")
        emptylist.remove(removeobject)
        print("The updated list is ", emptylist)
    elif operand.lower() == "max":
        print("Note: To use max function all elements in list must be of same datatypes otherwise program will generate error\n")
        maximum = max(emptylist)
        print("The maximum value in list is ", maximum)
    elif operand.lower() == "min":
        print("Note: To use min function all elements in list must be of same datatypes otherwise program will generate error\n")
        minimum = min(emptylist)
        print("The minimum value in list is ", minimum)
        
    else:
        print("Please make a right choice from the functions given above")
        print("Thank You , a program by Shubham")
    






