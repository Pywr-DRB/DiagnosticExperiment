#!/bin/bash
#SBATCH --job-name=DRB_diagnostic
#SBATCH --output=pywrdrb_diagnostic.out
#SBATCH --error=pywrdrb_diagnostic.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --exclusive

module load python/3.11.5
source venv/bin/activate

### run all simulations
echo Running pywrdrb simulations...
time python3 -W ignore run_pywrdrb_simulations.py 

### analyze results, make figures
echo Analyzing results...
time python3 -W ignore make_figs_diagnostics_experiment.py
