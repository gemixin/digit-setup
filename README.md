# DIGIT-Setup

## Overview

**DIGIT-Setup** is a minimal Python script for initialising, testing, and streaming data from a single [DIGIT](https://digit.ml/) tactile sensor using the [digit-interface](https://github.com/facebookresearch/digit-interface) library.

This tool provides a quick way to:

- Connect and configure a DIGIT sensor  
- View a live stream of tactile data  
- Save example frames as image files  
- Print basic sensor information

## Requirements

- **Operating System:** Linux only (DIGIT sensors are supported on Linux only)  
- **Tested Environment:** Ubuntu 22.04, Python 3.13.5  
- **Python Environment:** Regular Python or Anaconda environment

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/gemixin/digit-setup.git
cd digit-setup
```

### 2. Install dependencies

#### Option A: With pip

1. **(Optional) Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate

2. **Install the required package:**  
    ```bash
    pip install digit-interface

#### Option B: With Anaconda

Create a new conda environment using the provided `environment.yml`:

```bash
conda env create -f environment.yml
conda activate digit-env
```

## Running the Script

1. Connect your DIGIT sensor via USB.  
2. Run the script:

```bash
python single_digit.py
```

The script will:

- Automatically connect to the DIGIT sensor  
- Display configuration info  
- Stream a live tactile view  
- Save a few frames locally as `.jpg` images  

Follow the terminal output for step-by-step feedback.

## Known Issues

- **VGA Mode Bug:**  
  The [digit-interface](https://github.com/facebookresearch/digit-interface) library has a known issue with VGA mode producing glitchy output.  
  See [issue #10](https://github.com/facebookresearch/digit-interface/issues/10).  
  ✅ **Recommendation:** Stick to **QVGA mode** for reliable operation.

## Citation

If you use DIGIT or this repo in your research, please cite:

**DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation**  
Mike Lambeta, Po-Wei Chou, Stephen Tian, Brian Yang, Benjamin Maloon, Victoria Rose Most, Dave Stroud, Raymond Santos, Ahmad Byagowi, Gregg Kammerer, Dinesh Jayaraman, Roberto Calandra  
_IEEE Robotics and Automation Letters (RA-L), vol. 5, no. 3, pp. 3838–3845, 2020_  
[https://doi.org/10.1109/LRA.2020.2977257](https://doi.org/10.1109/LRA.2020.2977257)