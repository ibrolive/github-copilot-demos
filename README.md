# Github Copilot Prompts

1. **Getting more information**  
How does an azure app service read an azure sql database through private network traffic?

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