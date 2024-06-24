# Lab 06
from Apartment import Apartment # line is required to import all defined functions in apartment.py

def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList)-1):
        if apartmentList[i] > apartmentList[i + 1]: # found a problem. We can check using '>', as we have overloaded this in previous file.
            return False
    return True # no problems found

def mergesort(apartmentList):    # [a0,a1,a2,a3,a4,a5]
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        lefthalf = apartmentList[:mid] # not including the mid value.
        righthalf = apartmentList[mid:] 
        # these two portions of the list are just list portions, pieces of the entire list. # of pieces keep inc. due to recursion
        mergesort(lefthalf)   # recursively sort lefthalf
        mergesort(righthalf)  # recursively sort righthalf. 
        # Up to this point, we have just sorted the left portion and right portion. We haven't joined the two lists.
        # Merge two sorted sublists (left and right) into original list.
        i = 0 # index for lefthalf sublist
        j = 0 # index for righthalf sublist
        k = 0 # index for apartmentList

        while i < len(lefthalf) and j < len(righthalf):    # if this doesn't satisfy, we are at our last element and there is no next element to compare to 
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i += 1
            else:
                apartmentList[k] = righthalf[j]
                j += 1

            k += 1   # whatever if block runs (if or else), we always increment k, which is the apartment index by 1. 

        while i < len(lefthalf):  # this is run when index points to the last element in j
            apartmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf): # this is run when index points to the last element in i
            apartmentList[k] = righthalf[j] 
            j = j + 1
            k = k + 1

def getBestApartment(apartmentList):
    mergesort(apartmentList) # since we need to order the apartment list, in all functions in this lab, except ensureSortedAscending where we just check if list is sorted or not (True/False)
    return apartmentList[0].getApartmentDetails() # I want the first element of apartmentList

        
def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[-1].getApartmentDetails() # I want the last element of apartmentList
        

def getAffordableApartments(apartmentList, budget):
    mergesort(apartmentList)
    affordableapts = []
    for apt in apartmentList:
        if apt.rent <= budget:   # here we are comparing two integers
            affordableapts.append(apt)
    
    affordablestr = ''
    list_len = len(affordableapts)

    for i in range(list_len):
        if i == list_len - 1:
            affordablestr += affordableapts[i].getApartmentDetails()
        else:
            affordablestr += affordableapts[i].getApartmentDetails() + '\n'

    return affordablestr

# a0 = Apartment(1115, 215, "bad")
# a1 = Apartment(1117, 215, "bad")
# a2 = Apartment(99, 215, "bad")
# a3 = Apartment(1226, 215, "average")

# apartmentList = [a0, a1, a2, a3]
# x = getAffordableApartments(apartmentList, 98)
# print(x)