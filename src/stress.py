class Stress:
    import pandas as pd
    from src.files import File
    
    def __init__(self, file: File, cut_off: bool = True, fit_window: int = 500):
        
        self.file = file
        if cut_off:
            self.data = Stress.cutMaxStress(self.file.data)
        else:
            self.data = self.file.data
    
        self.fit_window = fit_window
        self.fit_results = self.getBestFit()
        
        
    @staticmethod
    def cutMaxStress(df) -> pd.DataFrame:
        max_stress_row = df[df['stress'] == df['stress'].max()]
        max_strain_index = max_stress_row.index[0]
        cut_df = df.iloc[:max_strain_index + 1]
        return cut_df
    
    def getBestFit(self):
        import pandas as pd
        from sklearn.linear_model import LinearRegression
        
        step = 10
        left = 0
        right = self.fit_window
    
        fit_results = pd.DataFrame()
        model = LinearRegression()
        sizeData = len(self.data)

        while True:
            if right > sizeData: 
                break

            data = self.data[left:right]

            model.fit(data[['strain']], data[['stress']])
            slope = model.coef_[0]
            intercept = model.intercept_
            y_exp = slope * data['strain'] + intercept
            error = (data['stress'] - y_exp)**2

            fit_results = pd.concat([fit_results, pd.DataFrame({'strain': data.iloc[100].strain, 'slope': slope, 'intercept': intercept, 'error': error.sum()})],axis=0)

            left += step
            right += step
            
        bestFit = fit_results[fit_results['error'] == fit_results['error'].min()].iloc[0]
        return bestFit
    
    def plotBestFit(self):
        import matplotlib.pyplot as plt
        max_stress = self.data[-1:]['stress'].values[0]
        max_strain = (max_stress - self.fit_results.intercept) / self.fit_results.slope
        strain_range = self.data[self.data['strain'] < max_strain]['strain']

        line = self.fit_results.slope * strain_range + self.fit_results.intercept
        other = self.fit_results.slope * (strain_range) + self.fit_results.intercept

        plt.plot(strain_range, line, linestyle='--')
        plt.plot(strain_range + 0.02, other, linestyle='dotted')
    
    
    def plot(self):
        import matplotlib.pyplot as plt
        plt.plot(self.data['strain'], self.data['stress'])
        plt.xlabel('Strain')
        plt.ylabel('Stress [Pa]')
        plt.title(self.file.filename)
        
        self.plotBestFit()
        
        plt.show()