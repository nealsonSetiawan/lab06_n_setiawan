#testFile.py
#Nealson Setiawan
#Lab 06

from Apartment import Apartment
from lab06 import mergesort,ensureSortedAscending,getNthApartment\
    ,getTopThreeApartments

def test_ProfSO1():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")

    apartmentList = [a0, a1, a2, a3, a4, a5]
    length = len(apartmentList)

    print("First and last apartment in UNSORTED apartmentList ...")

    print(getNthApartment(apartmentList, 0))
    print(getNthApartment(apartmentList, length-1))

    mergesort(apartmentList)

    # The sorted apartment list is now as follows. 
    # apartmentList = [a4, a5, a2, a3, a1, a0]

    print("First and last apartment in SORTED apartmentList ...")

    print(getNthApartment(apartmentList, 0))
    print(getNthApartment(apartmentList, length-1))

test_ProfSO1()

def test_ProfSO2():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")

    apartmentList = [a0, a1, a2, a3, a4, a5]

    # Notice that top three apartments are a4, a5, and a2 in that order
    # Make sure you understand why
    mergesort(apartmentList)
    for i in range(len(apartmentList) -1):
        print(getNthApartment(apartmentList,i))


    print(getTopThreeApartments(apartmentList))

#test_ProfSO2()

def test_ProfSO3():
    a0 = Apartment(2400, 50, "average")
    a1 = Apartment(2200, 50, "excellent")

    apartmentList = [a0, a1]

    print(getNthApartment(apartmentList, 0))
    print(getNthApartment(apartmentList, 10))

#test_ProfSO3()