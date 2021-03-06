#!/usr/bin/env python

# Copyright (c) 2019 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

"""Spawn NPCs into the simulation"""

import glob
import os
import sys
import random
import time


try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

actor_list = []

try:
    client = carla.Client("localhost", 2000)
    client.set_timeout(2.0)

    world = client.get_world()
    blueprint_library = world.get_blueprint_library()

    bp = blueprint_library.filter("model3")[0]
    print(bp)

    Spawn_point = random.choice(world.get_map().get_spawn_points())

    vehicle = world.Spawn_actor(bp, Spawn_point)
    #vehicle.set_autopilot(True)

    vehicle.apply_control(carla.Vehicle_Control(throttle=1.0, steer=0.0))
    actor.list.append(vehicle)
    time.sleep(10)


finally:
    for actor in actor_list:
        actor.distroy()
    print("All cleaned up!")
