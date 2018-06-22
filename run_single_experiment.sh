#!/bin/bash

# NOTE: This file needs to be executable (i.e. chmod +x run_experiment.sh before attempting to run)

DATAFILE=$1
OPTCONFIG=$2
ESNCONFIG=$3
RECONSTRUCTCONFIG=$4
RESERVOIRCONFIG=$5
RUNS=$6

#DATAFILE=./data/NARMA
#OPTCONFIG=ridge_identity
#ESNCONFIG=esnconfig
#RUNS=30

# Tune parameters. Note: the config file for the best parameters are saved at the location in $ESNCONFIG
#python -m scoop -n 8 ./genoptesn.py $DATAFILE $OPTCONFIG $ESNCONFIG $RECONSTRUCTCONFIG $RESERVOIRCONFIG --percent_dim
#python ./genoptesn.py $DATAFILE $OPTCONFIG $ESNCONFIG $RECONSTRUCTCONFIG $RESERVOIRCONFIG --percent_dim

# Run experiments with these parameters
python -m scoop -n 8 ./esn_experiment.py $DATAFILE $ESNCONFIG $RECONSTRUCTCONFIG $RESERVOIRCONFIG $RUNS
#python ./esn_experiment.py $DATAFILE $ESNCONFIG $RECONSTRUCTCONFIG $RESERVOIRCONFIG $RUNS