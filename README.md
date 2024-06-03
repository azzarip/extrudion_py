# Extudion: Python Package for Tensile Testing
Tensile testing, a key method in material science and engineering, assesses a sample's response to controlled tension until failure, aiming to determine its tensile properties. 

These properties, including tensile strength, Young's modulus, and Yield strength, offer insights into material behavior. 

The process of tensile testing involves placing the test specimen in the testing machine and slowly extending it until it fractures. 

The elongation of the gauge section is recorded against the applied force, and this data is used to calculate the strain and stress.

However, the sheer volume of data generated by tensile tests, especially when multiple datasets are produced for each sample, poses a significant challenge in terms of analysis efficiency and accuracy. 

Traditional manual analysis methods often entail tedious and time-consuming tasks, including data filtering, analysis, and parameter estimation, impeding the pace of research and development in materials science. 

## Set up Instructions
Run the following command in the conda/miniconda terminal to install the package:
`pip install extrudion` 

Import the package in your Jupyter project or Python script:
`import extrudion as ex`


## Available Functions:
The Extrudion package comes with one public main class method:
```
   import extrudion as ex
   ex.start(folder_path)
```
This start an automated process where the folder given as a function argument gets analyzed file by file. The initial length and sample area are given as user input.
Additional methods for analyzing a specific file or a specific folder can be called by importing the file:
The `TRAFolder` class for analyzing a full folder, without using the command line input: 
```
    import extrudion.file as ex
    ex.TRAFolder(folder_path).analyze( _
    {'sample_area': sample_area, 'initial_length': initial_length})
```
The `TRAFolder` class for analyzing a single file:
```
    import extrudion.file as ex
    ex.TRAFile(file_path).analyze( _
    {'sample_area': sample_area, 'initial_length': initial_length})
```

## Additional Information

More information on the usage of the package, the reported results and the physics behind the computation can be found in the [Doc File](https://azzarip.github.io/extrudion_py/Docs.pdf) inside the repository.


## Physics Fundamentals

`Stress` = Force['N'] / `sample_thickness` / 10 * 10^3 

returns gives the `stress` in `kPa`

`Strain` = ln( length['mm'] / initial length ['mm'] )

`Young Modulus` = slope of the best line fit for the curve

`Intercept` = the incercet of the previous fit

`Yield Stress and Strain` are the point of intersection for the Young modulus line shifted by 0.02 in the Strain and the data.

## Results

The numerical analysis output is stored in a `csv` file. 

An example is shown in the following table. 

For each file we have max stress and strain coordinates, Young's modulus, and the intercept of the fitting line in the linear regime. 

The intersection coordinates between the shifted line and the stress-strain curve are displayed as yield stress and yield strain. 

| File      | Max Stress (kPa) | Max Strain | Young Modulus (kPa) | Intercept (kPa) | Yield Stress (kPa) | Yield Strain |
|-----------|------------------|------------|----------------------|------------------|--------------------|--------------|
| File.TRA  | 61.73            | 0.14       | 692                  | 0.80             | 50.29              | 0.092        |

### Plot Example
The output of the analysis is as shown in the figure Below. 

The stress-strain curve, depicted in blue, features a blue dot denoting the maximum stress. A fitted line representing Young's modulus is depicted in orange dashed, alongside a 2\% shifted line displayed in dotted green. 

The point of intersection between the stress-strain curve and the green dotted line shows the stress and strain yield.

![image](https://github.com/azzarip/extrudion/assets/116155557/f4cefd4a-50b2-45b2-a603-f0fc15f6e8cc)
