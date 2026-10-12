# Implement Azure Virtual Networking

Source: [Microsoft Learning](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_04-Implement_Virtual_Networking.html)

## Problem

Build two Azure networks, inspect security rules, and verify public and private DNS.

Follow the linked exercise for its requirements. The checks below define what I want to verify in my attempt; extensions are my additions.

## Before starting

Azure subscription with resource-creation permissions; portal and Cloud Shell. DNS and other deployed resources can incur charges. Use a dedicated resource group and remove only this attempt’s resources afterward.

## Checks

- Record the address plan and show that the subnet ranges fit without overlapping.
- Compare the portal-created network with the template deployment; explain the intended inbound and outbound rule precedence.
- Save public DNS lookup output and the private-zone record/link configuration. Configuration alone does not prove private resolution from a VM.
- Record the resource inventory before cleanup and verify the dedicated group is gone.
