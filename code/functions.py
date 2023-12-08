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
	"proestrus":{"gkv43":1.3, "stim_current":-0.5, "P4":30, "E2":80},
	"estrus":{"gkv43":2.2, "stim_current":-0.5, "P4":14, "E2":45},
	"metestrus":{"gkv43":2.3, "stim_current":-0.25, "P4":22, "E2":43},
	"diestrus":{"gkv43":1.4, "stim_current":-0.5, "P4":74, "E2":15},
	}


def setEstrusParams(constants, legend_constants, estrus):
	""" Sets the specific values of the constants for the estrus stage

	Arguments:
	constants -- list[int], list of constant values.
	legend_constants -- list[str], list of legends for constants.
	estrus -- str, estrus stage, values are proestrus, estrus, 
		metestrus, diestrus.

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
		found = False
	
		for i, legend in enumerate(legend_constants):
			words = legend.split(' ')

			if words[0] == key:
				constants[i] = ESTRUS[estrus][key]
				found = True
				break

		if not found:
			sys.stderr.write("Warning: {} was not found in parameter list\n".format(
				key))	
		
	return constants
