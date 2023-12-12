# Uterine smooth muscle model conversion

# Table of contents
1. [General description](#general)
2. [Requirements](#requirements)
3. [Usage](#usage)
	1. [Setup](#setup)
	2. [Running the code](#code)
		1. [***PNP-comp.py*** script](#pnp)
		2. [***param-sweep.py*** script](#sweep)
4. [Results](#results)

<a id="general"></a>
## General description
This project focuses on comparing results from a pregnant and a non-pregnant uterine smooth muscle cell model and was used to generate results for an EMBC article. 

The project is structure as follows:
```
uSMC-conversion/ (top-level directory)
|-- cells/ (contains the cellML implementations)
|-- code/ (contains the Python code)
|-- res/ (contains simulation outputs)
```

<a id="requirements"></a>
## Requirements
The code was run on Linux Ubuntu 22.04.2 LTS\
The code was developed in [Python](https://www.python.org/) version 3.10.12\
The required packages for Python are found in requirements.txt


<a id="usage"></a>
## Usage

<a id="setup"></a>
### Setup 
First clone the project into *uSMC-conversion* and enter the new directory:
```bash
$ git clone git@github.com/mathiasroesler/uSMC-conversion.git
$ cd uSMC-conversion
```


Next, install the required packages with the following command:
```bash
$ pip3 install -r requirements.txt
```

Finally, create the *res/* folder in the uSMC-conversion folder to store the results in:
```bash
$ mkdir res
```

<a id="code"></a>
### Running the code
There are two scripts that can be run, contained in the *code/* folder: 
* ***PNP-comp.py***
* ***param-sweep.py***

<a id="pnp"></a>
#### ***PNP-comp.py*** script
The ***PNP-comp.py*** compares the simulation outputs of the pregnant and the non-pregnant cell models. The script has one positional argument, metric, that selects the comparison metric to use. Currently, the options are:
* **mae**, for Mean Absolute Error
* **rmse**, for Root Mean Squared Error
* **l2**, for L2-norm

There are also two optional flags:
* **-m**, use to only compute the metric and plot the results
* **-p**, use to only plot the results

**Note:** the script needs to be run once without any flags before being able to use the **-m** and **-p** flags.

When run with no flags, the script will generate two .pkl files in the *res/* folder:
* **sim_output.pkl**, which contains a dictionary with the time steps (in seconds) and the membrane potential values for the pregnant model and each stage of the estrus cycle (in mV)
* **metric_comp.pkl**, where metric is replaced with one of the metrics, which contains the comparison value between the pregnant and non-pregnant model

The **sim_output.pkl** file is required to use the **-m** flag and generate a  **metric_comp.pkl** file. Both of these files are needed to use the **-p** flag. 

**Note:** the estrus stages are always in the same order: proestrus, estrus, metestrus, diestrus.

Run the following command from inside the *code/* folder to view the help message:
```bash
$ python3 PNP-comp.py -h
```


<a id="sweep"></a>
#### ***param-sweep.py*** script
The ***param-sweep.py*** performs a parameter sweep for a given parameter and uses the provided metric to compare the results with the default simulation of the non-pregnant model at the same estrus stage. The script has two positional arguments:
* **param**, the name of the parameter to change, if the specified parameter is not in the parameter list, an error is thrown
* **metric**, the metric to use for comparison (the option can be found in the [***PNP-comp.py***](#pnp) description)

The script has two sub-commands: **sweep** and **plot**.
The **sweep** sub-command computes the results for different values of the given parameter **param**. It has three positional arguments:
* **start-val**, the value at which to start the sweep
* **end-val**, the value at which to end the sweep
* **step**, the size of the increment step for the sweep

The optional flag **--estrus** can be used to compute the sweep for a single estrus stage. The default value is all which computes the sweep for all four stages. 

The **sweep** sub-command will generate .pkl files in the *res/* folder with the following structure **param_stage_metric_sweep.pkl**, where param is replaced with the name of the parameter, stage is replaced with the estrus stage, and metric is replaced with the name of the used metric. The results will be plotted if the **--estrus** flag is set to all.

The **plot** sub-command plots the results without running the parameter sweep again. It can only be called after the **sweep** command has been used and the .pkl files have been generated. 

Run the following command from inside the *code/* folder to view the help message:
```bash
$ python3 param-sweep.py -h
```

An example of the **sweep** command for the gkv43 parameter with the RMSE metric:
```bash
$ python3 param-sweep gkv43 rmse sweep 1.2 2.6 0.14
```

An example of the **plot** command for the gkv43 parameter with the RMSE metric:
```bash
$ python3 param-sweep gkv43 rmse plot
```


<a id="results"></a>
## Results
Below is the plot generated from the [***PNP-comp.py***](#pnp) script using the RMSE metric to compare the simulation outputs of the pregnant model with the non-pregnant model. 
![alt text](fig/PNP_comp.png "Example of the plot from the PNP-comp.py script using the RMSE metric")

Below is the plot generated from the [***param-sweep.py***](#sweep) script for the gkv43 parameter with the L2-norm metric which compares the simulation output of the non-pregnant model with different values of gkv43 with the default value at all stages of the estrus cycle.
![alt text](fig/gkv43_l2_sweep.png "Example of the plot from the PNP-comp.py script using the RMSE metric")