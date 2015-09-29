from abc import ABCMeta, abstractmethod, abstractproperty

import math


class Body:
    """An abstract representation of an astronomic body.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, name, location, mass):
        """Initialize a body.

        @param name The name of the body.
        @param location The location of the center of the body as a vector.
        @param mass The mass of the body.
        """
        self.name = name
        self.location = location
        self.mass = mass

    @abstractmethod
    def __repr__(self):
        """Return the representation of the body."""
        return 'Body({0}, {1}, {2})'.format(self.name, self.location, self.mass)


    @abstractproperty
    def volume(self):
        """Return the volume of the body."""
        raise NotImplementedError()

    @abstractproperty
    def surface_area(self):
        """Return the surface area of the body."""
        raise NotImplementedError()

    @abstractproperty
    def density(self):
        """Return the density of the body."""
        return self.mass / self.volume

    @abstractmethod
    def distance_to(self, other):
        """Return the distance between two bodies."""
        return self.location - other.location
