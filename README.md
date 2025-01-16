# Hamilton-et-al.-2024
Runs the experiments from Hamilton et al. (2024)

**NOTE:**
This repository uses the latest stable version of the `pywrdrb` package to run the experiment from Hamilton et al. (2024). Consequently, the results generated using this repository will be slightly different from the exact results in the published paper.  The `pywrdrb` package is under continued development, and thus these results should continue to reflect the evolving quality of the `pywrdrb` functionality. 

You can access the exact code and data used to produce results in Hamilton et al. (2024) through the Zenodo repository:
Andrew Hamilton, Trevor Amestoy, & Marilyn Smith. (2024). Pywr-DRB/Pywr-DRB: Code and Data for Pywr-DRB paper (Hamilton et al, 2024, EMS) (v1.0.2). Zenodo. https://doi.org/10.5281/zenodo.13214630 


## Workflow

On Windows:
```
# Setup virtual env
python -m virtualenv venv
venv/Scripts/activate
pip install git+https://github.com/Pywr-DRB/Pywr-DRB.git@cl_packaging
pip install -r requirements.txt


# run workflow
python ./run_pywrdrb_simulations.py
python ./make_figs_diagnostics_experiment.py
```


On a Linux cluster:
```bash
# Setup virtual env
module load python
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# run workflow
sbatch pywrdrb_run_diagnostics_experiment.sh
```


On Mac (untested):
```

```