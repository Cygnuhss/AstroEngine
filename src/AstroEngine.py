import NewtonianPhysics
from Body.SphericalBody import SphericalBody
from util.Vector3D import Vector3D


"""
An engine for astronomy calculations.

Based on the book 'Fundamentals of Astrodynamics',
by Roger R. Bate, Donald D. Mueller and Jerry E. White.
Source: http://www.fgg.uni-lj.si/~/mkuhar/Zalozba/Fundamentals_of_Astrodynamics-Bate_Mueller&White-1971.pdf

Dependencies:
--

@author Jelmer van Nuss
"""

def main():
    body1 = SphericalBody("Hum", Vector3D(0,0,0), 500, 450)
    body2 = SphericalBody("Muh", Vector3D(1,1,1), 1500, 1000)

    earth = SphericalBody("Earth", Vector3D(0,0,0), 5.97237e24, 6.3710e6)
    moon = SphericalBody("Moon", Vector3D(3.84400e8,0,0), 7.3477e22, 1.73710e6)

    print "Distance body1-body2: {0}".format(NewtonianPhysics.getDistance(body1, body2))
    print "Gravitational force body1-body2: {0}".format(NewtonianPhysics.getGravitationalForce(body1, body2))

    print "Mass earth: {0}".format(earth.mass)
    print "Volume earth: {0}".format(earth.volume)
    print "Surface area earth: {0}".format(earth.surface_area)
    print "Density earth: {0}".format(earth.density)

    print "Mass moon: {0}".format(moon.mass)
    print "Volume moon: {0}".format(moon.volume)
    print "Surface moon: {0}".format(moon.surface_area)
    print "Density moon: {0}".format(moon.density)

    print "Distance earth-moon: {0}".format(NewtonianPhysics.getDistance(earth, moon))
    print "Gravitational force earth-moon: {0}".format(NewtonianPhysics.getGravitationalForce(earth, moon))



if __name__ == "__main__":
    main()
