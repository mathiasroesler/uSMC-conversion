#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# functions.py: Miscellaneous functions for model comparison
# Author: Mathias Roesler
# Last modified: 12/23

import os
import sys
import numpy as np

# Specific values for different estrus stages
ESTRUS = {
	"proestrus":{"gkv43":1.2, "stim_current":-0.5, "P4":30, "E2":80},
	"estrus":{"gkv43":2.2, "stim_current":-0.5, "P4":14, "E2":45},
	"metestrus":{"gkv43":2.3, "stim_current":-0.25, "P4":25, "E2":43},
	"diestrus":{"gkv43":1.4, "stim_current":-0.5, "P4":15, "E2":70}
	}

# Hard coded values of the P4 dependent constants
# Could probably be optimised
P4_MAP = {
	"P4": 4,
	"P4_max": 6,
	"mod_P4": 25
	}	

# Hard coded values of the E2 dependent constants
# Could probably be optimised
E2_MAP = {
	"E2": 5,
	"E2_max": 7,
	"mod_E2": 24
	}


def setParams(constants, legend_constants, param, value):
	""" Sets the new value for the specified parameter

	Raises an IndexError if the parameter was not found in the list.

	Arguments:
	constants -- list[int], list of constant values.
	legend_constants -- list[str], list of legends for constants.
	param -- str, name of the parameter to change.
	value -- float, new value for the parameter, if None the value
		is not updated.

	Return:
	updated_constants -- list[int], list of updated constant values.
	idx -- int, index of the parameter.

	"""
	found = False
	idx = 0

	if param in E2_MAP.keys():
		# Make sure the E2 modulator is updated
		constants[E2_MAP[param]] = value
		constants[E2_MAP["mod_E2"]] = (
			constants[E2_MAP["E2"]] / constants[E2_MAP["E2_max"]])
		return constants, E2_MAP[param]

	if param in P4_MAP.keys():
		# Make sure the P4 modulator is updated
		constants[P4_MAP[param]] = value
		constants[P4_MAP["mod_P4"]] = (
			constants[P4_MAP["P4"]] / constants[P4_MAP["P4_max"]])
		return constants, P4_MAP[param]

	for i, legend in enumerate(legend_constants):
		words = legend.split(' ')

		if words[0] == param:
			found = True
			idx = i

			if value != None:
				constants[i] = value

			break

	if not found:
		sys.stderr.write("Warning: {} was not found in parameter list\n".format(
			param))	
		raise IndexError
	
	return constants, idx


def setEstrusParams(constants, legend_constants, estrus):
	""" Sets the specific values of the constants for the estrus stage

	Arguments:
	constants -- list[int], list of constant values.
	legend_constants -- list[str], list of legends for constants.
	estrus -- str, estrus stage, 
		{all, proestrus, estrus, metestrus, diestrus}.

	Return:
	updated_constants -- list[int], list of updated constant values.

	"""
	try:
		assert(estrus in ESTRUS.keys())

	except AssertionError:
		sys.stderr.write("Error: the key {} is not valid\n".format(
			estrus))
		exit(1)

	for key in ESTRUS[estrus].keys():
		try:
			constants, _ = setParams(constants, legend_constants, 
				key, ESTRUS[estrus][key])

		except IndexError:
			sys.stderr.write("Warning: {} estrus parameter not set\n".format(
				key))
		
	return constants


def computeL2Norm(v1, v2):
	""" Computes the Euclidean distance between v1 and v2
	
	Arguments:
	v1 -- np.array, first vector.
	v2 -- np.array, second vector. 

	Return:
	l2 -- float, Euclidean distance.

	"""
	return np.linalg.norm(v1-v2)


def computeMAE(v1, v2):
	""" Computes the Mean Absolute Error between v1 and v2

	Arguments:
	v1 -- np.array, first vector.
	v2 -- np.array, second vector. 

	Return:
	mae -- float, mean absolute error.

	"""
	return np.mean(np.abs(v1 - v2))


def computeRMSE(v1, v2):
	""" Computes the Root Mean Squared Error between v1 and v2

	Arguments:
	v1 -- np.array, first vector.
	v2 -- np.array, second vector. 

	Return:
	rmse -- float, root mean square error

	"""
	return np.sqrt(np.mean((v1 - v2)**2))


def computeComparison(v1, v2, metric):
	""" Computes the comparison between v1 and v2 based on the metric

	Arguments:
	v1 -- np.array, first vector.
	v2 -- np.array, second vector. 
	metric -- str, comparison metric, {l2, rmse, mae}

	Return:
	comp_point -- float, comparison point.

	"""
	match metric:
		case "l2":
			return computeL2Norm(v1, v2)

		case "rmse":
			return computeRMSE(v1, v2)

		case "mae":
			return computeMAE(v1, v2)	


