#!/bin/env python3
import os, random

# Random pose of 5 cans close to the start position. 

poses= [[2.21479, 1.57095, -0.003171, -0.053354, -0.007227, -0.000762],
[-8.85945, -4.98875, -0.003019, -0.061385, -0.013938, -0.000643],
[-3.0218, -5.57062, 0.03, -0.063891, -1.57, 0.800031],
[-9.73952, 1.58332, -0.002799, -0.064154, 0.000605, -0.00056],
[1.43366, -8.2506, -0.002768, -0.061626, 0.003231, -0.000551],
[6.99396, -7.86856, -0.002738, -0.059766, 0.00452, -0.000532],
[6.72314, 3.65542, -0.002708, -0.057958, 0.00577, -0.000513],
[1.89524, 3.74147, -0.00267, -0.055773, 0.007283, -0.00049],
[-5.60945, 8.72727, -0.002659, -0.055112, 0.007741, -0.000483],
[1.36778, 1.63692, -0.003211, -0.051075, -0.00482, -0.000771]]

random.shuffle(poses)

for i in range( 5 ) :
    cmd= 'rosrun gazebo_ros spawn_model -file `rospack find larm`/models/coke_can/model.sdf -sdf'
    cmd+= ' -x '+ str( poses[i][0] )
    cmd+= ' -y '+ str( poses[i][1] )
    cmd+= ' -z '+ str( poses[i][2] )
    cmd+= ' -R '+ str( poses[i][3] )
    cmd+= ' -P '+ str( poses[i][4] )
    cmd+= ' -Y '+ str( poses[i][5] )
    cmd+= ' -model coke_can_'+ str(i)   
    os.system(cmd)
