#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PNP-comp.py: Compares the results from pregnant and non-pregnant models
# Author: Mathias Roesler
# Last modified: 12/23

import os
import sys
import numpy as np
import matplotlib.pyplot as plt


def plotPNPComp(l2_points):
	""" Plots the pregnant and non-pregnant comparison results

	Arguments:
	l2_points -- np.array(float), array of Euclidean norms for each stage
		of the estrus cycle.
	
	Return:

	"""
	fig, ax = plt.subplots(dpi=300)
	
	plt.plot(np.arange(1, 5), l2_points, '.b')

	# Reset x-axis ticks
	plt.xticks(ticks=[1, 2, 3, 4],
		labels=["Proestrus", "Estrus", "Metestrus", "Diestrus"])

	plt.ylabel("L2 norm")
	plt.show()
