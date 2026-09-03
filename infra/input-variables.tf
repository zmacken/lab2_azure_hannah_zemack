# This file contains input variables for the Terraform configuration.

# resource_group_name: The name of the Azure resource group where resources will be created.
# location: The Azure region where resources will be deployed.
# project_name: The name of the project, used for naming resources.
# acr_name: The name of the Azure Container Registry (ACR) to be created.
# image_tag: The tag for the Docker images to be used in the Azure Container App.
variable "resource_group_name" {
   default = "lab2-awf6che5hvf5ayh7-rg"
   type = string
}

variable "location" {
   default = "swedencentral"
   type = string
}

variable "project_name" {
   default = "lab2"
}

variable "acr_name" {
   default = "lab2"
}

variable "image_tag" {
   default = "latest"
} 