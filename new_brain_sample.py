## code to create new brain_sample.csv

import numpy as np
import random


# all row of zeros and one row of ones
data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_test1.csv", data_input, fmt='%d', delimiter=',')

# all zeros
data_input = np.zeros((20, 20))
np.savetxt("brain_test2.csv", data_input, fmt='%d', delimiter=',')

# all column of zeros and one of ones
data_input = np.zeros((20, 20))
data_input[: , -1] = 1
np.savetxt("brain_test3.csv", data_input, fmt='%d', delimiter=',')



# random numbers
data_input = random.randint(0, 20)
data_input = np.random.rand(0, 20)
(20,20)

((20, 20))
np.random



#####
data_output = np.loadtxt(file_input='brain_test_output2.csv')
np.testing.assert_array_equal(data_input, data_output)


####
# running bisect
# manually, this one works 
# dcaf17b7197034d6736ef1f83972b37ca9b62833
#    16 aug 2019
# 8fc86a4cb71e7c8bd6a3870a71c9c4b339451b44
# with numpy I can calculate
#    21 sept 2019 1308

# this is not working
# baef87988e0e44ac753987206ae80b65fa3a906e
#    29 sept 2019 0535
# uses numbpr to calculate
