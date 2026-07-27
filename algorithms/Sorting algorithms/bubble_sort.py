'''Bubble Sort is an algorithm which is used to sort a list of elements.
it comparess two adjacent elements and then swaps them if they are not in order
the process is repeated until no more swapping is needed.
the algorithm is called Bubble Sort , because with each iteration the smallest 
element in the list bubbles up to the top, just like a water bubble rises up to 
the water surface'''

def bubble_sort(nlist):
    for i in range(len(nlist)):
        for j in range(len(nlist)-1,0,-1):
            if nlist[j]<nlist[j-1]:
                nlist[j], nlist[j-1]=nlist[j-1],nlist[j]
    return nlist
