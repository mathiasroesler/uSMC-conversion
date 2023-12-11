#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PNP-comp.py: Compares the results from pregnant and non-pregnant models
# Author: Mathias Roesler
# Last modified: 12/23

import os
import sys
import argparse
import numpy as np
import pickle
import Roesler2024
import Means2022
import functions
import plots

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=
		"Compares the pregnant and non-pregnant models")

	parser.add_argument("metric", type=str, choices={"l2", "rmse", "mae"}, 
		help="comparison metric")
	parser.add_argument("-p", "--plot-only", action="store_true", 
		help="flag used just to plot data")

	args = parser.parse_args()
	init_states_M, constants_M = Means2022.initConsts()
	init_states_R, constants_R = Roesler2024.initConsts()
	_, _, _, legend_constants_R = Roesler2024.createLegends()

	if not args.plot_only:
		print("Computing Means2022 simulation")
		voi_M, states_M, _ = Means2022.solveModel(init_states_M, constants_M)
		comp_points = np.zeros(4) # Comparison points for each stage of estrus

		for i, key in enumerate(functions.ESTRUS.keys()):
			# Set estrus dependant constants
			constants_R = functions.setEstrusParams(constants_R, 
				legend_constants_R, key)

			print("Computing Roesler2024 {} simulation".format(key))

			voi_R, states_R, _ = Roesler2024.solveModel(init_states_R, 
				constants_R)

			match args.metric:
				case "l2":
					comp_points[i] = functions.computeL2Norm(states_M, states_R)

				case "rmse":
					comp_points[i] = functions.computeRMSE(states_M, states_R)

				case "mae":
					comp_points[i] = functions.computeMAE(states_M, states_R)	

		output_file = "../res/{}_comp.pkl".format(args.metric)

		with open(output_file, 'wb') as handler:
			# Pickle data
			pickle.dump(comp_points / max(comp_points), handler)

	# Plot normalized Euclidean distances
	plots.plotPNPComp(args.metric)
