#This Program Checks Plagarism in Files.
from cdifflib import CSequenceMatcher
def check_plagarism(data1, data2):
    with open(data1) as fp1, open(data2) as fp2:
        data_File1 = fp1.read()
        data_File2 = fp2.read()
        
        matches = CSequenceMatcher(None, data_File1, data_File2).ratio()
        print("The Files Plagarized with {}%".format(matches))



#Main program
First_file = input("Enter First File Name Along With It's Extension: ")
Second_file = input("Enter Second File Name Along With It's Extension: ")

result = check_plagarism(First_file, Second_file)