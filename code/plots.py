#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PNP-comp.py: Compares the results from pregnant and non-pregnant models
# Author: Mathias Roesler
# Last modified: 12/23

import os
import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt
import functions

COLOURS = {
	"proestrus": '.-r',
	"estrus": '.-b',
	"metestrus": '.-g',
	"diestrus": '.-k'
	}

PARAM = {
	"gkv43": r'g$_{Kv4.3}$',
	"gcal": r'g$_{CaL}$',
	"gkca": r'g$_{BK}$',
	"gna": r'g$_{Na}$'
	}

def plotPNPComp(metric):
	""" Plots the pregnant and non-pregnant comparison results

	Arguments:
	metric -- str, metric use for comparison to load the correct data.
	
	Return:

	"""
	fig, ax = plt.subplots(dpi=300)

	input_file = "../res/{}_comp.pkl".format(metric)

	with open(input_file, 'rb') as handler:
			# Unpack pickled data
			pickled_data = pickle.load(handler)
	
	plt.plot(np.arange(1, 5), pickled_data, '.b')

	# Reset x-axis ticks
	plt.xticks(ticks=[1, 2, 3, 4],
		labels=["Proestrus", "Estrus", "Metestrus", "Diestrus"])

	plt.ylabel("Normalized {}".upper())
	plt.show()


def plotParamSweep(param):
	""" Plots the L2 data from different stages of the estrus for 
	a given parameter

	Arguments:
	param -- str, name of the parameter to use.

	Return:

	"""
	fig, ax = plt.subplots(dpi=300)

	for i, key in enumerate(functions.ESTRUS.keys()):
		input_file = "../res/{}_{}_sweep.pkl".format(
			param, key)

		with open(input_file, 'rb') as handler:
			# Unpack pickled data
			pickled_data = pickle.load(handler)
			l2_points = pickled_data[0]
			values = pickled_data[1]

		plt.plot(values, l2_points, COLOURS[key])

	plt.legend(["Proestrus", "Estrus", "Metestrus", "Diestrus"])
	plt.xlabel(PARAM[param] + r' values (pA.pF$^{-1}$)')
	plt.ylabel("Normalized L2 norm")
	plt.show()
