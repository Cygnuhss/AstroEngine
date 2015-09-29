from abc import ABCMeta

import math


"""
Calculations for Newtonian physics.
"""


# The universal gravitational constant.
G = 6.670e-8


def getGravitationalForce(body1, body2):
    """Calculate the gravitational force between two bodies.

    The gravitational force F_g between two bodies with masses M and m a
    distance r apart is
        F_g = - (GMm)/r^2 r/r

    @param body1 The first body, exerting the force.
    @param body2 The second body, undergoing the force.
    @return The gravitational force between the two bodies.
    """
    distanceVector = getDistanceVector(body1, body2)
    distance = distanceVector.length

    mass1 = body1.mass
    mass2 = body2.mass

    gravitational_force = - ((G * mass1 * mass2) / distance**2) * (distanceVector / distance)

    return gravitational_force


def getDistance(body1, body2):
    """Calculate the distance between two bodies.

    Retrieve the length of the distance vector.

    @param body1 The first body.
    @param body2 The second body.
    @return The distance between the two bodies.
    """
    distance = getDistanceVector(body1, body2).length

    return distance

def getDistanceVector(body1, body2):
    """Calculate the distance vector between two bodies.

    @param body1 The first body.
    @param body2 The second body.
    @return The distance vector between the two bodies.
    """
    location1 = body1.location
    location2 = body2.location

    distanceVector = location1 - location2

    return distanceVector
