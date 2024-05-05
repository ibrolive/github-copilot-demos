# Github Copilot Prompts

1. **Getting more information**  
How do I create a scalable Azure AI search infrastructure that uses Kaggle GNN model?

1. **Implementation**
Using the Azure Machine Learning SDK, train the Kaggle fraud detection GNN model.  
Once the model is trained, save it in a format that can be loaded later.  

Using terraform, create an Azure Machine Learning Workspace.  
This workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts to be created later.

Using the Azure Machine Learning SDK, register the GNN model.  
Upload the trained model to the model registry in the Azure Machine Learning Workspace.

Using the Azure Machine Learning SDK, create a scoring script.  
This script will use the registered model to make predictions.  
It should load the model, take in an input, and output a prediction.

Using terraform, create an Azure Machine Learning Inference Cluster.  
This is a scalable cluster of machines that can serve out the model.  

Using the Azure Machine Learning SDK, deploy the model as a web service.  
Use the scoring script and registered model to create a web service on the inference cluster.

Using terraform, create an Azure Cognitive Search instance.  
This service allows the creation of a search index that can provide sophisticated search capabilities for the data.

Using the Azure Cognitive Search REST API, create a data source, index, indexer, and skillset in Azure Cognitive Search.  
The data source connects to the original data.  
The index defines the fields that will be searchable and retrievable.  
The indexer crawls over the data source and populates the index.  
The skillset defines a series of enrichment steps that use AI to extract more information from the data.  

Using the Azure Cognitive Search REST API, add a custom skill to the skillset that calls the GNN model web service.  
This will allow the search index to use the predictions from the GNN model.  

Using the Azure Cognitive Search REST API, run the indexer to populate the search index.  
This will crawl over the data source, use the skillset to enrich the data, and populate the search index.  

1. **Creating resources in powershell**  
Using Azure CLI, create azure resources based on the following:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Azure resource group  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;One virtual network with subnets named 'web', 'web-integration' and 'data'  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'web' subnet is used for web app private endpoint  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'web-integration' is used for web app virtual network integration  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'data' is used for private endpoint for sql server  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;One azure app service plan and web app with private endpoint and virtual network integration to the virtual network  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;One azure sql server and azure sql database. Generate admin-password that meets the password policy  
Create variables for the virtual network address space and for the three virtual network subnets address spaces  
Create unique variable names for app webapp, azure sql server and azure sql database ending with todays date in number format  
The az cli command will be executed in a windows powershell  
Please suggest appropriate values for these variables  

