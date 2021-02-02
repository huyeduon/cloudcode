terraform {
  backend "remote" {
      hostname ="app.terraform.io"
      organization="huyeduon"
      workspaces {
        name = "cloudcode"
      }
  }
}

provider "azurerm" {
    subscription_id = var.azure_demo04_subs
    client_id = var.client_idhuyeduon_api_client_id
    client_secret = var.huyeduon_api_client_secret
    tenant_id = var.azure_tenant_id
    features {}
}
