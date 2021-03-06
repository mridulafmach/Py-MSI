from PIL import Image
import numpy as np
from numpy import inf

################################ Function load image
'''Open image in python'''

im = Image.open('wood.png').convert('L')
im = np.array(im)

################################# Image slicer
'''Slice big picture into nu. of small blocks'''

import image_slicer
image_slicer.slice('huge_test_image.png', 14)

############################### Histogram plot
'''Image histogram plot'''

figure()
hist(im.flatten(),128)
show()

###################################  Entropy
'''Function to calculate entropy from GCLM'''


def entropy(g):
    con1 = -g
    lcon = np.log(g)
    lcon[lcon == -inf] = 0
    mat = np.multiply(con1,lcon)
    mat[mat == -0] = 0
    result = np.sum(mat)
    return(result)


#### ASM

np.sum(np.multiply(con,con))

#########

d = np.arange(3,42,3)
a = [0, np.pi/4, np.pi/2, 3*np.pi/4]

contrast = np.zeros(shape=(d.size,len(a)))
energy = np.zeros(shape=(d.size,len(a)))
homo = np.zeros(shape=(d.size,len(a)))
entropy1 = np.zeros(shape=(d.size,len(a)))

for i in range(d.size):
  for j in range(len(a)):
  g = greycomatrix(im,[d[i]],[a[j]],normed = True,symmetric =True)  
  contrast[i,j] = greycoprops(g,'contrast') 
  homo[i,j]     = greycoprops(g,'homogeneity')
  energy[i,j]   = greycoprops(g,'energy')
  entropy1[i,j] = entropy(g)


np.savetxt("contrast.csv",contrast,delimiter=",")
np.savetxt("homo.csv",homo,delimiter=",")
np.savetxt("entropy.csv",entropy1,delimiter=",")
np.savetxt("energy.csv",energy,delimiter=",")


##### R heat map

x = seq(3,60,len=20)
a = seq(0,135,len=4)
filled.contour(x,a,contrast,color.palette = heat.colors)
filled.contour(x,a,homo1,color.palette = colorRampPalette(c("red", "white", "blue")))
