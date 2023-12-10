#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PNP-comp.py: Compares the results from pregnant and non-pregnant models
# Author: Mathias Roesler
# Last modified: 12/23

import os
import sys
import numpy as np
import Roesler2024
import Means2022
import functions
import plots

if __name__ == "__main__":
	init_states_M, constants_M = Means2022.initConsts()
	init_states_R, constants_R = Roesler2024.initConsts()
	_, _, _, legend_constants_R = Roesler2024.createLegends()

	print("Computing Means2022 simulation")
	voi_M, states_M, _ = Means2022.solveModel(init_states_M, constants_M)
	l2_points = np.zeros(4) # L2 points for each stage of the estrus

	for i, key in enumerate(functions.ESTRUS.keys()):
		# Set estrus dependant constants
		constants_R = functions.setEstrusParams(constants_R, 
			legend_constants_R, key)

		print("Computing Roesler2024 {} simulation".format(key))

		voi_R, states_R, _ = Roesler2024.solveModel(init_states_R, constants_R)
		l2_points[i] = functions.computeL2Norm(states_M, states_R)


	plots.plotPNPComp(l2_points)
