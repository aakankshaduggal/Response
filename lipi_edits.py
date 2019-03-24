
# coding: utf-8




import csv
import random

with open('affirmationdata.csv') as f:
    reader = csv.reader(f)
    l = list(reader)
    chosen_row1 = random.choice(l)[1]
    chosen_row2 = random.choice(l)[1]
    chosen_row3 = random.choice(l)[1]
    
neutral = ["Okay","Alright","Good going", "Tell me more", "Sounds good", "Great", "Umhmm", "You gotta do what you gotta do"]



"""input data
    type of personality: 1=more response,2=moderate,3=light response
    sentiment between -1 to 1
"""
def generatedRes(persona,sentiment):
    if not(sentiment==0):
        if(persona==1):
            return chosen_row1+". "+chosen_row2+". "+chosen_row3
        elif(persona==2):
            return chosen_row1+". "+chosen_row2
        else:
            return chosen_row1
    else:
        return random.choice(neutral)
        

print(generatedRes(2,0.6))
print(generatedRes(1,-0.6))




