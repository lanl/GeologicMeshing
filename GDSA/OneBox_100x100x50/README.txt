OneBox stretched example from Tara
The 100x100x100 version of this box works fine. PFLOTRAN is not getting to first time step on this 100x100x50 version.
The vorocrust mesh looks good, the model should work.

Files:

VC (vorocrust input and output files):
-rw-r--r--@ 1 tamiller  staff  1221810 Mar 19 11:08 Vmesh_001.ply
-rw-r--r--@ 1 tamiller  staff   343933 Mar 19 11:08 Voronoi_Seeds.csv
-rw-r--r--@ 1 tamiller  staff      302 Mar 19 11:08 corner_spheres.csv
-rw-r--r--@ 1 tamiller  staff     2566 Mar 19 11:08 edges_spheres.csv
-rw-r--r--@ 1 tamiller  staff  1341143 Mar 19 11:08 mesh.uge
-rw-r--r--@ 1 tamiller  staff   926917 Mar 19 11:09 out_mesh.uge
-rw-r--r--@ 1 tamiller  staff    30870 Mar 19 11:08 surface_mesh.obj
-rw-r--r--@ 1 tamiller  staff    43728 Mar 19 11:08 surface_spheres.csv
-rw-r--r--@ 1 tamiller  staff      127 Mar 19 11:08 vc.in

pflotran_tara (pflotran simulaiton files):
-rw-r--r--@ 1 tamiller  staff   14559 Mar 30 08:13 bdry_lgX.ex
-rw-r--r--@ 1 tamiller  staff   16801 Mar 30 08:13 bdry_lgY.ex
-rw-r--r--@ 1 tamiller  staff   15036 Mar 30 08:13 bdry_smX.ex
-rw-r--r--@ 1 tamiller  staff  926928 Mar 30 09:59 out_mesh_edited.uge

-rw-r--r--@ 1 tamiller  staff    4595 Mar 30 08:13 2D_voro_z50.in
-rw-r--r--@ 1 tamiller  staff     206 Mar 19 11:07 OneBox_stretched_100x100x50.obj
-rw-r--r--  1 tamiller  staff    5490 Mar 30 11:19 README.txt
-rw-r--r--@ 1 tamiller  staff    4919 Mar 30 09:59 load_voro_mesh_100x100x50.py
-rw-r--r--@ 1 tamiller  staff     127 Mar 19 11:08 vc.in

From Tara:

To have a mesh file we can run in pflotran we have to strip out all the region IDs from the cell centers, 
all the normals the faces from each of the connections, and separate all the boundary connections from the 
interior connections.  
We write the boundaries into separate files that pflotran can use, which are the .ex files. 

The python script I attached does this for the 100x100x50 example box.  Much of the script is hard-coded at the moment and you have to change the number of cells and boundary locations in the first 15 or so lines to get it to work on a different size mesh.

Ultimately we want a point source for tracer at (x,y)=(0,0) and constant pressure boundaries at x=100 and y=100.  
We also want the mesh to be 100x100x1m instead of 100x100x50m.

We are going to compare convergence with grid refinement to the analytical solution for 1D radial advection/diffusion of a tracer.  This problem is interesting because it is so simple, but the solution on a structured hex mesh converges incredibly slowly with grid refinement because of grid orientation effects.  This is a universal problem for single-point flux approximation schemes.  
We are also working on simulations of the same problem on polyhedral meshes.



