Example Test 04
See https://meshing.lanl.gov/proj/SFWD_models/index.html

Project Directory:
/project/meshing/GEO_Integration/work/Cube_Test04

Octree refined mesh with faulted layers 
Background unrefined elements are 1 meter blocks
Refined 3 times to edge length of 12.5

node count is  253688                                         
tet  count is 1459249      

ZONES:

Materials are offset on either side of fault plane into 5 pieces.
Top layer is material 1 and 2
Middle layer is material 2 and 3
Bottom layer is material 5

Material 1 Layer 1a  has     63219 nodes. #nodes/nnodes is   0.249199807644     
Material 2 Layer 1b  has     29352 nodes. #nodes/nnodes is   0.115701176226     
Material 3 Layer 2a  has     78157 nodes. #nodes/nnodes is   0.308083146811     
Material 4 Layer 2b  has     69252 nodes. #nodes/nnodes is   0.272980988026     
Material 5 Layer 3   has     13708 nodes. #nodes/nnodes is   0.540348775685E-01 

Face top           1 has      1488 nodes.                                       
Face bottom        2 has      1609 nodes.                                       
Face left_w        3 has      2068 nodes.                                       
Face right_e       5 has      2068 nodes.                                       
Face back_n        6 has      1259 nodes.                                       
Face front_s       4 has      1885 nodes.                


MESH STATS:

---------------------------------------                                         
elements with aspect ratio b/w .2  and .5 :      13377                          
elements with aspect ratio b/w .5  and 1. :    1445872                          
min aspect ratio =  0.2100E+00  max aspect ratio =  0.9854E+00                  
---------------------------------------                                         
element volumes b/w  0.2713E-03 and  0.1085E-02:   1127408                      
element volumes b/w  0.1085E-02 and  0.4340E-02:    203302                      
element volumes b/w  0.4340E-02 and  0.1736E-01:     71829                      
element volumes b/w  0.1736E-01 and  0.6944E-01:     41074                      
element volumes b/w  0.6944E-01 and  0.2778E+00:     15636                      
min volume =   2.7126736E-04  max volume =   2.7777778E-01                      
-----------------------------------------------------------                     
   1459249 total elements evaluated.                                           

*** Construct and Compress Sparse Matrix:3D ***                                 
   *** Compress Area Coefficient Values ***                                     
AMatbld3d_stor: Matrix compress_eps:  0.1000000E-07                             
AMatbld3d_stor: Local epsilon:  0.1000000E-14                                   
SparseMatrix initialize epsilon to 1.000000e-08
SparseMatrix using Epsilon 1.000000e-08
AMatbld3d_stor: *****Zero Negative Coefficients ******                          
AMatbld3d_stor: Number of 'zero' (< compress_eps) coefs         0               
AMatbld3d_stor: npoints =   253688  ncoefs =    2221094                         
AMatbld3d_stor: Number of unique coefs =       189                              
AMatbld3d_stor: Maximum num. connections to a node =         28                 
AMatbld3d_stor: Volume min =   4.0690104E-04                                    
AMatbld3d_stor: Volume max =   8.3333333E-01                                    
AMatbld3d_stor: Total Volume:   4.0000000E+03                                   
AMatbld3d_stor: abs(Aij/xij) min =   0.0000000E+00                              
AMatbld3d_stor: abs(Aij/xij) max =   1.2000000E+00                              
AMatbld3d_stor: (Aij/xij) max =   0.0000000E+00                                 
AMatbld3d_stor: (Aij/xij) min =  -1.2000000E+00                                 
AMatbld3d_stor Matrix coefficient values stored as scalar area/distance         
AMatbld3d_stor Matrix compression used for graph and coefficient values         
ascii STOR file written with name tet.stor                                      
*** SPARSE COEFFICIENT MATRIX _astor SUCCESSFUL ***                             
3D Matrix Coefficient file written with name tet.stor                   


ATTRIBUTE        MIN               MAX         DIFFERENCE    LENGTH  
 xic     0.000000000E+00  2.000000000E+01 2.000000000E+01    253688  
 yic     0.000000000E+00  2.000000000E+01 2.000000000E+01    253688  
 zic    -1.000000000E+01  0.000000000E+00 1.000000000E+01    253688  
