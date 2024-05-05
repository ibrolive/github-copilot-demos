import azureml.core
import tarfile
import urllib.request
from azureml.core import Workspace, Experiment
from azureml.train.dnn import PyTorch
import os

# Load the Azure Machine Learning workspace
ws = Workspace.from_config()

# Create a new experiment
experiment_name = 'fraud-detection-gnn'
experiment = Experiment(workspace=ws, name=experiment_name)

# Download the compressed .tgz file
url = 'https://public.boxcloud.com/d/1/b1!m524Hx-RIrhHPPEFGuz4Y4gA32fPymIiqr8enAXjTaa_UlTAOVGKzXMp4rll5FZqiCMDC44TObmpgbeyVnGJliFSl2AVniW_yiwiHz60OMBeOujLXhswMz3o9toVm5gJuy7b8aRfXkkJFyIBGFTNn0oD91oGmsKRt88NmX5R165dKsCZyyFvhXcz9mWQChMI2-FH9fA2w_RmyKhruMEcojsooTDhGmtRmvKfjCyLwRsAoFZRPj6J-l6XoBoGzXA4aSjkp-Bf16oLMBsxRpHCBSlSFTrlTDcMKcTaKMD15wKW3U6C7OXU293_VXD5XjySMT4WfQm7lfJPdUxzzNU2foTGE5K3TvNAO1EghxoFwG0KQOBBsVfcFymQJiqZXqBnUUpUNGuqBs7WYvtZVtoVJHcBW-V_1rDWeRu1WQa2f9heL-U22oapep01TvvmrwCe3p_G1Ph75Cho8yeSNFbHmmGSb2sSjvbwFNg8oWFi-mRMhYPyBbFYIZ-C4TO18pk6addL1KKKyTG-6FIgG5NrZ6IuUEIcJVK8uJgfi7g8GH1UXXFI_hhu-Livm2rTiCVAaTsS0nEcCakRnlquv92ZIQF4YdKd_YLB977hKmsZqXIKpMElO_M6DgJK-tB1mkbJO6qLRzk5JdThDdwkXfvKwXdVVWxdQXAdpSZ5Qd-xDTlxx7NQzsGUne2awJ3AUb_5IzlBGQhpevUtH4MBlePpyyI8BerM8xochzUJ6juzjjVsHHyxjX7B-n9hxi65opZPsiHhQae9w8Rwe_01D5pFRnCxIE16z0hQ0xsiOyjs8Jb5WgGryitNF127X2i0Xp_EBTZSXGdK1wqQDxyjt-gQogSj2AJGDHmZhbxMRT7pJjS_Cs2i3mYnPvtkapZBjU5qn5_r72cy5kY_fRH3-zKi5bzIGf_u-qnQugTZti4Ad8daZlNF75BMU26sVs84YhD5Opy4J4PxvCU2WoBetAJj0FzSkjHJ_n2wI76rfkZIUyly215GMQa7YmnrFwSZVkiuhWIEhs815iCe_GEDtelQrXsCNYhT6LrXfRgpp9TWCgWj1PiT8gPSagID8sVsb8a-Dr__R_g0XLc8qg9CFcdcBs95ndmVh1y1i6qow4nWIBatt3vbRt2g82Trbe4i1waUE70S0ZoISjkye-HypthI-0xK8N_LdtyU_06ILrtkIzGzh1NHlUApQ0D_oe8-ClrOvE5jm2Db84YQg1JQaDCj-xsekI2fjOGIAdnSk9VW4GRy3Ox4dxLRi0PuNgmRziOjPWosi28-4JdFW-Yog6gZ_Yr38vUfrMUlfwRlEPth/download'
file_path = './data/transactions.tgz'
urllib.request.urlretrieve(url, file_path)

# Extract the .tgz file
output_folder = './data'
with tarfile.open(file_path, 'r:gz') as tar:
    tar.extractall(output_folder)

# Define the training script
script_params = {
    '--data-folder': './data',
    '--output-folder': './outputs'
}

# Delete the downloaded file
os.remove(file_path)

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