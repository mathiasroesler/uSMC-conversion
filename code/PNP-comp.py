#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PNP-comp.py: Compares the results from pregnant and non-pregnant models
# Author: Mathias Roesler
# Last modified: 12/23

import argparse
import numpy as np
import pickle
import Roesler2024
import Means2023
import functions
import plots


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compares the pregnant and non-pregnant models")

    parser.add_argument("metric", type=str, choices={"l2", "rmse", "mae"},
                        help="comparison metric")
    parser.add_argument("-p", "--plot-only", action="store_true",
                        help="flag used just to plot data")
    parser.add_argument("-m", "--metric-only", action="store_true",
                        help="flag used just to compute metric")

    args = parser.parse_args()
    init_states_M, constants_M = Means2023.initConsts()
    init_states_R, constants_R = Roesler2024.initConsts()
    _, _, _, legend_constants_R = Roesler2024.createLegends()

    sim_output = dict()  # Store simulation output results

    # Output files
    sim_file = "../res/sim_output.pkl"
    comp_file = "../res/{}_comp.pkl".format(args.metric)
    comp_points = np.zeros(4)  # Comparison points for each stage of estrus

    if not args.plot_only and not args.metric_only:
        print("Computing Means2023 simulation")
        _, states_M, _ = Means2023.solveModel(init_states_M, constants_M)

        sim_output["means"] = states_M[0, :]

        for i, key in enumerate(functions.ESTRUS.keys()):
            # Set estrus dependant constants
            constants_R = functions.setEstrusParams(constants_R,
                                                    legend_constants_R, key)

            print("Computing Roesler2024 {} simulation".format(key))

            voi_R, states_R, _ = Roesler2024.solveModel(init_states_R,
                                                        constants_R)

            sim_output[key] = states_R[0, :]  # Membrane potential for plot
            comp_points[i] = functions.computeComparison(
                states_M, states_R, args.metric)

            # Reset the model
            init_states_R, constants_R = Roesler2024.initConsts()

        sim_output["time"] = voi_R / 1000  # Add timesteps in s

        with open(comp_file, 'wb') as handler:
            # Pickle data
            pickle.dump(comp_points, handler)

        with open(sim_file, 'wb') as handler:
            # Pickle data
            pickle.dump(sim_output, handler)

    else:
        with open(sim_file, 'rb') as handler:
            # Unpickle data
            sim_output = pickle.load(handler)

        if args.metric_only:
            # Compute just the metric
            for i, key in enumerate(functions.ESTRUS.keys()):
                comp_points[i] = functions.computeComparison(
                    sim_output["means"], sim_output[key], args.metric)

            with open(comp_file, 'wb') as handler:
                # Pickle data
                pickle.dump(comp_points, handler)

    # Plot normalized Euclidean distances
    plots.plotSimulationOutput(sim_output, args.metric)
