#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Connor Mentel
CS 5001
HW 2
Programming #1
Using Functions
"""
#Imports
from Hurricane.haversine import haversine
from datetime import date

#Define Coordinates and Variables
lat1 = float(27.1) #Dorian Lat
lon1 = float(-78.4) #Dorian Lon
lat2 = float(42.361145) #Boston Lat
lon2 = float(-71.057083) #Boston Lon
lat3 = float(25.761681) #Miami Lat
lon3 = float(-80.191788) #Miami Lon
Today = date.today() #Today's date

#Defining functions    
def other(): #If user selects "O"
     name = str(input(("What is the name of the city? ")))
     print("\nYour city is", name)
     
     lat4 = input("What is the latitude (decimal degrees?) ")
     print("\nYour Latitude is ",float(lat4))
     
     lon4 = input("What is the longitude (decimal degrees?) ")
     print("\nYour Longitude is ",float(lon4))
     
     print("\nHurricane Dorian was",round(float(newh(lat4, lon4)),2),
           "nautical miles from ",
           name,)
     zoot = newh(lat4, lon4)
     if (zoot < 150):
         print ("/nWARNING! You are in the hurricane zone! Seek shelter now!")
     else:(print ("You are in a safe zone."))
     
def newh(lat4,lon4): #Haversine for "O" selection
    return haversine(float(lat1), float(lon1), float(lat4), float(lon4))
    
def main():
    #Greeting
    print("\nWelcome to the hurricane tracker and warning system!")
    
    #Initial Question
    Q1 = input(str('''Enter the location to apply our radar:
        B for Boston
        M for Miami
        O for another location of your choice
        B, M, or O? '''))
        
    #Boston
    if (Q1 == "B" or Q1 == "b") :
        print("\nHurricane Dorian was " , 
              round(haversine(int(lat1) , int(lon1) , int(lat2) , int(lon2)),2),
              " nautical miles from Boston on 03-Sept-2019"
              "\nBoston was not in the hurricane zone.")
    #Miami
    elif(Q1 == "M" or Q1 == "m") :
        print("\nHurricane Dorian was ", 
              round(haversine(int(lat1) , int(lon1) , int(lat3) , int(lon3)),2),
              " nautical miles from Miami on 03-Sept-2019")
        print("\nWARNING! Miami was in the hurricane zone! Seek shelter now!")
                  
    #Other
    elif(Q1 == "O" or Q1 == "o") :
        other()

    #None
    else:
        print("\nPlease select an option from above :)")
             
main()