#!/bin/env python3
import os, random

poses= [[2.21479, 1.57095, -0.003171, -0.053354, -0.007227, -0.000762],
[-3.0218, -5.57062, 0.03, -0.063891, -1.57, 0.800031],
[1.43366, -8.2506, -0.002768, -0.061626, 0.003231, -0.000551],
[6.72314, 3.65542, -0.002708, -0.057958, 0.00577, -0.000513],
[-5.60945, 8.72727, -0.002659, -0.055112, 0.007741, -0.000483],
[1.36778, 1.63692, -0.003211, -0.051075, -0.00482, -0.000771]]

for i in range( number ) :
    cmd= 'rosrun gazebo_ros spawn_model -file `rospack find larm`/models/coke_can/model.sdf -sdf'
    cmd+= ' -x '+ str( poses[i][0] )
    cmd+= ' -y '+ str( poses[i][1] )
    cmd+= ' -z '+ str( poses[i][2] )
    cmd+= ' -R '+ str( poses[i][3] )
    cmd+= ' -P '+ str( poses[i][4] )
    cmd+= ' -Y '+ str( poses[i][5] )
    cmd+= ' -model coke_can_'+ str(i)   
    os.system(cmd)
