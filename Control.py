import pandas as pd
import numpy as np
import traceback
Cl_H = []
Cl_M = []
Cl_L = []
deficient_b = []
Ac = 0.0
Rec = 0.0
Rc_H = 0.0
Rc_L = 0.0
Rc_M = 0.0
#Calculate reserve capacities
def Reserve_cap(building_id,asset_id,customer_id):
 Rc = [5,5,10,2,5,5,5]
 H_Cl , M_Cl , L_Cl = Clusters(building_id,cutomer_id)
 i = 0
 while(i < np.len(H_Cl)):
    Rc_H = np.sum(Rc[H_Cl],Rc_H)
    i = i+1
 i = 0
 while(i < np.len(M_Cl)):
    Rc_M = np.sum(Rc[M_Cl],Rc_M)
 i = i+1

 i = 0
 while(i < np.len(L_Cl)):
    Rc_L = np.sum(Rc[L_Cl],Rc_L)
    i = i+1
 return Rc_H,Rc_M,Rc_L,H_Cl,M_Cl,L_Cl

#Clustering the assets based on the their maximum activation capacities
def Clusters(building_id,customer_id):
    Cl_H = 3
    Cl_M = [1,2,6,7,8]
    Cl_L = 5
    return Cl_H,Cl_M,Cl_L

def Reactive_Control(Ac,Rc,Rec,building_id):
#check if the real capacities is equal to the activated capacity. This inequality will decide to activate the RC
 if(Rec-Ac) != 0 :
   def_p = Rec-Ac
   while( flag == 0 and (building_id < 9)):
        building_id = 1
        if (Recb[building_id] != Ac[building_id]):
            temp = (Recb[building_id] - Ac[building_id])
            flag = building_id
            np.append(deficient_b,buidling_id)
        return temp
 building_id = building_id + 1
 Rc_h, Rc_m,Rc_l,H_cl,M_cl,L_cl = Reserve_cap(building_id)
 if (temp <= Rc_h):
        l = np.len(H_cl)
        Ac_cap = (temp/l)
        #Code to write it to the FCR-N table

 if (temp <= (Rc_h + Rc_m)):
    l = np.len(M_cl)
    lower_capacity = temp - Rc_h
    Ac_cap = (lower_capacity/l)
    #Send Rc_H/(np.len(H_cl))  for the batteries in the high cluster and Ac_cap for the lower cluster
    #Write the code here
 if (temp <= (Rc_h+Rc_m +Rc_l)):
     Capacity_low = temp - (Rc_h + Rc_m)
     l = np.len(L_cl)
     Ac_cap = (Capacity_low/l)
     #Send Rc_H/np.len(H_cl) for high cluster batteries and Rc_l/np.len(M_cl) for med cluster batteries
     #write the code here
 if(temp > (Rc_h+Rc_m+Rc_l)):
     print('Game over')

 return flag