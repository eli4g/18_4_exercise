"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        self.start=start
        self.original_start = start
        self.count = 0
        
    def generate(self):
        if self.count == 0:
            self.count += 1
            return self.start
        else: 
            self.start += 1
            return self.start
    
    def reset(self):
        self.start = self.original_start
        self.count = 0
        
