import azureml.core
from azureml.core import Workspace, Experiment
from azureml.train.dnn import PyTorch

# Load the Azure Machine Learning workspace
ws = Workspace.from_config()

# Create a new experiment
experiment_name = 'fraud-detection-gnn'
experiment = Experiment(workspace=ws, name=experiment_name)

# Define the training script
script_params = {
    '--data-folder': './data',
    '--output-folder': './outputs'
}

estimator = PyTorch(source_directory='./src',
                    script_params=script_params,
                    compute_target='local',
                    entry_script='train.py',
                    conda_packages=['pytorch', 'torchvision'])

# Submit the experiment for training
run = experiment.submit(estimator)

# Wait for the training run to complete
run.wait_for_completion(show_output=True)

# Save the trained model
model = run.register_model(model_name='fraud-detection-gnn',
                           model_path='outputs/model.pt',
                           tags={'type': 'GNN'})

print("Model saved successfully!")