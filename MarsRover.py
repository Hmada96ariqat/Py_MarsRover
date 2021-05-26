import pandas as pd
import math

#This function is for removing '/n' from the data 
def strip(movement_list):


    for counter in range(len(movement_list)):

        if movement_list[counter][1].rstrip().isdigit():
            movement_list[counter][1] = int(movement_list[counter][1])
        else:
            movement_list[counter][1] = movement_list[counter][1].rstrip()
    return movement_list

#This funtion is for choosing which operation you want to perform
def distance_in_meters(A, B, C, D):


    def switch(x):

        choosing = {1 :  getAngle(A, C),
                    2 :  getAngle(D, C),
                    3 :  getAngle(C, B),
                    4 :  getAngle(A, D)
                   }
        return choosing.get(x, 'Invalid input, please re-enter a valid number')
    print(switch(int(input(' 1-AtoC \n 2-DtoC \n 3-CtoB \n 4-AtoD \n'))))


#This function is for getting the angle to calculate
    #x = x1 + distance * cos(angle * (pi/180))
        #Where x1 is the previous x
        #Distance is the travelled value
def getAngle(x, y):
    
    
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    sin_1 = 0
    cos_1 = 0
    cos_2 = 0
    left = 0
    right = 0
    forward = 0
    #This 1st solution taking 2 direction wether left and forward
        #Or right and forward
    #If left then forward so the car should just move to the left side
        #and the move forward with respect to the angle's value, which is the value of left or right
    for i in range(len(x)):
        
        if x[i][0] == 'left':  
            left = x[i][1]
        elif x[i][0] == 'forward':
            forward = x[i][1]
            x1 = x1 + forward * math.cos(left * (3.14/180))
            y1 = y1 + forward * math.sin(left * (3.14/180))

        if x[i][0] == 'right':  
            right = x[i][1]
        elif x[i][0] == 'forward':
            forward = x[i][1]
            x1 = x1 + forward * math.cos(-right * (3.14/180))
            y1 = y1 + forward * math.sin(-right * (3.14/180))

    for i in range(len(y)):
        if y[i][0] == 'left':  
            left = y[i][1]
        elif y[i][0] == 'forward':
            forward = y[i][1]
            x2 = x2 + forward * math.cos(left * (3.14/180))
            y2 = y2 + forward * math.sin(left * (3.14/180))

        if y[i][0] == 'right':  
            right = y[i][1]
        elif y[i][0] == 'forward':
            forward = y[i][1]
            x2 = x2 + forward * math.cos(-right * (3.14/180))
            y2 = y2 + forward * math.sin(-right * (3.14/180))

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    #This 2nd solution is for assuming the circle has 4 quartar 
        #The first one is +90 which is left side of the cirlce
        #The second one is -90 which is left side of the circle
        #The third one is 0 which is forward
#     for i in range(len(x)):
#         if x[i][0] == 'left':
#             cos_1 = x[i][1]
#             x1 = x1 + cos_1 * math.cos((+90) * (3.14/180))
#         elif x[i][0] == 'right':
#             cos_2 = x[i][1]
#             x1 = x1 + cos_2 * math.cos((-90) * (3.14/180))
#         elif x[i][0] == 'forward':
#             sin_1 = x[i][1]
#             y1 = y1 + sin_1 * math.sin((0) * (3.14/180))

#     for i in range(len(y)):
#         if y[i][0] == 'left':
#             cos_1 = y[i][1]
#             x2 = x2 + cos_1 * math.cos((+90) * (3.14/180))
#         elif y[i][0] == 'right':
#             cos_2 = y[i][1]
#             x2 = x2 + cos_2 * math.cos((-90) * (3.14/180))
#         elif y[i][0] == 'forward':
#             sin_1 = y[i][1]
#             y2 = y2 + sin_1 * math.sin((0) * (3.14/180))

    #Euclidean method
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distance


def distance_travelled(A, C):


    def switch(x):

        choosing = {1 : travelled(A, C)}
        return choosing.get(x)
    print(switch(int(input(' 1-AtoC \n'))))

#This function is for counting the forward for 2 markers
def travelled(x, y):


    sum_1 = 0
    sum_2 = 0

    for i in range(len(x)):
        if x[i][0] == 'forward':
            sum_1 = x[i][1] + sum_1

    for i in range(len(y)):
        if y[i][0] == 'forward':
            sum_2 = y[i][1] + sum_2
    return str(sum_2 + sum_1)

#Opening the file
file_open = open('C:/Users/hmada/FINISH/.ipynb_checkpoints/operations-checkpoint.csv', 'r')
list_ = [[], [], [], [], []]
list_df = pd.DataFrame(list_)
movement_list = []
move_df = pd.DataFrame(movement_list)
#extracting the data into list_[0]
list_[0] = file_open.readlines()

for storing_data in list_[0]:
    movement_list.append(storing_data.split(' '))
#stipping the data
movement_list = strip(movement_list)
for a_counter in range(len(movement_list)):
    list_[1].append(movement_list[a_counter])

    if movement_list[a_counter][1] == 'A':
        for b_counter in range(len(list_[1]),len(movement_list)):
            list_[2].append(movement_list[b_counter])

            if movement_list[b_counter][1] == 'B':
                for c_counter in range(len(list_[2]) + len(list_[1]), len(movement_list)):
                    list_[3].append(movement_list[c_counter])

                    if movement_list[c_counter][1] == 'C':
                        for d_counter in range(len(list_[2]) + len(list_[1]) + len(list_[3])
                                              ,len(movement_list)):
                            list_[4].append(movement_list[d_counter])

                        break
                break
        break

pick = input(' A-Meters \n B-Travelled \n')
if pick == 'A':
    distance_in_meters(list_[1], list_[2], list_[3], list_[4])
if pick == 'B':
    distance_travelled(list_[1], list_[3])
