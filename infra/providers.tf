# This file defines the Terraform provider configuration for Azure Resource Manager (azurerm).
terraform{
    required_providers{
        azurerm = {
            source = "hashicorp/azurerm"
            version = "~> 4.4"
        }
    }
    required_version = ">= 1.13"
}

provider "azurerm" {
    features {}
}