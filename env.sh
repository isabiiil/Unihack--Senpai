#!/bin/bash


export ASTRA_CLUSTER_ID=aca4e01c-1465-4012-8e84-f282757e54f9
export ASTRA_CLUSTER_REGION=us-east1
export ASTRA_DB_USERNAME=moody
export ASTRA_DB_KEYSPACE=data
export ASTRA_DB_PASSWORD=REPLACE_ME_WITH_PASSWORD

token=$(curl --request POST \
  --url https://$ASTRA_CLUSTER_ID-$ASTRA_CLUSTER_REGION.apps.astra.datastax.com/api/rest/v1/auth \
  --header 'Content-Type: application/json' \
  --data '{"username":"'"$ASTRA_DB_USERNAME"'", "password":"'"$ASTRA_DB_PASSWORD"'"}')

export token