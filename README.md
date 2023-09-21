Python Package to 

#Instruction
Run the following command in the conda/miniconda terminal to install the package:
`pip install extrudion` 

Import the package in your Jupyter project or Python script:
`import extrudion as ex`


##Available commands:
**Analyze a whole directory**
`ex.analyzeDirectory(folder_path)`

- `folder_path` can be left empty to analyze the current working directory (e.g. `ex.analyzeDirectory()` )
- `folder_path` can be a relative path to a folder within the current working directory (e.g. `ex.analyzeDirectory('data')` )
- `folder_path` can be the absolute path (e.g. `ex.analyzeDirectory('C:\Users\Desktop\extrusion_data')` )

**Analyze a single file**
`ex.analyzeDirectory(*file_path*)`

#Mathematical Formulas

#Input data

The 