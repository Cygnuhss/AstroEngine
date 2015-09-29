# -*- coding: utf-8 -*-

from Body import *


class SphericalBody(Body):
    """A spherical body.
    """

    def __init__(self, name, location, mass, radius):
        """Initialize a body.

        @param name The name of the body.
        @param location The location of the center of the body as a vector.
        @param mass The mass of the body.
        @param radius The radius of the body.
        """
        Body.__init__(self, name, location, mass)
        self.radius = radius

    def __repr__(self):
        return 'SphericalBody({0}, {1}, {2}, {3})'.format(self.name, self.location,
                                                          self.mass, self.radius)


    @property
    def volume(self):
        """Calculate the volume of the spherical body.

        The volume of a sphere is
            V = (4/3)πr^3.

        @return The volume of the spherical body.
        """
        return (4/3.0) * math.pi * self.radius**3

    @property
    def surface_area(self):
        """Calculate the surface area of the spherical body.

        The surface area of a sphere is
            A = 4πr^2.

        @return The surface area of the spherical body.
        """
        return 4 * math.pi * self.radius**2
        
    @property
    def density(self):
        return super(SphericalBody, self).density

    def distance_to(self, other):
        return super(SphericalBody, self).distance_to(other)
