# Pipeline 
> Summer 2022 research  pipeline

## Features
- Parse Data
- Create experiments
- Run experiments on different models

## Data Structure class functions
- makeAllExps: makes experiments for each proof in the file
- makeTrials: makes given number of trials for an experiment
- makeMultiExps: makes experiments for multi rule experiments

## Util Functions
- removeCause: removes experiments with cause from the input text file
- parse: parse regular experiment file (Assumption[s] , proof)
- parseMulti: parse multi rule experiment file

## runner class Functions
- run : Run experiments with select models
- runModels: Run experiments with both models
- runTrials: Run multiple trials with different in context examples of one experiment
