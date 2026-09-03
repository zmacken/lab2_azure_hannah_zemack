# This file defines a random string resource that generates a random suffix for the Azure Container Registry name. 
# The random string is 6 characters long, does not include special characters, and is in lowercase.
resource "random_string" "suffix" {
  length  = 6
  special = false
  upper  = false
}