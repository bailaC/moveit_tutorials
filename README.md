# MoveIt! Tutorials

This repository is automatically built by the ROS build farm and its output is hosted here: http://docs.ros.org/kinetic/api/moveit_tutorials/html/

The tutorials use the [reStructuredText](http://www.sphinx-doc.org/en/stable/rest.html) format commonly used in the Sphinx "Python Documentation Generator". This unfortunately differs from the common Markdown format.

## Travis Continuous Integration

[![Build Status](https://travis-ci.org/ros-planning/moveit_tutorials.svg?branch=master)](https://travis-ci.org/ros-planning/moveit_tutorials)

## ROS Buildfarm

[![Build Status](http://build.ros.org/buildStatus/icon?job=Kdoc__moveit_tutorials__ubuntu_xenial_amd64)](http://build.ros.org/job/Kdoc__moveit_tutorials__ubuntu_xenial_amd64/)

## Coveralls Test Coverage
[![Coverage Status](https://coveralls.io/repos/github/bailaC/moveit_tutorials/badge.svg?branch=kinetic-devel)](https://coveralls.io/github/bailaC/moveit_tutorials?branch=kinetic-devel)

## Versions

The ``indigo-devel`` branch should be considered for the most part "frozen" for historical reasons, and new changes to tutorials should be in the ``kinetic-devel`` branch.

## dummy Build : 01_01_10_18

If you want to test the tutorials by generating the html pages locally on your machine, install [rosdoc_lite](http://wiki.ros.org/rosdoc_lite):

    sudo apt-get install ros-kinetic-rosdoc-lite

and run in the root of the package:

    rosdoc_lite -o build .

Then open ``LOCAL_PACKAGE_PATH/build/html/index.html`` in your web browser.

## Deployment

For deploying documentation changes to the web, [Section 3 of rosdoc_lite wiki](http://wiki.ros.org/rosdoc_lite) says that "rosdoc_lite is automatically run for packages in repositories that have rosinstall files listed in the rosdistro repository." This is done about once every 24 hours, [overnight](http://wiki.ros.org/rosdistro/Tutorials/Indexing%20Your%20ROS%20Repository%20for%20Documentation%20Generation).

## Contributing

These tutorials use the same [style guidelines](http://moveit.ros.org/documentation/contributing/code/) as the MoveIt! project. When modifying or adding to these tutorials, it is required that code is auto formatted using [clang-format](http://moveit.ros.org/documentation/contributing/code/).
