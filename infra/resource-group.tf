# This file defines an Azure Resource Group resource using the azurerm provider.
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

