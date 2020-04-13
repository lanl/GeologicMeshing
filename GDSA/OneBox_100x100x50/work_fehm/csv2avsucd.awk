# Modified for March 2020 version files

# read x y z csv into AVS UCD format 
# awk -f csv2avsucd.awk file.csv > file.inp
# this can  be read and viewed by paraview
BEGIN {num=0; } 
{ 

# comma deliminated
OFS=","
DEF_MAT = 5

if (NR>1)  {

# read coordinates
  num=num+1
  xp[num] = $1
  yp[num] = $2

  if (NF == 2) { zp[num] = 0. }
  if (NF > 2) {
      zp[num] = $3;
  }

# read subregion + 1 to avoid 0
  if (NF > 12) {
      imat[num] = $13+1;
  }
  else imat[num] = DEF_MAT 
  

}
} END { 
print num " " num " 0 0 0"

# write point coordinates
for (i = 1; i <= num; i = i + 1) { 
   printf("%10d %12.8f %12.8f %12.8f\n", i, xp[i], yp[i], zp[i]) ; } 

# write point elements
for (i = 1; i <= num; i = i + 1) { 
   printf("%10d %10d pt %10d\n", i,imat[i],i ) ; }

# write imt attribute
# print "001 1"
# print "imt, integer"
# for (i = 1; i <= num; i = i + 1) { 
#    printf("%10d %10d\n", i,imat[num]) ; }

}
