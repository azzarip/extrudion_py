class TERFolder:
    class FolderNotFound(Exception):
        pass
    
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        
        self.file_list =self.getTERFilesInFolder()
        
        import pandas as pd
        self.results = pd.DataFrame()
        
        import os
        if not os.path.exists(folder_path + '/plots'):
            os.makedirs(folder_path + '/plots') 
    
    def analyze(self, options = []):
        import pandas as pd
        
        for file in self.file_list:
            result = TERFile(self.folder_path + '/' + file).analyze(options)
            self.results = pd.concat([self.results, result])
    
    
    def getTERFilesInFolder(self):
        import os
            
        try:
            dir_list = os.listdir(self.folder_path)
            
            try:
                file_list = [filename for filename in dir_list if filename.endswith('.TRA')]

                if not file_list:
                    print('No .TRA files found in the folder.')
                    return []
                else:
                    return file_list
            
            except FileNotFoundError:
                print('An error occurred while filtering files.')
                raise
            
        except FileNotFoundError:
            raise TERFolder.FolderNotFound('Folder not found') 
        
    

class TERFile:
    def __init__(self, filepath: str):
        import pandas as pd
        self.data = pd.read_table(filepath, header = [3], encoding = 'ANSI', sep = ',')
    
    def analyze(self, options = []):
        pass
    
        
# class Old:
 
                
#     def openFile(self) -> pd.DataFrame:
#         import os 
#         file = os.path.join(self.folder, self.filename)
        
#         import pandas as pd
#         return pd.read_table(file, header = [3], encoding = 'ANSI', sep = ',')
        
#     def calculate(self) -> pd.DataFrame:
#         import pandas as pd
#         data = self.openFile()
        
#         strain = self.getStrain(data)
#         stress = self.getStress(data)
        
#         return pd.DataFrame({'strain': strain, 'stress': stress})
        
#     def getStress(self, data) -> pd.Series:
#         # Divide force by surface in mm to get Pascals, divide by 1000 to get KPascals
#         return data['N'] / (self.sample_area) * 1_000_000 / 1000

    
#     def getStrain(self, data) -> pd.Series:
#         import numpy as np
#         return np.log(data['mm.1'] / data['mm.1'][0])