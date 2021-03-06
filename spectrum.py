## Class spectrum: low level class which contains mz and I for a single 
## spectrum


import numpy as np


## Small scale classes which identifies one spectrum
class spectrum:
    def __init__(self, m):
        ''' Define the spectrum class '''
        pippo = np.array(m)
        self.mz = pippo[:,0]
        self.intensity = pippo[:,1] 
        self.x = 0 
        self.y = 0
