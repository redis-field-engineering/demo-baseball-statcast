terraform {
  required_providers {
    grafana = {
      source = "grafana/grafana"
    }
  }
}

provider "grafana" {
  url  = "http://localhost:3000/"
  auth = "admin:admin"
}

# Got the type by running:
# curl -s -H "Authorization: Basic YWRtaW46YWRtaW4=" http://localhost:3000/api/datasources |jq

resource "grafana_data_source" "simplejson" {
  type       = "grafana-simple-json-datasource"
  name       = "SimpleJson"
  url        = "http://leaderboard:5000/"
  is_default = false
}

resource "grafana_data_source" "redis" {
  type       = "redis-datasource"
  name       = "Redis"
  url        = "redis://redis:6379/"
  is_default = true
}

# Grab dasboard
# Need to be sure and export by clicking on the share item - totally messed up

resource "grafana_dashboard" "pitches" {
  config_json = file("pitches.json")
}

