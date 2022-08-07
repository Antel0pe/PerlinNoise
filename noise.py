import functools
import random

class PerlinNoise():
    
    def __init__(self,
                 seed: float = 1,
                 amplitude: float = 1,
                 frequency: float = 1,
                 scale: float = 1,
                 octaves: float = 1,
                 persistence: float = 0.5,
                 lancunarity: float = 1
                 ):
        self.seed = seed # used
        self.amplitude = amplitude # used
        self.frequency = frequency
        self.scale = scale 
        self.octaves = octaves 
        self.persistence = persistence 
        self.lancunarity = lancunarity
        
        random.seed(self.seed)
    
    # Extend for higher dimensions
    def getNoiseAt(self, x: float) -> float:
        if x % self.frequency == 0:
            return 0
        
        lowerBound: int = int(x // self.frequency) * self.frequency
        upperBound: int = lowerBound + self.frequency
        
        distanceToLowerBound: float = x - lowerBound
        
        smoothersteppedDiff: float = self.smootherstep(distanceToLowerBound)
        
        persistenceInc = 1
        yVal = 0
    
        for octave in range(self.octaves):
            lowerBoundSlope: float = self.getSlopeAt(lowerBound, octave, self.amplitude * persistenceInc)
            upperBoundSlope: float = self.getSlopeAt(upperBound, octave, self.amplitude * persistenceInc)
        
        
            result: float = self.getInterpolated(self.getY(lowerBoundSlope, lowerBound, x),
                                            self.getY(upperBoundSlope, upperBound, x), smoothersteppedDiff
                                            )

            yVal += result 
            persistenceInc *= self.persistence
            
            
        
        return yVal
        
    # seed makes it so sequence of random num is always same
    # not that same x val returns same random num
    # no matter what x vals are, sequence of nums will always be same
    @functools.cache
    def getSlopeAt(self, x: int, octave: int, amplitude: float) -> float:
        return random.uniform(-1 * amplitude, amplitude)
        
    
    def smootherstep(self, x: int) -> float:
        return -1 * (-2*x**3 + 3*x**2) + 1
    
    def getInterpolated(self, y1: float, y2: float, adjustment: float) -> float:
        return y1 * adjustment + y2 * (self.frequency - adjustment)
    
    def getY(self, slope: float, x0: float, x1: float) -> float:
        return slope * (x1 - x0)
    
    
