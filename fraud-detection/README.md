# Fraud Detection Solution

**How to execute**  
Execute the following command on your terminal:  
`python 0.\ executioner.ps1`

**Explanation**
For the purpose of this project, the IaC tool will be: Azure CLI.  
For the purpose of this project, the model training SDK will be: Azure Machine Learning SDK.  

Step 1: gnn-model-registration.py
Using Azure Machine Learning SDK, train the Kaggle fraud detection GNN model.  
Once the model is trained, save it in a format that can be loaded later.  
Also suggest appropriate values for the variables.  

Step 2: ml-workspace.azcli
Using Azure CLI, create an Azure Machine Learning Workspace.  
This workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts to be created later.
Also suggest appropriate values for the variables.  

Step 3: gnn-model-registration.py
Using Azure Machine Learning SDK, register the GNN model.  
Upload the trained model to the model registry in the Azure Machine Learning Workspace.  
Also suggest appropriate values for the variables.  

Step 4: scoring-script.py
Using Azure Machine Learning SDK, create a scoring script.  
This script will use the registered model to make predictions.  
It should load the model, take in an input, and output a prediction.  
Also suggest appropriate values for the variables.  

Step 5: ml-interference-cluster.azcli
Using Azure CLI, create an Azure Machine Learning Inference Cluster.  
This is a scalable cluster of machines that can serve out the model.  
Also suggest appropriate values for the variables.  

Step 6: model-deployment.py
Using Azure Machine Learning SDK, deploy the model as a web service.  
Use the scoring script and registered model to create a web service on the inference cluster.  
Also suggest appropriate values for the variables.  

Step 7: cognitive-search.azcli
Using Azure CLI, create an Azure Cognitive Search instance.  
This service allows the creation of a search index that can provide sophisticated search capabilities for the data.  
Also suggest appropriate values for the variables.  

Step 8:
Using the Azure AI Search REST API, create a data source, index, indexer, and skillset in Azure Cognitive Search.  
The data source connects to the original data.  
The index defines the fields that will be searchable and retrievable.  
The indexer crawls over the data source and populates the index.  
The skillset defines a series of enrichment steps that use AI to extract more information from the data.  

Using the Azure Cognitive Search REST API, add a custom skill to the skillset that calls the GNN model web service.  
This will allow the search index to use the predictions from the GNN model.  

Using the Azure Cognitive Search REST API, run the indexer to populate the search index.  
This will crawl over the data source, use the skillset to enrich the data, and populate the search index.  
