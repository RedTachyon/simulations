import numpy as np

G = .01
M = 500.
m = .1
dt = .0001

def force(r):
    """
    Computes the force at a given position.
    
    Args:
        r: array of shape (2,), position
        
    Returns:
        array of shape (2,), force at a given position
    """
    return ((-G*M*m) / np.power(np.dot(r, r), 3/2.)) * r

def potential(r):
    """
    Computes the potential energy at a given position.
    
    Args:
        r: array of shape (2, -1), position
        
    Returns:
        array of shape (-1,), potential at a given position
    """
    return (-G*M*m) / np.linalg.norm(r, axis=1)

def kinetic(p):
    """
    Computes the potential energy at a given position.
    
    Args:
        p: array of shape (2, -1), momentum
        
    Returns:
        array of shape (-1,), kinetic energy
    """
    return np.square(np.linalg.norm(momentums, axis=1)) / (2*m)

def energy(p, r):
    return potential(r) + kinetic(p)


class Particle:
    """
    Holds information about the simulated body.
    
    Args:
        r0: array, initial position
        p0: array, initial momentum
    """
    
    def __init__(self, r0, p0, F=None):
        self.r0 = r0
        self.position = np.copy(r0)
        
        self.t = 0.

        # For Euler
        self.p0 = p0
        self.momentum = np.copy(p0)       
        
        # For Verlet
        self.pos_prev = self.r0 - (self.p0 / m) * dt
        
        # For Leapfrog
        if F is None:
            F = force(self.r0)
            
        self.v = (self.p0/m) - (0.5 * F * dt) / m
            
        
    def evolve_euler(self, F=None):
        """
        Performs a position and momentum update according to the Euler's algorithm.
        """
        self.t += dt
        if F is None:
            F = force(self.position)
        
        self.position += (self.momentum / m) * dt + (.5 * (F / m)) * dt**2
        self.momentum += F * dt
    
    def evolve_verlet(self, F=None):
        """
        Performs a position update according to the Verlet's algorithm.
        """
        self.t += dt
        if F is None:
            F = force(self.position)
        
        r_new = 2*self.position - self.pos_prev + ((F/m) * dt**2)
        
        self.momentum = (m*(r_new - self.pos_prev)) / (2*dt)
        
        self.pos_prev = np.copy(self.position)
        self.position = np.copy(r_new)

        
    def evolve_frog(self, F=None):
        """Preforms a position update according to the leapfrog algorithm."""
        self.t += dt
        if F is None:
            F = force(self.position)
        
        v_new = self.v + (F/m) * dt
        self.momentum = (m*(self.v + v_new)) / 2.
        self.v = v_new
        self.position += self.v * dt
    
    
    def __str__(self):
        return "Particle(" + str(self.position) + ", " + str(self.momentum) + ")"
    
    def __repr__(self):
        return "Particle(" + str(self.position) + ", " + str(self.momentum) + ")"