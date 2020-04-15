'''
Connor Mentel
CS 5001
HW 6
Programming 1
rxdrug.py
'''

class RxDrug:
    def __init__(self, name, rx_ID, interactions):
        self.name = name
        self.rx_ID = rx_ID
        self.description = ''
        self.interactions = interactions

    def add_interactions(self, other_drug):

        # if other drug is not in our interactions list, adds other_drug to our interactions list
        # add drugs that drug interacts with to list

        if other_drug not in self.interactions:
            self.interactions.append(other_drug)


    def check_interaction(self, other_drugs):
        self.yes_list = []
        for i in other_drugs:
            if i in self.interactions:
                self.yes_list.append(i)
        return self.yes_list

        # given a list of drugs that possibly interact with
        # return a list containing the names of the drugs that we actually match with from the list passed in


    def set_description(self,description):
        self.description = description


    def __str__(self):
        if self.interactions == []:
            return "No serious drug interactions found in Rx."

        return "Warning drug drug interaction between " + self.name + "and " + str(self.interactions)

