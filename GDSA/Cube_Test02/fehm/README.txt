Example Test 02
See https://meshing.lanl.gov/proj/SFWD_models/index.html

Project Directory:
/project/meshing/GEO_Integration/work/Cube_Test02

Octree refined mesh with pinchout
Background unrefined elements are 1 meter blocks
Refined 3 times to edge length of 12.5

Delaunay mesh is larger than GFM to avoid refinement at top and bottom boundary.
Top extended from 0 to 1, Bottom extended from -10 to -11

node count is   182154                                         
tet  count is  1036237      

ZONES:

Material 1 bottom   has   64141 nodes. #nodes/nnodes is   0.352125138044     
Material 2 pinchout has   79317 nodes. #nodes/nnodes is   0.435439229012     
Material 3 top      has   38696 nodes. #nodes/nnodes is   0.212435632944     

Face top           1 has       441 nodes.                                       
Face bottom        2 has       441 nodes.                                       
Face left_w        3 has      1079 nodes.                                       
Face right_e       5 has      2006 nodes.                                       
Face back_n        6 has      1594 nodes.                                       
Face front_s       4 has      1594 nodes.       

MESH STATS:

-----------------------------------------------------------                     
elements with aspect ratio b/w .2  and .5 :       3737                          
elements with aspect ratio b/w .5  and 1. :    1032500                          
min aspect ratio =  0.4483E+00  max aspect ratio =  0.1000E+01                  
---------------------------------------                                         
element volumes b/w  0.3255E-03 and  0.1134E-02:    744015                      
element volumes b/w  0.1134E-02 and  0.3947E-02:    179124                      
element volumes b/w  0.3947E-02 and  0.1374E-01:     59197                      
element volumes b/w  0.1374E-01 and  0.4786E-01:     34588                      
element volumes b/w  0.4786E-01 and  0.1667E+00:     19313                      
min volume =   3.2552083E-04  max volume =   1.6666667E-01                      
-----------------------------------------------------------                     
1036237 total elements evaluated.                                  

*** Construct and Compress Sparse Matrix:3D ***                                 
   *** Compress Area Coefficient Values ***                                     
 
AMatbld3d_stor: Matrix compress_eps:  0.1000000E-07                             
AMatbld3d_stor: Local epsilon:  0.1000000E-14                                   
SparseMatrix initialize epsilon to 1.000000e-08
SparseMatrix using Epsilon 1.000000e-08
AMatbld3d_stor: *****Zero Negative Coefficients ******                          
AMatbld3d_stor: Number of 'zero' (< compress_eps) coefs         0               
AMatbld3d_stor: npoints =   182154  ncoefs =    1622298                         
AMatbld3d_stor: Number of unique coefs =        99                              
AMatbld3d_stor: Maximum num. connections to a node =         31                 
AMatbld3d_stor: Volume min =   4.8828125E-04                                    
AMatbld3d_stor: Volume max =   1.0000000E+00                                    
AMatbld3d_stor: Total Volume:   4.8000000E+03                                   
AMatbld3d_stor: abs(Aij/xij) min =   0.0000000E+00                              
AMatbld3d_stor: abs(Aij/xij) max =   1.1250000E+00                              
AMatbld3d_stor: (Aij/xij) max =   0.0000000E+00                                 
AMatbld3d_stor: (Aij/xij) min =  -1.1250000E+00                                 
AMatbld3d_stor Matrix coefficient values stored as scalar area/distance         
AMatbld3d_stor Matrix compression used for graph and coefficient values         
ascii STOR file written with name tet.stor                                      
*** SPARSE COEFFICIENT MATRIX _astor SUCCESSFUL ***                             
3D Matrix Coefficient file written with name tet.stor     


ATTRIBUTE        MIN            MAX            DIFFERENCE          LENGTH  
 xic     0.000000000E+00  2.000000000E+01      2.000000000E+01    182154  
 yic     0.000000000E+00  2.000000000E+01      2.000000000E+01    182154  
 zic    -1.100000000E+01  1.000000000E+00      1.200000000E+01    182154  

