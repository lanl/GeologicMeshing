
Original work done in:
/project/meshing/GEO_Integration/work/Cube_Test02

Link to the GFM mesh from JewelSuite
  ln -s ../GFM_JS/tet_materials.inp tet_gfm.inp

Use LaGriT to stack surfaces from the GFM
First create a 2D Delaunay triangulation 
Interpolate elevations from each surface
Add intermediate layers and stack into a prism mesh
Connect Delaunay

lagrit < get_external_surfs.lgi 
cp lagrit.out lagrit_surfs.out.txt

lagrit < top_refine.lgi
cp lagrit.out lagrit_refine.out.txt

lagrit < stack_to_fehm.lgi
cp lagrit.out lagrit_stack.out.txt



