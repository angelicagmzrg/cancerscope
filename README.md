#SCOPE - Supervised Cancer Origin Prediction using Expression  

|pypi| |build-status| || |docs| |license|
pypi | build-status | docs | license

.. |pypi| image:: https://badge.fury.io/py/cancerscope.svg
   :target: https://pypi.python.org/pypi/cancerscope
   :alt: PyPI Release
   
.. |build-status| image:: https://travis-ci.org/jasgrewal/cancerscope.svg?branch=master
   :target: https://travis-ci.org/jasgrewal/cancerscope
   :alt: Travis CI status

.. |code-health| image:: 
   :target: 
   :alt: Landscape Code Health 
 
.. |license| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT license


A python package that takes the whole transcriptome of a sample as input, and outputs a set of probabilities across 66 different categories (40 tumor types and 26 healthy tissues) that sum to 1.  

You can also train additional models and include them in the ensemble that SCOPE uses (Instructions forthcoming).  

## This release contains   
- [x] Setup Tests    
- [ ] Tutorial   
- [x] License   
- [x] Model files setup   

## Installation   
### Automated Install   
SCOPE can be installed using the command `pip install cancerscope`    

### Installing Python Dependencies  
If you have Anaconda installed, you can set up the environment using  
`>>> conda create --name cscope --file conda_specs-file.txt`  

## Setup and Usage  
To get started with SCOPE, launch a python instance and run:  
`>>> import cancerscope`  

The first time you import cancerscope, the package will attempt to set up a local download of the models needed for prediction. Please be patient as this will take a while (3-10 minutes).  

## Folder descriptors  
All scripts required to run SCOPE are [included](cancerscope).

## License  
cancerscope is distributed under the terms of the MIT license.  

## Issues  
If you encounter any problems, please contact the developer and provide detailed error logs and description [here](https://github.com/jasgrewal/cancerscope/issues).  


