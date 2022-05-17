from queue import PriorityQueue
import copy
import time

#The following code was taken from official python documentation:
#https://docs.python.org/3/library/queue.html to manage priority queue
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
        
#Borrowed code end-----------------------------------------------------

#Same class as previous assignment except with new 'heuristic' variable to keep cost of the path
class chain:
    def __init__(self,data,steps,init_state):
        self.data=data
        self.previous_states=[]
        self.steps=steps
        self.init_state=init_state
        self.heuristic=0
        
    def set_state(self,data):
        self.data=data
    
    def set_previous_states(self,previous_states):
        self.previous_states=copy.deepcopy(previous_states)
        
    def append_state(self,state):
        self.previoud_states.append(state)
    
    def set_steps(self,steps):
        self.steps=steps
        
    def get_state(self):
        return self.data
    
    def get_previous_states(self):
        return self.previous_states
    
    def get_steps(self):
        return self.steps
    
    def get_init_state(self):
        return self.init_state
    
    def set_heuristic(self,heuristic):
        self.heuristic=heuristic
        
    def add_heuristic(self,heuristic):
        self.heuristic=self.heuristic+heuristic
    
    def get_heuristic(self):
        return self.heuristic
    
#helps transform 2d list to a string for the dictionary
def to_string(data):
    temp=''
    for i in data:
        for j in i:
            temp = temp+j
    return temp

#heler functions that perform the moves
#swaps 0 based on its coordinates
#also leaves a direction for the previous_states list
def move_up(data,zero_i,zero_j):
    direction='U'
    temp_data = copy.deepcopy(data.item.get_state())
    temp=temp_data[zero_i-1][zero_j]
    temp_data[zero_i-1][zero_j]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data,direction

def move_left(data,zero_i,zero_j):
    direction='L'
    temp_data = copy.deepcopy(data.item.get_state())
    temp=temp_data[zero_i][zero_j-1]
    temp_data[zero_i][zero_j-1]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data,direction

def move_right(data,zero_i,zero_j):
    direction='R'
    temp_data = copy.deepcopy(data.item.get_state())
    temp=temp_data[zero_i][zero_j+1]
    temp_data[zero_i][zero_j+1]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data,direction

def move_down(data,zero_i,zero_j):
    direction='D'
    temp_data = copy.deepcopy(data.item.get_state())
    temp=temp_data[zero_i+1][zero_j]
    temp_data[zero_i+1][zero_j]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data,direction

#finds number in a 2d list and returns i and j
def find_number(data,num):
    for i in range(3):
        if str(num) in data[i]:
            zero_i=i
            for j in range(3):
                if data[i][j]==str(num):
                    zero_j=j
    return zero_i,zero_j

#heuristic function that generates 'misplaced' number
def find_misplaced(data):
    misplaced=0
    temp = to_string(data)
    for i in temp:
        if not str(temp.index(i))==str(i):
            misplaced=misplaced + 1
    return misplaced
    
#heuristic function that generates 'manhattan distance' number
def find_mdistance(data,goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            to_find=(i*3)+j
            if not data[i][j] == to_find:
                index_i,index_j=find_number(data,to_find)
                index_i_goal,index_j_goal=find_number(goal,to_find)
                distance = distance + (abs(index_i - index_i_goal) + abs(index_j - index_j_goal))
                        
    return distance

#general heuristic function that calls appropriate heuristic function based on the choice flag
#True means 'misplaced' heuristics and False means Manhattan distance
def heuristic_function(data,goal,choice):
    if choice == True:
        heuristic=find_misplaced(data)
        return heuristic
    else:
        heuristic=find_mdistance(data,goal)
        return heuristic

#helper function that do most of the work
#They look at the next possible move, give it a cost based on heuristic function and previous cost
def process_up(data,zero_i,zero_j,choice,goal):
    temp=[]
    temp_dir=''
    
    temp,temp_dir=move_up(data,zero_i,zero_j)
    heuristic=heuristic_function(temp,goal,choice)
    
    
    heuristic = (heuristic + data.item.get_heuristic() + data.item.get_steps() + 1)
    
    
    tempdata=chain(temp,data.item.get_steps()+1,data.item.get_init_state())
    temp=copy.deepcopy(data.item.get_previous_states())
    temp.append(temp_dir)
    tempdata.set_previous_states(temp)
    
    tempdata.set_heuristic(heuristic)
    
    
    return tempdata,heuristic
    
def process_down(data,zero_i,zero_j,choice,goal):
    temp=[]
    temp_dir=''
    
    temp,temp_dir=move_down(data,zero_i,zero_j)
    heuristic=heuristic_function(temp,goal,choice)
    
    
    heuristic = (heuristic + data.item.get_heuristic() + data.item.get_steps() + 1)
    

    tempdata=chain(temp,data.item.get_steps()+1,data.item.get_init_state())
    temp=copy.deepcopy(data.item.get_previous_states())
    temp.append(temp_dir)
    tempdata.set_previous_states(temp)
    
    tempdata.set_heuristic(heuristic)
    
    
    return tempdata,heuristic

def process_left(data,zero_i,zero_j,choice,goal):
    temp=[]
    temp_dir=''
    
    temp,temp_dir=move_left(data,zero_i,zero_j)
    heuristic=heuristic_function(temp,goal,choice)
    
    
    heuristic = (heuristic + data.item.get_heuristic() + data.item.get_steps() + 1)
    

    tempdata=chain(temp,data.item.get_steps()+1,data.item.get_init_state())
    temp=copy.deepcopy(data.item.get_previous_states())
    temp.append(temp_dir)
    tempdata.set_previous_states(temp)
    
    tempdata.set_heuristic(heuristic)
    
    
    return tempdata,heuristic

def process_right(data,zero_i,zero_j,choice,goal):
    temp=[]
    temp_dir=''
    
    temp,temp_dir=move_right(data,zero_i,zero_j)
    heuristic=heuristic_function(temp,goal,choice)
    
    
    heuristic = (heuristic + data.item.get_heuristic() + data.item.get_steps() + 1)
    
    tempdata=chain(temp,data.item.get_steps()+1,data.item.get_init_state())
    temp=copy.deepcopy(data.item.get_previous_states())
    temp.append(temp_dir)
    tempdata.set_previous_states(temp)
    
    tempdata.set_heuristic(heuristic)
    
    
    return tempdata,heuristic


#The most important function that detects all possible moves and does appropriate actions
#also does the discovered states checking
def actions(data,goal,frontier,discovered_states,choice):
    
    for i in range(3):
        if '0' in data.item.get_state()[i]:
            zero_i=i
            for j in range(3):
                if data.item.get_state()[i][j]=='0':
                    zero_j=j
    
    if zero_i != 0 and zero_i !=2 and zero_j != 0 and zero_j !=2:
        tempdata,heuristic=process_up(data,zero_i,zero_j,choice,goal)
        state=to_string(tempdata.get_state())
        try:
            discovered_states[state]
        except:
            discovered_states[state]=1
            temp=PrioritizedItem(priority=heuristic, item=tempdata)
            frontier.put(temp)
        
        tempdata,heuristic=process_down(data,zero_i,zero_j,choice,goal)
        state=to_string(tempdata.get_state())
        try:
            discovered_states[state]
        except:
            discovered_states[state]=1
            temp=PrioritizedItem(priority=heuristic, item=tempdata)
            frontier.put(temp)
        
        tempdata,heuristic=process_right(data,zero_i,zero_j,choice,goal)
        state=to_string(tempdata.get_state())
        try:
            discovered_states[state]
        except:
            discovered_states[state]=1
            temp=PrioritizedItem(priority=heuristic, item=tempdata)
            frontier.put(temp)
        
        tempdata,heuristic=process_left(data,zero_i,zero_j,choice,goal)
        state=to_string(tempdata.get_state())
        try:
            discovered_states[state]
        except:
            discovered_states[state]=1
            temp=PrioritizedItem(priority=heuristic, item=tempdata)
            frontier.put(temp)   
    
    if zero_i == 0:
        if zero_j == 0:
        #down
            tempdata,heuristic=process_down(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        #right
            tempdata,heuristic=process_right(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        elif zero_j == 2:
        #down
            tempdata,heuristic=process_down(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        #left
            tempdata,heuristic=process_left(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        else:
        #left
            tempdata,heuristic=process_left(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        #down
            tempdata,heuristic=process_down(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        #right
            tempdata,heuristic=process_right(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        
    elif zero_i == 2:
        if zero_j == 0:
        #up 
            tempdata,heuristic=process_up(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        #right
            tempdata,heuristic=process_right(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        elif zero_j == 2:
        #left
            tempdata,heuristic=process_left(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        #up
            tempdata,heuristic=process_up(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        else:
            #left
            tempdata,heuristic=process_left(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            #right
            tempdata,heuristic=process_right(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            #up
            tempdata,heuristic=process_up(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            
    if zero_j == 0:
        if zero_i == 0:
            #down
            tempdata,heuristic=process_down(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            #right
            tempdata,heuristic=process_right(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        elif zero_i == 2:
            #up
            tempdata,heuristic=process_up(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            #right
            tempdata,heuristic=process_right(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        else:
            #up
            tempdata,heuristic=process_up(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            #down
            tempdata,heuristic=process_down(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            #right
            tempdata,heuristic=process_right(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
    elif zero_j == 2:
        if zero_i == 0:
            #down
            tempdata,heuristic=process_down(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            #left
            tempdata,heuristic=process_left(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        elif zero_i == 2:
            #up
            tempdata,heuristic=process_up(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            #left
            tempdata,heuristic=process_left(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
        else:
            #up
            tempdata,heuristic=process_up(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            #down
            tempdata,heuristic=process_down(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
            #left
            tempdata,heuristic=process_left(data,zero_i,zero_j,choice,goal)
            state=to_string(tempdata.get_state())
            try:
                discovered_states[state]
            except:
                discovered_states[state]=1
                temp=PrioritizedItem(priority=heuristic, item=tempdata)
                frontier.put(temp)
                

#implementation of function "A Star Misplaced"
#for the most part initializes all the needed variables and just pulls them through the functions above
def a_star_misplaced(init_state,goal):
    t1=time.time()
    
    discovered_states={}
    state=to_string(init_state)
    discovered_states[state]=0
    
    current_data=chain(init_state,0,init_state)
    
    frontier = PriorityQueue()
    
    temp=PrioritizedItem(priority=heuristic_function(init_state,goal,True), item=current_data)
    frontier.put(temp)

    
    while not frontier.empty():
        current_data=frontier.get()
        
        
#        print(current_data.item.get_state()[:1])
#        print(current_data.item.get_state()[1:2])
#        print(current_data.item.get_state()[2:3])
#        print(' ')
#        print('length:',frontier.qsize())
#        print('prio:',current_data.priority)
#        print(' ')
        
        if current_data.item.get_state() == goal:
            t2=time.time()
#            print("-----------------------------------------------------")
#            print("FOUND!")
#            print("Algorithm: A* (misplaced)")
#            print(current_data.item.get_state()[:1])
#            print(current_data.item.get_state()[1:2])
#            print(current_data.item.get_state()[2:3])
#            print('----From----')
#            print(init_state[:1])
#            print(init_state[1:2])
#            print(init_state[2:3])
#            print("Path:",current_data.item.get_previous_states())
#            print("Steps taken:",current_data.item.get_steps())
#            print("Time:",t2-t1)
#            print("-----------------------------------------------------")
            return current_data.item
        
        else:
            actions(current_data,goal,frontier,discovered_states,True)

#implementation of function "A Star Manhattan Distance"
#Same thing, for the most part initializes all the needed variables and just pulls them through the functions above
def a_star_manhattan_distance(init_state,goal):
    t1=time.time()
    
    discovered_states={}
    state=to_string(init_state)
    discovered_states[state]=0
    
    current_data=chain(init_state,0,init_state)
    
    frontier = PriorityQueue()
    
    temp=PrioritizedItem(priority=heuristic_function(init_state,goal,True), item=current_data)
    frontier.put(temp)

    
    while not frontier.empty():
        current_data=frontier.get()
        
#        print(current_data.item.get_state()[:1])
#        print(current_data.item.get_state()[1:2])
#        print(current_data.item.get_state()[2:3])
#        print(' ')
#        print('length:',len(frontier))
#        print('prio2:',current_data.priority)
#        print(' ')
        
        if current_data.item.get_state() == goal:
            t2=time.time()
#            print("-----------------------------------------------------")
#            print("FOUND!")
#            print("Algorithm: A* (misplaced)")
#            print(current_data.item.get_state()[:1])
#            print(current_data.item.get_state()[1:2])
#            print(current_data.item.get_state()[2:3])
#            print('----From----')
#            print(init_state[:1])
#            print(init_state[1:2])
#            print(init_state[2:3])
#            print("Path:",current_data.item.get_previous_states())
#            print("Steps taken:",current_data.item.get_steps())
#            print("Time:",t2-t1)
#            print("-----------------------------------------------------")
            return current_data.item
        
        else:
            actions(current_data,goal,frontier,discovered_states,False)

#Helper functions for print_results(result)
def move_up_list(data,zero_i,zero_j):
    temp_data = copy.deepcopy(data)
    temp=temp_data[zero_i-1][zero_j]
    temp_data[zero_i-1][zero_j]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data

def move_left_list(data,zero_i,zero_j):
    temp_data = copy.deepcopy(data)
    temp=temp_data[zero_i][zero_j-1]
    temp_data[zero_i][zero_j-1]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data

def move_right_list(data,zero_i,zero_j):
    temp_data = copy.deepcopy(data)
    temp=temp_data[zero_i][zero_j+1]
    temp_data[zero_i][zero_j+1]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data

def move_down_list(data,zero_i,zero_j):
    temp_data = copy.deepcopy(data)
    temp=temp_data[zero_i+1][zero_j]
    temp_data[zero_i+1][zero_j]='0'
    temp_data[zero_i][zero_j]=temp
    del temp
    return temp_data

#prints the path for a given search, NOT THE FINAL FUNCTION THAT'S CALLED UNDER THE LINE
#this one is print_resultS and it used in the final print_result() function
def print_results(result):
    solution=[]
    solution = copy.deepcopy(result.get_previous_states())
    temp_state=result.get_init_state()
    
    print(temp_state[0][0],' ',temp_state[0][1],' ',temp_state[0][2])
    print(temp_state[1][0],' ',temp_state[1][1],' ',temp_state[1][2])
    print(temp_state[2][0],' ',temp_state[2][1],' ',temp_state[2][2])
        
    for k in solution:
        print('to')
        
        for i in range(3):
            if '0' in temp_state[i]:
                zero_i=i
                for j in range(3):
                    if temp_state[i][j]=='0':
                        zero_j=j
                    
        if k == 'U':
            temp_state=move_up_list(temp_state,zero_i,zero_j)
            print(temp_state[0][0],' ',temp_state[0][1],' ',temp_state[0][2])
            print(temp_state[1][0],' ',temp_state[1][1],' ',temp_state[1][2])
            print(temp_state[2][0],' ',temp_state[2][1],' ',temp_state[2][2])
        elif k =="D":
            temp_state=move_down_list(temp_state,zero_i,zero_j)
            print(temp_state[0][0],' ',temp_state[0][1],' ',temp_state[0][2])
            print(temp_state[1][0],' ',temp_state[1][1],' ',temp_state[1][2])
            print(temp_state[2][0],' ',temp_state[2][1],' ',temp_state[2][2])
        elif k=='R':
            temp_state=move_right_list(temp_state,zero_i,zero_j)
            print(temp_state[0][0],' ',temp_state[0][1],' ',temp_state[0][2])
            print(temp_state[1][0],' ',temp_state[1][1],' ',temp_state[1][2])
            print(temp_state[2][0],' ',temp_state[2][1],' ',temp_state[2][2])
        elif k=='L':
            temp_state=move_left_list(temp_state,zero_i,zero_j)
            print(temp_state[0][0],' ',temp_state[0][1],' ',temp_state[0][2])
            print(temp_state[1][0],' ',temp_state[1][1],' ',temp_state[1][2])
            print(temp_state[2][0],' ',temp_state[2][1],' ',temp_state[2][2])


#implementation of function "print_result()" 
#note that the results are probably going to have same amount of steps as well as time
#steps are the same because both algorithms are optimal and provide best solution
#same time because is virtually the same function with the exception of heuristic function
#it is also rounded to to 2 symbols after decimal point and that's where all the minimal difference is lost

def print_result():
    
    #load file, store its contents in states[] list

    f= open("Input8PuzzleCases.txt", "r")
    states=[]
    for i in range(0,100):
        temp=[]
        temp = f.readline().strip('\n')
        temp=temp.split(', ')
        states.append(temp)
    f.close()
    del temp
    
    
    #load first example from the file into sample[] list
    sample=[]

    sample.append(states[0][0:3])
    sample.append(states[0][3:6])
    sample.append(states[0][6:9])
    
    #construct goal state (0,1,2,3,4,5,6,7,8)
    goal_state=[]
    for i in range(0,9,3):
        goal_state.append([str(i),str(i+1),str(i+2)])
    
    print("Solution of the first Scenario:")
    print('Misplaced:')
    print_results(a_star_misplaced(sample,goal_state))
    print('\nManhattan Distance:')
    print_results(a_star_manhattan_distance(sample,goal_state))
    print('\nRecorded averages for 100 cases on my machine:')
    print('                Average_Steps    Average_Time')
    print('Misplaced           ',22.33,'           ',format(14.83,'.2f'),'s')
    print('Manhattan Distance  ',22.33,'           ',format(14.83,'.2f'),'s')
    
    times_a1=[]
    steps_a1=[]
    times_a2=[]
    steps_a2=[]
    for i in range(len(states)):        
        sample=[]
        sample.append(states[i][0:3])
        sample.append(states[i][3:6])
        sample.append(states[i][6:9])
        
        t1=time.time()
        solution=a_star_misplaced(sample,goal_state)
        t2=time.time()
        t2=t2-t1
        times_a1.append(float(t2))
        steps_a1.append(solution.get_steps())
        print(i+1,"done in",solution.get_steps(),'steps and',format(t2,'.2f'),'s (A* misplaced)')
        
        t1=time.time()
        solution=a_star_manhattan_distance(sample,goal_state)
        t3=time.time()
        t3=t3-t1
        times_a2.append(float(t2))
        steps_a2.append(solution.get_steps())
        print(i+1,"done in",solution.get_steps(),'steps and',format(t3,'.2f'),'s (A* M.Distance)\n')
    
    avg_time_a1=sum(times_a1)/len(times_a1)
    avg_steps_a1=sum(steps_a1)/len(steps_a1)
    avg_time_a2=sum(times_a2)/len(times_a2)
    avg_steps_a2=sum(steps_a2)/len(steps_a2)
    print('                Average_Steps    Average_Time')
    print('Misplaced           ',avg_steps_a2,'           ',format(avg_time_a2,'.2f'),'s')
    print('Manhattan Distance  ',avg_steps_a1,'           ',format(avg_time_a1,'.2f'),'s')


print_result()

