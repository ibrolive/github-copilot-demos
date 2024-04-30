***Github Copilot Prompts***

0. Getting more information
How does an azure app service read an azure sql database through private network traffic?

0. Creating resources in powershell
Using Azure CLI, create azure resources based on the following:
	azure resource group
	One virtual network with subnets named 'web', 'web-integration' and 'data'
	'web' subnet is used for web app private endpoint
	'web-integration' is used for web app virtual network integration
	'data' is used for private endpoint for sql server
	One azure app service plan and web app with private endpoint and virtual network integration to the virtual network
	One azure sql server and azure sql database. Generate admin-password that meets the password policy.
create variables for the virtual network address space and for the three virtual network subnets address spaces
Create unique variable names for app webapp, azure sql server and azure sql database ending with todays date in number format
The az cli commands will be executed in a windows powershell.
please suggest appropriate values for these variables