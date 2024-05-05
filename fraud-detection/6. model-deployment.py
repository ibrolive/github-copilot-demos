from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.environment import Environment
from azureml.core.conda_dependencies import CondaDependencies

# Load the Azure ML workspace
workspace = Workspace.from_config()

# Get the registered model
model = Model(workspace, 'gnn-model')

# Create a scoring script
scoring_script = 'scoring-script.py'
with open(scoring_script, 'w') as file:
    file.write('''
import json
import numpy as np
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('gnn-model')
    model = load_model(model_path)

def run(raw_data):
    data = json.loads(raw_data)['data']
    predictions = model.predict(data)
    return json.dumps(predictions.tolist())
''')

# Create an environment
env = Environment('deploy-env')
conda_dep = CondaDependencies()
conda_dep.add_pip_package('azureml-defaults')
env.python.conda_dependencies = conda_dep

# Deploy the web service
service_name = 'myModelWebService'
inference_config = InferenceConfig(entry_script=scoring_script, environment=env)
deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)
service = Model.deploy(workspace, service_name, [model], inference_config, deployment_config)
service.wait_for_deployment(show_output=True)