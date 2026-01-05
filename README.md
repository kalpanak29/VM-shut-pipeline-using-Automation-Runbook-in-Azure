# VM-shut-pipeline-using-Automation-Runbook-in-Azure

# Overview:
Azure Automation Runbook is used to shut down the virtual machine.
After the shutdown, an ADF pipeline is triggered.
ADF uses its managed identity to fetch the VM power state.
If the VM status is Deallocated, ADF sends a success email notification.
Proper RBAC (Virtual Machine Reader/Contributor) is assigned to ADF to read VM status.

Granted ADF managed identity VM Reader and VM Contributor roles via VM IAM to enable VM status validation.


<img width="679" height="550" alt="image" src="https://github.com/user-attachments/assets/8a7df855-b79e-4f6c-83b4-36eb340ec0c4" />
