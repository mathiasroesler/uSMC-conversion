#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# param-sweep.py: Computes a parameters sweep for a cellML export model
# Author: Mathias Roesler
# Last modified: 12/23

import os
import sys
import argparse
import pickle
import numpy as np
import Roesler2024
import functions
import plots

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=
		"Perform a parameter sweep for a given parameter")

	parser.add_argument("param", type=str, help="name of the parameter")
	parser.add_argument("start_val", type=float, metavar="start-value",
		help="value to start the sweep at")
	parser.add_argument("end_val", type=float, metavar="end-value",
		help="value to end the sweep at")
	parser.add_argument("step", type=float, help="step size for the parameter sweep")
	parser.add_argument("--estrus", type=str,  default="all",
		choices={"estrus", "metestrus", "proestrus", "diestrus", "all"}, 
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

	try:
		_, idx = functions.setParams(constants, legend_constants, 
			args.param, None)

	except IndexError:
		sys.stderr.write("Error: parameter sweep for {} can't be done\n".format(
			args.param))	
		exit(1)

	if args.estrus == "all":
		estrus_stage = ["proestrus", "estrus", "metestrus", "diestrus"]

	else:
		estrus_stage = [args.estrus]

	for estrus in estrus_stage:
		constants = functions.setEstrusParams(constants, legend_constants, 
			estrus)

		print("{} stage".format(estrus.capitalize()))

		# Original model solution
		print("  Computing original simulation")
		orig_voi, orig_states, _ = Roesler2024.solveModel(init_states, constants)
		nb_points = int(np.round((args.end_val - args.start_val) / args.step)) + 1
		l2_points = np.zeros(nb_points)
		values = np.arange(args.start_val, args.end_val + args.step, args.step)

		for i, value in enumerate(values):
			print("    Computing simulation {}".format(i))
			constants[idx] = value
			_, states, _ = Roesler2024.solveModel(init_states, constants)		
			l2_points[i] = functions.computeL2Norm(orig_states, states)

		print("  Writing results\n")
		output_file = open("../res/{}_{}_sweep.pkl".format(
			args.param, estrus), 'wb')

		pickle.dump([l2_points / max(l2_points), values], output_file)

		output_file.close()

	if args.estrus == "all":
		plots.plotParamSweep(args.param)
