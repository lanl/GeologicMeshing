SFWD-GDSA GEO Integration Project
June 2019

PROJECT:

The Spent Fuel and Waste Science and Technology (SFWST) Campaign of the U.S. Department of Energy (DOE) Office of Nuclear Energy (NE) is tasked with conducting research and development (R&D) related to the geological disposal of spent nuclear fuel (SNF) and high level nuclear waste (HLW). 
Two high priority topics for SFWST R&D are to create design concepts and numerical modeling approaches for disposal systems. 
A major piece of the R&D work will be a Geologic Disposal Safety Analysis (GDSA) reference case for each of the studied rock types (salt, crystalline, argillite) (Mariner et al., 2018). 

PROCESS:

The workflow we use for modeling geologic applications is as follows:

- Collect and process data for the model area.
- Create a Geologic Framework Model (GFM) to represent the model area.
- Create an appropriate computational mesh based on the GFM and data.
- Write model mesh and setup files for the modeling application.
- Run simulations and adjust previous work as necessary.

PROJECT FILES:

Each Test directory represents an example workflow:
- Cube_Test01 is a simple 4 layer model
- Cube_Test02 is 3 layers with a pinchout
- Cube_Test03 is an embedded body or lens feature
- Cube_Test04 is a fault plane used to offset layers

Each Test directory has the following:
- GFM_JS has the JewelSuite GOCAD file and the converted AVS file (correct coordinate system)
- lagrit is the work directory to create surfaces and a Delaunay tet mesh based on the GFM
- fehm are the mesh and setup files for FEHM
- pflotran are the fehm mesh and setup converted to pflotran files 
- VC is a directory for VoroCrust work
- images includes png files and gallery.html for the Test version


