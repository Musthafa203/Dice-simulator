my_list=[2,5,7,8,9,10,14,17,18,19,20]

x=input("Enter the number:")
x=int(x)
def binarysearch(my_list,l,h,x):
 if h>=l:
    m=(h+l)//2
    if my_list[m]==x:
        return m
    elif my_list[m]>x:
        return binarysearch(my_list,l,m-1,x)
    else:
        return binarysearch(my_list,m+1,h,x)
 else:
    return -1
r=binarysearch(my_list,0,len(my_list)-1,x)
if r!=-1:
    print("Number is present at index",str(r))
else:
    print("Number is not present in list")

