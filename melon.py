# -*- coding: utf-8-*-

import matplotlib.pyplot as plt

data = [[3,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,9,9,10,10,10,10],
        [10,10,10,9,9,0,9,10,10,10],
        [10,10,9,9,9,9,9,9,10,10],
        [10,9,9,0,9,9,9,9,9,10],
        [10,6,6,6,6,6,6,6,6,10]]
"""
data = [[1,2,3,4,5,6,7,8,9,10]]
"""
    
plt.imshow(data,cmap="nipy_spectral") 
print("saving to melon.png!")
plt.axis('off')
plt.savefig('melon.png')
print("showing!")
plt.show()
