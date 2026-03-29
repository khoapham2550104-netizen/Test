import numpy as np

final = np.arange(1,13)
final = final.reshape(3,4)
final = final.T

final = final.reshape(3,4)

begin = np.array(
    [   [1,5,9,2],
        [6,10,3,7],
        [11,4,8,12]]       
)

print(final)