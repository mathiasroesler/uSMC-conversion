#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sensitivity.py: Plots the sensitivity analysis results
# Author: Mathias Roesler
# Last modified: 12/23

import argparse
import plots

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Plots the sensitivity analysis results")

    parser.add_argument("metric", type=str,
                        choices={"l2", "rmse", "mae"},
                        help="comparison metric")

    # Parse input arguments
    args = parser.parse_args()

    plots.plotSensitivity(args.metric)
