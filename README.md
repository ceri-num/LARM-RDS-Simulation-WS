# LARM Turtlebot2

Melodic dependencies:

```
sudo apt install ros-melodic-teleop-twist-joy ros-melodic-joy ros-melodic-pid
```

# How to install

```
cd <catkin_ws>/src
git clone https://github.com/ceri-num/LARM-RDS-Simulation-WS.git larm_turtlebot2
cd ..
catkin_make
source devel/setup.bash
```

# How to use


Test your install:

```bash
roslaunch larm test.launch
# open gazebo client

# if xbox controller
roslaunch larm teleop_xbox.launch
```
You should see:

![Turtlebot_car](doc/turtlebot_car.png "turtlebot_car robot in Willow garage map")

And this ros graph:

![rosgraph](doc/rosgraph.png)

## Next...

You can now, clone your own workspace in `catkin_ws` directory and develope your control solution.

