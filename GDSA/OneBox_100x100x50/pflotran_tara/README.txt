OneBox stretched example from Tara
The 100x100x100 version of this box works fine. PFLOTRAN is not getting to first time step on this 100x100x50 version.
The vorocrust mesh looks good, the model should work.

Problem fixed with suggestions from Satish, Tara will send fixed files when done.

From: "LaForce, Tara" <tlaforc@sandia.gov>
Date: Friday, March 27, 2020 at 10:39 AM

Files include uge file (modified from vorocrust uge) and exe files.

To have a mesh file we can run in pflotran we have to strip out all the region IDs from the cell centers, 
all the normals the faces from each of the connections, and separate all the boundary connections from the 
interior connections.  
We write the boundaries into separate files that pflotran can use, which are the .ex files. 

The python script I attached does this for the 100x100x50 example box.  Much of the script is hard-coded at the moment and you’d have to change the number of cells and boundary locations in the first 15 or so lines to get it to work on a different size mesh.


Ultimately we want a point source for tracer at (x,y)=(0,0) and constant pressure boundaries at x=100 and y=100.  
We also want the mesh to be 100x100x1m instead of 100x100x50m.

We are going to compare convergence with grid refinement to the analytical solution for 1D radial advection/diffusion of a tracer.  This problem is interesting because it is so simple, but the solution on a structured hex mesh converges incredibly slowly with grid refinement because of grid orientation effects.  This is a universal problem for single-point flux approximation schemes.  We are also working on simulations of the same problem on polyhedral meshes.


 
The uge file I use is created from the vorocrust output, but isn't the same.  
The vorocrust files contain much more information, some which we are using, and some that we are not yet. 
 
In the vorocrust output file the cell centers are:
Cell_ID x_center, y_center, z_center, volume, Region_ID
 
We don't do anything with the region ID yet, but we will once we get simulations up and running. 
 
 
The connections are written as:
CELL1 CELL2 x_face, y_face, z_face, area, <normal to the face>
 
Right now we don't use the normals, but we will once we start calculating fluxes in and out of parts of the model.
 
The boundary faces are written as a node connected to itself in the connections section:
CELL1 CELL1  x_face, y_face, z_face, area, <normal to the face>
 
To have a mesh file we can run in pflotran we have to strip out all the region IDs from the cell centers, all the normals the faces from each of the connections, and separate all the boundary connections from the interior connections.  We also write the boundaries into separate files that pflotran can use, which are the .ex files. 

The python script I attached does this for the 100x100x50 example box.  Much of the script is hard-coded at the moment and 
you have to change the number of cells and boundary locations in the first 15 or so lines to get it to work on a different 
size mesh.
 


