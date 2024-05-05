try {
    # Execute model training script
    python "./1. model-training.py"
}
catch {
    Write-Host "Error executing model training script: $_"
}

try {
    # Execute ml-workspace azcli script
    $mlWorkspaceScript = "./2. ml-workspace.azcli"
    Write-Host "Executing $mlWorkspaceScript"
    az extension add --name azure-cli-ml
    az ml job create --file $mlWorkspaceScript
}
catch {
    Write-Host "Error executing ml-workspace azcli script: $_"
}

try {
    # Execute the Python script for GNN model registration
    python "./3. gnn-model-registration.py"
}
catch {
    Write-Host "Error executing GNN model registration script: $_"
}

try {
    # Execute the scoring-script using Python
    python "./4. scoring-script.py"
}
catch {
    Write-Host "Error executing scoring script: $_"
}

try {
    # Execute ml-interference-cluster azcli script
    $mlInterferenceClusterScript = "./5. ml-interference-cluster.azcli"
    Write-Host "Executing $mlInterferenceClusterScript"
    az extension add --name azure-cli-ml
    az ml job create --file $mlInterferenceClusterScript
}
catch {
    Write-Host "Error executing ml-interference-cluster azcli script: $_"
}

try {
    # Execute the model-deployment script using Python
    python "./6. model-deployment.py"
}
catch {
    Write-Host "Error executing model deployment script: $_"
}

try {
    # Execute ml-cognitive-search azcli script
    $mlCognitiveSearchScript = "./7. cognitive-search.azcli"
    Write-Host "Executing $mlCognitiveSearchScript"
    az extension add --name azure-cli-ml
    az ml job create --file $mlCognitiveSearchScript
}
catch {
    Write-Host "Error executing ml-cognitive-search azcli script: $_"
}
