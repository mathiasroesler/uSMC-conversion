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

LABELS = {
	"l2": "L2-norm",
	"mae": "MAE",
	"rmse": "RMSE"
	}

ESTRUS = ["proestrus", "estrus", "metestrus", "diestrus"]


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
		labels=[estrus.capitalize() for estrus in ESTRUS])

	plt.ylabel("Normalized {}".format(LABELS[metric]))
	plt.show()


def plotParamSweep(param, metric):
	""" Plots the comparison data from different stages of the estrus for
	a given parameter and metric

	Arguments:
	param -- str, name of the parameter to use.
	metric -- str, name of the used metric, {l2, rmse, mae}.

	Return:

	"""
	fig, ax = plt.subplots(dpi=300)

	for i, key in enumerate(functions.ESTRUS.keys()):
		input_file = "../res/{}_{}_{}_sweep.pkl".format(
			param, key, metric)

		with open(input_file, 'rb') as handler:
			# Unpack pickled data
			pickled_data = pickle.load(handler)
			comp_points = pickled_data[0]
			values = pickled_data[1]

		plt.plot(values, comp_points, COLOURS[key])

	plt.legend([estrus.capitalize() for estrus in ESTRUS])
	plt.xlabel(PARAM[param] + r' values (pA.pF$^{-1}$)')
	plt.ylabel("Normalized {}".format(LABELS[metric]))
	plt.show()


def plotSimulationOutput(sim_output, metric):
	""" Plots the output of a non-pregnant simulation and the
	comparison metric

	Arguments:
	sim_output -- dict{str: np.array}, dict containing the simulation
		outputs for each stage in mV and the time stamps in s.
	metric -- str, name of the used metric, {l2, rmse, mae}.

	Return:

	"""
	input_file = "../res/{}_comp.pkl".format(metric)

	with open(input_file, 'rb') as handler:
		comp_points = pickle.load(handler)

	fig, ax = plt.subplots(2, 2, dpi=300, sharex=True, sharey=True)

	cpt = 0
	t = sim_output["time"]

	for i in range(2):
		for j in range(2):
			ax[i, j].plot(t, sim_output[ESTRUS[cpt]], color="black")
			ax[i, j].text(6.5, 0, LABELS[metric] + ' ' +  "{:.2f}".format(
				comp_points[cpt]))
			ax[i, j].set_xlim([0, 10])
			cpt += 1
			
	# Labels are added on Illustrator	
	plt.show()

	fig, ax = plt.subplots(dpi=300)
	plt.plot(t, sim_output["means"], color="black")
	plt.xlim([0, 10])
	plt.show()
