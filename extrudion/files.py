class TERFolder:
    class FolderNotFound(Exception):
        pass
    
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        
        self.file_list =self.getTERFiles()
        
        import pandas as pd
        self.results = pd.DataFrame()
        
        import os
        if not os.path.exists(folder_path + '/plots'):
            os.makedirs(folder_path + '/plots') 
    
    def analyze(self, options = {}):
        import pandas as pd
        
        for file in self.file_list:
            result = TERFile(self.folder_path + '/' + file).analyze(options)
            self.results = pd.concat([self.results, result])
    
    
    def getTERFiles(self):
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
        df = pd.read_table(filepath, header = [3], encoding = 'ANSI', sep = ',')
        df['mm'] = df['mm'].apply(replace_negative_values)
        self.data = df
         
    def analyze(self, options):
        from .analyzers import StressStrain
        
        ss = StressStrain(self.data, sample_area=options['sample_area'], initial_length=options['initial_length'])
        print(ss.result)

def replace_negative_values(x):
    if x >= 0:
        return x
    if abs(x) < 0.01:
        return 0
    else:
        raise ValueError("Negative values in column 'mm'")    