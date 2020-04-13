import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import sys

n_cells=1550
x_min = 0.0
x_max = 100
y_min = 0.0
y_max = 100.0
z_min = 0.0
z_max = 50.0

#this assumes the script is already in the correct directory
mesh_name = 'mesh.uge'
def nan_image_connect(v1,v2):
    if (v1 <= n_cells) & (v2 <= n_cells):
        return v1
    else:
        return -99

mesh=pd.read_csv(mesh_name,sep='\s+',header=None,skiprows=1,index_col=0,nrows=n_cells)
mesh.columns = ['x','y','z','Volume','MatID']
print(mesh.head())
print(mesh.tail())
mesh_np=mesh.as_matrix()

file_name = 'out_'+ mesh_name
print('New mesh file name is:')
print(file_name)
#np.savetxt(file_name,conne,fmt='%5s')
#conne = ['CELLS '+ str(n_cells)]       
#np.savetxt(file_name,conne,fmt='%5s')
#this line prints columns as the first entry, which is indexed starting from 1
mesh.to_csv(file_name, columns=['x','y','z','Volume'], sep=' ',header=False,float_format='%1.15e')

########################
connect=np.genfromtxt(mesh_name,skip_header= n_cells+2)

len_connect = len(connect[:,0])
real_connect = np.zeros((len_connect,6))
smX_connect = np.zeros((len_connect,5))
lgX_connect = np.zeros((len_connect,5))
smY_connect = np.zeros((len_connect,5))
lgY_connect = np.zeros((len_connect,5))
smZ_connect = np.zeros((len_connect,5))
lgZ_connect = np.zeros((len_connect,5))
reassigned_v1 = np.zeros((len_connect))
reassigned_v2 = np.zeros((len_connect))
num_real = 0
num_smX = 0
num_lgX = 0
num_smY = 0
num_lgY = 0
num_smZ = 0
num_lgZ = 0
del_x = 1e-8
print('number of connections read')
for i in range(0,len_connect):
    bdry_claimed = 0
    if math.ceil(i/10000)==math.floor(i/10000):
        print(i)
        print(num_real)
    if (connect[i,0] != connect[i,1]):
        real_connect[num_real,:]=connect[i,0:6]
        num_real = num_real + 1
        bdry_claimed = 1
        
    if (connect[i,2] > x_max-del_x) & (connect[i,2] < x_max+del_x) & (connect[i,0] == connect[i,1]):
        lgX_connect[num_lgX,0]=connect[i,0]
        lgX_connect[num_lgX,1:5]=connect[i,2:6]
        num_lgX = num_lgX + 1
        bdry_claimed = 1
    if (connect[i,2] > x_min-del_x) & (connect[i,2] < x_min+del_x) & (connect[i,0] == connect[i,1]):
        smX_connect[num_smX,0]=connect[i,0]
        smX_connect[num_smX,1:5]=connect[i,2:6]
        num_smX = num_smX + 1
        bdry_claimed = 1

    if (connect[i,3] > y_max-del_x) & (connect[i,3] < y_max+del_x) & (connect[i,0] == connect[i,1]):
        lgY_connect[num_lgY,0]=connect[i,0]
        lgY_connect[num_lgY,1:5]=connect[i,2:6]
        num_lgY = num_lgY + 1
        bdry_claimed = 1
    if (connect[i,3] > y_min-del_x) & (connect[i,3] < y_min+del_x) & (connect[i,0] == connect[i,1]):
        smY_connect[num_smY,0]=connect[i,0]
        smY_connect[num_smY,1:5]=connect[i,2:6]
        num_smY = num_smY + 1
        bdry_claimed = 1


    if (connect[i,4] > z_max-del_x) & (connect[i,4] < z_max+del_x) & (connect[i,0] == connect[i,1]):
        #print 'large Z connection'
        #print connect[i,:]
        lgZ_connect[num_lgZ,0]=connect[i,0]
        lgZ_connect[num_lgZ,1:5]=connect[i,2:6]
        num_lgZ = num_lgZ + 1
        bdry_claimed = 1
    if (connect[i,4] > z_min-del_x) & (connect[i,4] < z_min+del_x) & (connect[i,0] == connect[i,1]):
        smZ_connect[num_smZ,0]=connect[i,0]
        smZ_connect[num_smZ,1:5]=connect[i,2:6]
        num_smZ = num_smZ + 1
        bdry_claimed = 1
    if bdry_claimed == 0:
        print('ERROR! Boundary element has not been assigned to any boundary')
        print(connect[i,:])


fd=open(file_name,'a')
conne = ['CONNECTIONS '+ str(num_real)]       
np.savetxt(fd,conne,fmt='%5s')
np.savetxt(fd,real_connect[0:num_real,:],fmt='%1i %1i %1.15e %1.15e %1.15e %1.15e')
fd.close()

fd=open('bdry_smX.ex','w')
conne = ['CONNECTIONS '+ str(num_smX)]       
np.savetxt(fd,conne,fmt='%5s')
np.savetxt(fd,smX_connect[0:num_smX,:],fmt='%1i %1.15e %1.15e %1.15e %1.15e')
fd.close()


fd=open('bdry_lgX.ex','w')
conne = ['CONNECTIONS '+ str(num_lgX)]       
np.savetxt(fd,conne,fmt='%5s')
np.savetxt(fd,lgX_connect[0:num_lgX,:],fmt='%1i %1.15e %1.15e %1.15e %1.15e')
fd.close()

fd=open('bdry_smY.ex','w')
conne = ['CONNECTIONS '+ str(num_smY)]       
np.savetxt(fd,conne,fmt='%5s')
np.savetxt(fd,smY_connect[0:num_smY,:],fmt='%1i %1.15e %1.15e %1.15e %1.15e')
fd.close()


fd=open('bdry_lgY.ex','w')
conne = ['CONNECTIONS '+ str(num_lgY)]       
np.savetxt(fd,conne,fmt='%5s')
np.savetxt(fd,lgY_connect[0:num_lgY,:],fmt='%1i %1.15e %1.15e %1.15e %1.15e')
fd.close()

fd=open('bdry_smZ.ex','w')
conne = ['CONNECTIONS '+ str(num_smZ)]       
np.savetxt(fd,conne,fmt='%5s')
np.savetxt(fd,smZ_connect[0:num_smZ,:],fmt='%1i %1.15e %1.15e %1.15e %1.15e')
fd.close()


fd=open('bdry_lgZ.ex','w')
conne = ['CONNECTIONS '+ str(num_lgZ)]       
np.savetxt(fd,conne,fmt='%5s')
np.savetxt(fd,lgZ_connect[0:num_lgZ,:],fmt='%1i %1.15e %1.15e %1.15e %1.15e')
fd.close()

