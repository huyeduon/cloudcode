variable "azure_demo04_subs" {
  type = string
}

variable "azure_tenant_id" {
  type = string
}

variable "huyeduon_api_client_id" {
  type = string
}

variable "huyeduon_api_client_secret" {
  type = string
}

variable "rgName" {
  type = string
  default = "tfcloudrg"
}

variable "location" {
  type = string
  default = "eastus"
}