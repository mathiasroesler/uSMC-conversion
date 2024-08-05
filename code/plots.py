#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PNP-comp.py: Compares the results from pregnant and non-pregnant models
# Author: Mathias Roesler
# Last modified: 12/23

import pickle
import numpy as np
import matplotlib.pyplot as plt


COLOURS = {
    "proestrus": '.r',
    "estrus": '.b',
    "metestrus": '.g',
    "diestrus": '.k'
}

PARAM = {
    "gkv43": r'g$_{Kv4.3}$',
    "gcal": r'g$_{CaL}$',
    "gkca": r'g$_{KCa}$',
    "gna": r'g$_{Na}$'
}

LABELS = {
    "l2": "L2-norm",
    "mae": "MAE",
    "rmse": "RMSE"
}

ESTRUS = ["estrus", "proestrus", "metestrus", "diestrus"]


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
    comp_points = []  # Store the results for each stage

    for i, estrus in enumerate(ESTRUS):
        input_file = "../res/{}_{}_{}_sweep.pkl".format(
            param, estrus, metric)

        with open(input_file, 'rb') as handler:
            # Unpack pickled data
            pickled_data = pickle.load(handler)
            comp_points.append(pickled_data[0])
            values = pickled_data[1]  # Assume the values are always the same

    comp_points /= np.max(comp_points)  # Normalise the data

    for i, stage in enumerate(ESTRUS):
        plt.plot(values, comp_points[i], COLOURS[stage], linestyle='-')

    plt.legend([estrus.capitalize() for estrus in ESTRUS])
    plt.xlabel(PARAM[param] + r' values (pA.pF$^{-1}$)')
    plt.ylabel("Normalized {}".format(LABELS[metric]))
    plt.show()


def plotSensitivity(metric):
    """ Plots the results of the sensitivity analysis for a certain metric

    Arguments:
    metric -- str, name of the used metric, {l2, rmse, mae}.

    Return:

    """
    fig, ax = plt.subplots(dpi=300)

    values = np.arange(len(PARAM))  # x-values for plot

    for i, stage in enumerate(ESTRUS):
        comp_points = []  # Store the results for each stage

        for j, param in enumerate(PARAM):
            input_file = "../res/{}_{}_{}_sweep.pkl".format(
                param, stage, metric)

            with open(input_file, 'rb') as handler:
                # Unpack pickled data
                pickled_data = pickle.load(handler)
                comp_points.append(pickled_data[0])

        mean = np.mean(comp_points, axis=1)
        std = np.std(comp_points, axis=1)
        _, caps, bars = ax.errorbar(values+i*0.1, mean, yerr=std,
                                    fmt=COLOURS[stage],
                                    linestyle='', capsize=3)

        # Change cap marker
        caps[0].set_marker('_')
        caps[1].set_marker('_')

    plt.legend([estrus.capitalize() for estrus in ESTRUS])

    # Reset x-axis ticks
    plt.xticks(ticks=values+0.15, labels=PARAM.values())

    plt.xlabel("Parameters")
    plt.ylabel("{} (mV)".format(LABELS[metric]))
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
            ax[i, j].text(6.6, 1, LABELS[metric] + ' ' + "{:.2f}".format(
                comp_points[cpt]) + ' mV', fontsize='small')
            ax[i, j].set_xlim([0, 10])
            ax[i, j].set_title(ESTRUS[cpt])
            cpt += 1

    # Labels are added on Illustrator
    plt.show()

    fig, ax = plt.subplots(dpi=300)
    plt.plot(t, sim_output["means"], color="black")
    plt.xlim([0, 10])
    plt.show()
