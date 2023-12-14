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
	parser.add_argument("metric", type=str,
		choices={"l2", "rmse", "mae"}, help="comparison metric")

	# Create subparser for the sweep and plot commands
	subparser = parser.add_subparsers()

	# Sweep subcommand arguments
	sweep_subparser = subparser.add_parser("sweep", 
		help="performs parameter sweep")
	sweep_subparser.add_argument("start_val", type=float, metavar="start-value",
		help="value to start the sweep at")
	sweep_subparser.add_argument("end_val", type=float, metavar="end-value",
		help="value to end the sweep at")
	sweep_subparser.add_argument("nb_points", metavar="nb-points", type=int,
		 help="number of points for the parameter sweep")
	sweep_subparser.add_argument("--estrus", type=str,  default="all",
		choices={"estrus", "metestrus", "proestrus", "diestrus", "all"}, 
		help="estrus stage")
	
	# Plot subcommand arguments
	plot_subparser = subparser.add_parser("plot",
		help="plots results without doing a parameter sweep")

	# Parse input arguments
	args = parser.parse_args()

	plot_only = False

	# Error check
	try:
		assert(args.start_val < args.end_val)

	except AssertionError:
		sys.stderr.write("Error: start value must be smaller than end value\n")
		exit(1)

	except AttributeError:
		# If the plot command was used
		plot_only = True

	if not plot_only:
		init_states, constants = Roesler2024.initConsts()
		_, _, _, legend_constants = Roesler2024.createLegends()

		# Error check and index retrival
		try:
			_, idx = functions.setParams(constants, legend_constants, 
				args.param, None)

		except IndexError:
			sys.stderr.write(
				"Error: parameter sweep for {} can't be done\n".format(
				args.param))	
			exit(1)

		# Error check
		try:
			assert(args.nb_points > 0)

		except AssertionError:
			sys.stderr.write(
				"Error: the number of points must be greater than 0\n")
			exit(1)
		
		if args.estrus == "all":
			plot_only = True
			estrus_stage = ["proestrus", "estrus", "metestrus", "diestrus"]

		else:
			estrus_stage = [args.estrus]

		for estrus in estrus_stage:
			constants = functions.setEstrusParams(constants, legend_constants, 
				estrus)

			print("{} stage".format(estrus.capitalize()))

			# Original model solution
			print("  Computing original simulation")
			_, orig_states, _ = Roesler2024.solveModel(init_states, constants)

			# Preset the size of the comparison points
			values = np.linspace(args.start_val, args.end_val, args.nb_points)
			comp_points = np.zeros(len(values))

			for i, value in enumerate(values):
				# Run the simulations with different values
				print("    Computing simulation {}".format(i))
				constants[idx] = value
				_, states, _ = Roesler2024.solveModel(init_states, constants)
				comp_points[i] = functions.computeComparison(
					orig_states, states, args.metric)

			print("  Writing results\n")
			output_file = "../res/{}_{}_{}_sweep.pkl".format(
				args.param, estrus, args.metric)

			with open(output_file, 'wb') as handler:
				pickle.dump([comp_points, values], handler)

			init_states, constants = Roesler2024.initConsts() # Reset constants

	# Plot if estrus is all or plot subcommand is used
	if plot_only:
		plots.plotParamSweep(args.param, args.metric)
