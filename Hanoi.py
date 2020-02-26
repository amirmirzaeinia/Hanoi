
'''
This code finds the number of moves to return a random disk distribution to first rod. 
all the Hanoi conditions are applied.
# R is number of rods
# disks_distribution is an array that shows location of that disk. for example if R=3 and disks_distribution=[0,1,2], 
#it means largest disk on rod 0, second largest on rod 1 and the smalest disk on rod 2.
sample output for
R=4 
disks_distribution =[1,2,0,
                     1,3,0,
                     3,2,1,
                     1,0,3,
                     2]
output=
[[2, 5, 10], [0, 3, 8, 9], [1, 7, 12], [4, 6, 11]]
[[2, 5, 10], [3, 8, 9], [0, 1, 7, 12], [4, 6, 11]]
[[0, 1, 2, 5, 10], [3, 8, 9], [7, 12], [4, 6, 11]]
[[5, 10], [0, 1, 2, 3, 8, 9], [7, 12], [4, 6, 11]]
[[5, 10], [8, 9], [7, 12], [0, 1, 2, 3, 4, 6, 11]]
[[0, 1, 2, 3, 4, 5, 10], [8, 9], [7, 12], [6, 11]]
[[10], [8, 9], [7, 12], [0, 1, 2, 3, 4, 5, 6, 11]]
[[10], [8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 12], [11]]
[[10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [12], [11]]
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [12], [11]]
[[], [], [12], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
[[], [], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], []]
move_counter:7667
'''

 



 
def top_finder(all_rod, top):

    counter =0
    for rod in all_rod: 
        counter +=1
        if (len(rod) > 0):
            if (rod[0] == top):
                return counter-1
        elif (len(rod) == 0):
            continue

        

def sort_finder(rod):
    sorted_length=0
    for i in range(1,len(rod)):
        if (rod[i]- rod[i-1]) == 1:
            sorted_length +=1
        else:
            return sorted_length + 1
        
        if (sorted_length == (len(rod) - 1)) :
            return len(rod)       
     
    
    


#Q1
#R=4
#disks_distribution = [0,1,1,0]
            
#Q2
#R=3
#disks_distribution =[1,2,0,
#                     1,1,0,
#                     2,2,1,
#                     1,2,1,
#                     1,0,2]
#Q3
#R=4 
#disks_distribution =[1,2,0,1,3,0,3,2,1,1,0,3,2,2]
#Q4
#R=3
#disks_distribution =[1,2,0,
#                     1,1,0,
#                     2,2,1,
#                     1]
#Q5
#R=4 
#disks_distribution =[1,2,0,
#                     1,1,0,
#                     2,2,1,
#                     1]
#Q6
R=4 
disks_distribution =[1,2,0,
                     1,3,0,
                     3,2,1,
                     1,0,3,
                     2]


all_rod=[]
for i in range (R):
    all_rod.append([]) 


for i in range(len(disks_distribution)):
    all_rod[disks_distribution[i]].append(i)


#print(all_rod)
i = 0
move_counter=0
src_rod = top_finder(all_rod, i)
print(all_rod)

while i <  len(disks_distribution)-1:
    i=0
    
    sorted_length = sort_finder(all_rod[src_rod])
    i+=sorted_length 
    dest_rod = top_finder(all_rod, i)
    
    if sorted_length == len(disks_distribution):
        if src_rod !=0:
            move_counter += 2** len(disks_distribution)-1
                
        break
    
    
    
    tmp=[]

    
    
    for k in range(sorted_length):
        tmp.append(all_rod[src_rod].pop(0))
        all_rod[dest_rod].insert(k, tmp[k])
    
    
    print(all_rod) 
    src_rod =  dest_rod  
    move_counter += 2 ** sorted_length -1

print("move_counter:"+str(move_counter))    
    
