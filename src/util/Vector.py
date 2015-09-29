from abc import ABCMeta, abstractmethod, abstractproperty

import math


class Vector():
    """An abstract representation of a vector.
    D-dimensional vectors will have to be implemented.

    Vectors can be added and subtracted together, and multiplied and divided
    by a scalar.
    Vectors have a length and can be normalized.
    A dot product and the distance between vectors can be calculated.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        """Initialize a vector."""
        raise NotImplementedError()

    @abstractmethod
    def __repr__(self):
        """Return the representation of the vector."""
        raise NotImplementedError()


    @abstractmethod
    def __add__(self, other):
        """Add two vectors."""
        raise NotImplementedError()

    @abstractmethod
    def __sub__(self, other):
        """Subtract two vectors."""
        raise NotImplementedError()

    @abstractmethod
    def __mul__(self, scalar):
        """Multiply the vector with a scalar."""
        raise NotImplementedError()

    @abstractmethod
    def __rmul__(self, scalar):
        """Multiply the vector with a scalar."""
        return self.__mul__(scalar)

    @abstractmethod
    def __div__(self, scalar):
        """Divide the vector by a scalar."""
        raise NotImplementedError()


    @abstractproperty
    def length(self):
        """Return the length of the vector."""
        raise NotImplementedError()

    @abstractmethod
    def normalize(self):
        """Normalize the vector."""
        raise NotImplementedError()

    @abstractmethod
    def dot_product(self, other):
        """Calculate the dot product between two vectors."""
        raise NotImplementedError()

    @abstractmethod
    def distance_to(self, other):
        """Calculate the Euclidean distance between two vectors."""
        raise NotImplementedError()
