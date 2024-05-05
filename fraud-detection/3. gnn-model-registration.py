from azureml.core import Workspace, Model

# Load the Azure Machine Learning workspace
workspace = Workspace.from_config()

# Register the GNN model
model = Model.register(workspace=workspace,
                       model_path='/C:/Projects/github-copilot-demos/fraud-detection/gnn-model.txt',
                       model_name='gnn-model',
                       tags={'framework': 'GNN'},
                       description='Graph Neural Network model for fraud detection')

# Upload the model to the model registry
model.upload(workspace=workspace,
             model_path='/C:/Projects/github-copilot-demos/fraud-detection/gnn-model.txt',
             model_name='gnn-model',
             tags={'framework': 'GNN'},
             description='Graph Neural Network model for fraud detection')