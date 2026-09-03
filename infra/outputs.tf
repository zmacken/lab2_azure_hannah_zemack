# Output values for the Azure resources

# acr_login_server: The login server URL of the Azure Container Registry (ACR).
# acr_name: The name of the Azure Container Registry (ACR).
# container_app_name: The name of the Azure Container App for the API.
# resource_group_name: The name of the Azure resource group where resources are created.
output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}

output "acr_name" {
  value = azurerm_container_registry.acr.name
}

output "container_app_name" {
  value = azurerm_container_app.api.name
}

output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}