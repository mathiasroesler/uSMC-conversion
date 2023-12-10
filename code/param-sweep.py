#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# param-sweep.py: Computes a parameters sweep for a cellML export model
# Author: Mathias Roesler
# Last modified: 12/23

import os
import sys
import argparse
import numpy as np
import Roesler2024
import functions

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=
		"Perform a parameter sweep for a given parameter")

	parser.add_argument("param", type=str, help="name of the parameter")
	parser.add_argument("start_val", type=float, metavar="start-value",
		help="value to start the sweep at")
	parser.add_argument("end_val", type=float, metavar="end-value",
		help="value to end the sweep at")
	parser.add_argument("step", type=float, help="step size for the parameter sweep")
	parser.add_argument("--estrus", type=str,  default="estrus",
		choices={"estrus", "metestrus", "proestrus", "diestrus"}, 
		help="estrus stage")

	# Parse input arguments
	args = parser.parse_args()

	try:
		assert(args.start_val < args.end_val)

	except AssertionError:
		sys.stderr.write("Error: start value must be smaller than end value\n")
		exit(1)

	init_states, constants = Roesler2024.initConsts()
	_, _, _, legend_constants = Roesler2024.createLegends()

	constants = functions.setEstrusParams(constants, legend_constants, 
		args.estrus)

	try:
		_, idx = functions.setParams(constants, legend_constants, 
			args.param, None)

	except IndexError:
		sys.stderr.write("Error: parameter sweep for {} can't be done\n".format(
			args.param))	
		exit(1)
	
	orig_voi, _, _ = Roesler2024.solveModel() # Original model solution

	l2_points = np.zeros((np.ceil(( # Create vector for L2 norms
		args.end_val - args.start_val) / args.step)), 1)
