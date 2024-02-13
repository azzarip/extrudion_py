# Copyright 2023 Paride Azzari
#
# Licensed under the MIT License. See LICENSE

def analyzeDirectory(folder_path: str = '.', options = {}):
    '''
    Give a folder path as a relative or absolute path, the script will analyze all the .TAR files found in the directory and return a DataFrame containing the results.
    Leaving returns the Current Working Directory.
    '''
    from .files import TERFolder
    return TERFolder(folder_path).analyze(options)
    



    
def analyzeFile(file, options = {}):
    '''
    Give a filename and a folder as a relative or absolute path, the script will analyze the .TAR files found and return a DataFrame containing the results.
    '''    
    # from .results import Result
    from .files import TERFile

    return TERFile(file).analyze(options)