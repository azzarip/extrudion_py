def analyzeDirectory(folder_path: str = '.', cut_off = True, sample_thickness = 10):
    '''
    Give a folder path as a relative or absolute path, the script will analyze all the .TAR files found in the directory and return a DataFrame containing the results.
    Leaving returns the Current Working Directory.
    '''
    from src.files import Folder

    try:
        files = Folder.getList(folder_path)
       
        for file in files:
            analyzeFile(file, folder_path, cut_off, sample_thickness)
            
    except Exception as e:
        print(e)
        
    
def analyzeFile(filename:str, folder: str, cut_off: bool = True, sample_thickness = 10):
    '''
    Give a filename and a folder as a relative or absolute path, the script will analyze the .TAR files found and return a DataFrame containing the results.
    '''
    from src.files import File
    file = File(filename, folder, sample_thickness)
    
    from src.stress import Stress
    Stress(file, cut_off).plot()
    return 
