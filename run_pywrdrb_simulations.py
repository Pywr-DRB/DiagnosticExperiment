"""
Constructs models and runs pywrdrb simulations using 
multiple different inflow datasets.
"""

import pywrdrb
from pywr.recorders import TablesRecorder

inflow_types = [
    "nhmv10",
    "nhmv10_withObsScaled",
    "nwmv21",
    "nwmv21_withObsScaled",
]

output_dir = "./output_data/"


for inflow in inflow_types:

    print(f"Building model for inflow {inflow}")
    
    #Initialize a model builder
    mb = pywrdrb.ModelBuilder(
        inflow_type=inflow, 
        start_date="1983-10-01",
        end_date="2016-12-31"
        )

    # Make a model
    mb.make_model()

    # Output model.json file
    model_filename = rf"model_data/pywrdrb_model_{inflow}.json"
    mb.write_model(model_filename)

    # Load the model using Model inherited from pywr
    model = pywrdrb.Model.load(model_filename)

    # Output file
    output_filename = rf"{output_dir}drb_output_{inflow}.hdf5"

    ### Add a storage recorder
    

    TablesRecorder(
        model, output_filename, parameters=[p for p in model.parameters if p.name]
    )
    # Run the simulation
    stats = model.run()