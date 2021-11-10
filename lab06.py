#CS9 Lab06
#Nealson Setiawan
#rent -> meters -> condition

from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList)>1:
        mid = len(apartmentList)//2
    
        left = apartmentList[mid:]
        right = apartmentList[:mid]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while(i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                apartmentList[k] = left[i]
                k = k+1
                i = i+1
            else:
                apartmentList[k] = right[j]
                k = k+1
                j = j+1

        while(i < len(left)):
            apartmentList[k] = left[i]
            k = k+1
            i = i+1

        while(j < len(right)):
            apartmentList[k] = right[j]
            k = k+1
            j = j+1
        
def ensureSortedAscending(apartmentList):
    sorted = True

    for i in range(len(apartmentList)-1):
        for j in range(len(apartmentList)-1,i,-1):
            if(apartmentList[i]>apartmentList[j]):
                return False
    
    return True

def getNthApartment(apartmentList, n):
    try:
        return apartmentList[n].getApartmentDetails()
    except IndexError:
        return "(Apartment) DNE"

def getTopThreeApartments(apartmentList):
    strTotal = ""
    mergesort(apartmentList)

    if(ensureSortedAscending(apartmentList) == False):
        return "Your MergeSort Function is not working properly."

    for i in range(0,3):
        if(getNthApartment(apartmentList, i) != "(Apartment) DNE"):
            if i == 0:
                strTotal = "1st: " + getNthApartment(apartmentList, i) + "\n"
            elif i == 1:
                strTotal = strTotal + "2nd: " + getNthApartment(apartmentList, i) + "\n"
            elif i == 2:
                strTotal = strTotal + "3rd: " + getNthApartment(apartmentList, i)

    return strTotal

l = [1,2,1,4,5,6]
mergesort(l)
print(l)
print(ensureSortedAscending(l))
    



                        

