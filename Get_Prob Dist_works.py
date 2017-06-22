#### This works till getting individual prob distributions

import numpy as np
import pandas as pd

def sort_uniq(data_inp,i):

    mydata_tran = np.transpose(data_inp)
    my_list = [row[i] for row in mydata_tran] 
    ret_my_list = np.unique(np.sort(np.asarray(my_list)))
    return ret_my_list

df=pd.read_csv('C:/Kiru/Official/Markov/Python Programs/Cartersian product/Files/Old_Exec_Q_2.csv', sep=',',header=0)
a_mydata = df.values

mydata =[]
nums = 0
temp = np.transpose(a_mydata)
temp_n = (len(temp[0]))
while nums < temp_n:
    mydata = np.append(mydata,a_mydata[nums])
    nums +=1
i=0

mydata_tran = np.transpose(a_mydata)
u_test_case_arr = np.asarray(sort_uniq(mydata_tran,0))
u_date_arr = np.asarray(sort_uniq(mydata_tran,1))
u_stat_arr = np.asarray(sort_uniq(mydata_tran,2))

xy = 0
b=0
base_matrix = ["NR" for x in u_test_case_arr]
date_temp_list = base_matrix 
to_app_base_matrix=[]
while xy < len(u_date_arr):    
    while b  <= (len(u_test_case_arr)-1):
        for index in range(len(mydata)):
            if u_test_case_arr[b] == mydata[index]:
                if mydata [index+1] == u_date_arr[xy]:
                    date_temp_list[b] = mydata[index+2]
                    break                       
        b +=1
    to_app_base_matrix= np.append(to_app_base_matrix,date_temp_list)
    b=0
    xy +=1
final_matrix = ["NR" for x in u_test_case_arr]
final_matrix = np.append(final_matrix,to_app_base_matrix)
final_matrix = np.reshape(final_matrix,((len(u_date_arr)+1),len(u_test_case_arr)))
print("final matrix",(final_matrix))

###############################################################################
####Totals of state change test cases by date based on the final matrix
indx_var = 0
indx_var_list = []
u_stat_arr_wNR = ["NR"]
u_stat_arr_wNR = np.append(u_stat_arr_wNR,u_stat_arr)
for st in u_stat_arr_wNR:
    indx_var_list  = np.append(indx_var_list,indx_var)
    indx_var += 1
p_date_arr = []
c_date_arr = []
a = 1
tot_list=len(u_date_arr)*len(u_stat_arr)
print(tot_list, "total list")
target_arr_arr = []

while a <= len(u_date_arr):
    target_arr = np.zeros((len(u_stat_arr)+1)*(len(u_stat_arr)+1))    
    to_update = 0
    p_date_arr = final_matrix[a-1]
    c_date_arr = final_matrix[a]
    c_date_arr = np.asarray(c_date_arr)
    aa = 0
    bb = 0
    print("For Date:", u_date_arr[a-1])
    while aa < len(c_date_arr):
        row_index=[i for i, j in enumerate(u_stat_arr_wNR) if j == c_date_arr[aa]]
        col_index=[i for i, j in enumerate(u_stat_arr_wNR) if j == p_date_arr[aa]]
        to_update = ((1+len(u_stat_arr))*col_index[0]) + row_index[0]
        target_arr[to_update] += 1        
        aa += 1
    target_arr_arr = np.append(target_arr_arr,target_arr)
    a +=1
target_arr_arr = np.reshape(target_arr_arr,((a-1),((len(u_stat_arr)+1)*(len(u_stat_arr)+1))))
print("Checkpoint Uploaded to file...")
np.savetxt('C:/Kiru/Official/Markov/Python Programs/Cartersian product/Files/Out.csv', target_arr_arr, delimiter=',',fmt='%d')

###############################################################################
#####Relative prob calculation


U_Stat = u_stat_arr_wNR
#State_Change_arr = np.append([30,0,0,5,0,1,2],[100,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0])
State_Change_arr = target_arr_arr
State_Change_arr  = np.ndarray.flatten(State_Change_arr)

State_Change_arr = np.asarray(State_Change_arr,dtype = float)

Old_Relprob_arr = []

num_schange = int(len(State_Change_arr)/len(U_Stat))
num_statuses = len(U_Stat)
num_statuses_str = str(num_statuses)


x = 0
i = 0
my_indv = 0
while x <= (num_schange-1):

    start = x*num_statuses
    end = start + num_statuses
    split_st_ch_arr = State_Change_arr[start:end]
    split_st_ch_arr_dup = State_Change_arr[start:end]
    mylist = sum(int(a) for a in split_st_ch_arr)
    mylist_arr = np.asarray(mylist, dtype= float)
    
    while i < (num_statuses):
        
        a = split_st_ch_arr[i]
        b = sum(int(a) for a in split_st_ch_arr_dup)
        print(a,b)
        my_indv = round((a / b),4)
        a = split_st_ch_arr[i]
        b = sum(int(a) for a in split_st_ch_arr_dup)
        
        if b == 0: 
            b = 1
        
        my_indv = a/b
        my_indv_arr = np.asarray(my_indv)
        Old_Relprob_arr = np.append(Old_Relprob_arr,my_indv)
        i +=1
    i = 0
    x = x +1


print("Relative Prob Dist output on file...")
np.savetxt('C:/Kiru/Official/Markov/Python Programs/Cartersian product/Files/Old_Relprob_arr.csv', Old_Relprob_arr, delimiter=',',fmt='%f')


