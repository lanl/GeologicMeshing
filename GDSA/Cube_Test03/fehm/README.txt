Example Test 03
See https://meshing.lanl.gov/proj/SFWD_models/index.html

Project Directory:
/project/meshing/GEO_Integration/work/Cube_Test03

Octree refined mesh with embedded body
Background unrefined elements are 1 meter blocks
Refined 3 times to edge length of 12.5


node count is   72329                                         
tet  count is  420897      

ZONES:

Material 3 is embedded body within a single material (combine 1 and 2)

Material 1 above body has   27223 nodes. #nodes/nnodes is   0.376377373934     
Material 2 below body has   28338 nodes. #nodes/nnodes is   0.391793042421     
Material 3 body       has   16768 nodes. #nodes/nnodes is   0.231829553843    

Face top           1 has       441 nodes.                                       
Face bottom        2 has       441 nodes.                                       
Face left_w        3 has       231 nodes.                                       
Face right_e       5 has       231 nodes.                                       
Face back_n        6 has       231 nodes.                                       
Face front_s       4 has       231 nodes.           


MESH STATS:

---------------------------------------                                         
elements with aspect ratio b/w .2  and .5 :       1495                          
elements with aspect ratio b/w .5  and 1. :     419402                          
min aspect ratio =  0.3440E+00  max aspect ratio =  0.1000E+01                  
---------------------------------------                                         
element volumes b/w  0.3255E-03 and  0.1302E-02:    326557                      
element volumes b/w  0.1302E-02 and  0.5208E-02:     43440                      
element volumes b/w  0.5208E-02 and  0.2083E-01:     13934                      
element volumes b/w  0.2083E-01 and  0.8333E-01:     16411                      
element volumes b/w  0.8333E-01 and  0.3333E+00:     20555                      
min volume =   3.2552083E-04  max volume =   3.3333333E-01                      
-----------------------------------------------------------                     
    420897 total elements evaluated.                                      

*** Construct and Compress Sparse Matrix:3D ***                                 
   *** Compress Area Coefficient Values ***                                     
AMatbld3d_stor: Matrix compress_eps:  0.1000000E-07                             
AMatbld3d_stor: Local epsilon:  0.1000000E-14                                   
SparseMatrix initialize epsilon to 1.000000e-08
SparseMatrix using Epsilon 1.000000e-08
AMatbld3d_stor: *****Zero Negative Coefficients ******                          
AMatbld3d_stor: Number of 'zero' (< compress_eps) coefs         0               
AMatbld3d_stor: npoints =    72329  ncoefs =     568865                         
AMatbld3d_stor: Number of unique coefs =       115                              
AMatbld3d_stor: Maximum num. connections to a node =         28                 
AMatbld3d_stor: Volume min =   1.9531250E-03                                    
AMatbld3d_stor: Volume max =   1.0000000E+00                                    
AMatbld3d_stor: Total Volume:   4.0000000E+03                                   
AMatbld3d_stor: abs(Aij/xij) min =   0.0000000E+00                              
AMatbld3d_stor: abs(Aij/xij) max =   1.1250000E+00                              
AMatbld3d_stor: (Aij/xij) max =   0.0000000E+00                                 
AMatbld3d_stor: (Aij/xij) min =  -1.1250000E+00                                 
AMatbld3d_stor Matrix coefficient values stored as scalar area/distance         
AMatbld3d_stor Matrix compression used for graph and coefficient values         
ascii STOR file written with name tet.stor                                      
 
*** SPARSE COEFFICIENT MATRIX _astor SUCCESSFUL ***                             
 
3D Matrix Coefficient file written with name tet.stor           

ATTRIBUTE        MIN               MAX         DIFFERENCE    LENGTH  
 xic     0.000000000E+00  2.000000000E+01 2.000000000E+01     72329  
 yic     0.000000000E+00  2.000000000E+01 2.000000000E+01     72329  
 zic    -1.000000000E+01  0.000000000E+00 1.000000000E+01     72329  
