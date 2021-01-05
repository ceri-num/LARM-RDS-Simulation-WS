# LARM Simulation WorkSpace


## Installation:

Create a ROS-Kinetic project on The construct RDS. Then clone this repository in place of `simulation_ws`:

```bash
rm -fr simulation_ws
git clone https://github.com/ceri-num/LARM-RDS-Simulation-WS.git simulation_ws
```

Enter in this new directory `simulation_ws` and build it:

```bash
cd simulation_ws
catkin_make
source devel/setup.bash
```

Finally you can test your install by running a simulation launch file:

```bash
roslaunch turtlebot_gazebo robot_simulation_test.launch
```

Don't forget to open Gazebo.


## Contribute:



## Ressources:

- Initial turtlebot [repo](https://aezquerro@bitbucket.org/theconstructcore/turtlebot.git)
- Initial hokuyo [repo](https://bitbucket.org/theconstructcore/hokuyo_model.git)

With removing of the heavy turtlebot_rtab package
