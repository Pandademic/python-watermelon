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

plt.imshow(data,cmap="nipy_spectral") 
print("saving to melon.png!")
plt.axis('off')
plt.savefig('melon.png')
print("showing!")
plt.show()
