# DIGIT-Setup

## Basic setup for a single DIGIT tactile sensor
A simple script to setup and test a single [DIGIT](https://digit.ml/) tactile sensor using:  
https://github.com/facebookresearch/digit-interface

### Installation
You can install the digit-interface library via pip:  
`pip install digit-interface`

If you want to create a new Anaconda environment, you can use the **environment.yml** file in this repo:  
`conda env create -f environment.yml`

### Running the Script
Connect your DIGIT sensor via USB and simply run the **single_digit.py** script.  
Follow the instructions/output within the console.

### DIGIT Reference
Mike Lambeta, Po-Wei Chou, Stephen Tian, Brian Yang, Benjamin Maloon, Victoria Rose Most, Dave Stroud, Raymond Santos, Ahmad Byagowi, Gregg Kammerer, Dinesh Jayaraman, Roberto Calandra.  
“DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation.”  
IEEE Robotics and Automation Letters (RA-L), vol. 5, no. 3, pp. 3838–3845, 2020.  
https://doi.org/10.1109/LRA.2020.2977257
