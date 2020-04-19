'''
Connor Mentel
CS 5001
HW 6
Programming 1
rxdrug_driver.py
'''

# imports
from RX.rxdrug import *



'''
    Function that reads text files.
    
    Parameters: text files
    Returns: List of contents
    Does: Opens the passed through file in read mode, assigns 
    the variable contents and creates a list split by lines.
    '''

def read_files(file):
    try:
        new_file = open(file,'r')
        contents = new_file.read()
        list = contents.splitlines()
        return list

    except OSError:
        print('\nError reading file')




'''
    Function that passses text files into read_files function , assigns variables, 
    and passes those into the RX Class.
    
    Parameters: Nothing
    Returns: Drug interactions, and warnings.
    Does: Parses through the files and assigns variables that 
    will be appended to dictionary and run through class.
'''

def main():
        # list split by lines in file, opens text file rxcui_drugs.txt in read mode
        # and assigns variable Alist to be the text in the file rxcui_drugs.txt
        Alist = read_files('rxcui_drugs.txt')

        # list split by lines in file, opens text file prescriptions.txt in read mode
        # and assigns variable personstart to be the text in the file prescriptions.txt
        personstart = read_files('prescriptions.txt')

        # empty list of drugs
        drug_list = []

        # empty dictionary
        dict_drugs = {}


        # for-loop to loop through all lines in rxcui_drugs.txt
        for i in range(len(Alist)):

            # list of each line broken up by | as a list
            line = Alist[i].split('|')

            # assigns variable 'name' to the first element in list 'line'
            name = line[0]

            # assigns variable 'rx_ID' to the second element in list 'line'
            rx_ID = line[1]

            # assigns variable 'description' to the third element in list 'line'
            description = line[2]

            # assigns variable 'b' to the fourth element in the list 'line'
            b = line[3]

            # assigns the variable 'interactions' to the now separated list of the last variables from b in list 'line'
            interactions = b.split(sep=",")

            # runs the functions from Class RxDrug using the name and rx_ID assigned from loop
            drug = RxDrug(name,rx_ID, interactions)

            # appends the drug and rx_ID from first function in class to 'drug_list'
            drug_list.append(drug)

            # creating dictionary of drugs
            dict_drugs[name]= RxDrug(name,rx_ID,interactions)


        # for-loop to loop through all lines in prescriptions.txt
        for i in range(len(personstart)):

            # Parsing through the prescriptions.txt file
            parson = personstart[i].split('|')

            # Gets the name from prescriptions.txt file
            person = parson[0]

            # Gets the second element, condition from the line
            ConditionFinal = parson[1]

            # Gets the third element, prescriptions from the line
            RXFinal = parson[2]

            # Splits lines by comma
            splitRXFinal = RXFinal.split(',')

            for i in range(len(splitRXFinal)):
                # check interaction with dictionary and pass through split rx final
                interactions = dict_drugs[splitRXFinal[i]].check_interaction(splitRXFinal)


            print("Checking presriptions for",person,"who suffers from",ConditionFinal,
                      "\nCurrent Rx:",RXFinal)

            if interactions == []:
                print("No serious drug interactions found in Rx.\n")

            else:
                print("Warning drug drug interaction between",splitRXFinal[0],"and",splitRXFinal[1],"\n")



main()