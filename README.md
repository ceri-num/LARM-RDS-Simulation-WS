# LARM Simulation WorkSpace

## Installation

Create a ROS-Melodic ROSjet on The construct RDS. Steps:

```bash
rm -fr simulation_ws
git clone https://github.com/ceri-num/LARM-RDS-Simulation-WS.git simulation_ws
cd simulation_ws
catkin_make
source devel/setup.bash
```

Test your install:

```bash
roslaunch larm project.launch
# open gazebo client 
```

## Ressources

- Initial turtlebot [repo](https://aezquerro@bitbucket.org/theconstructcore/turtlebot.git)
    Removed the heavy `turtlebot_rtab` package

- Initial hokuyo [repo](https://bitbucket.org/theconstructcore/hokuyo_model.git)

