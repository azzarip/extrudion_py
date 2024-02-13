class StressStrain:
    def __init__(self, raw, sample_area, initial_length):
        self.raw = raw
        
        strain = self.getStrain(sample_area)
        stress = self.getStress(initial_length)
        
        import pandas as pd
        self.data = pd.DataFrame({'strain': strain, 'stress': stress})

    
    def getStress(self, sample_area):
        return self.raw['N'] / (sample_area) * 1_000_000 / 1000
    
    def getStrain(self, initial_length):
        from numpy import log
        length = self.raw['mm'] + initial_length
        return log(length / initial_length)
    

