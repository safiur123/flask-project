#!/bin/bash
set -x
DIR_PATH=$(cd $(dirname "${BASH_SOURCE:-$0}") && pwd)
path=$DIR_PATH/$(basename "${BASH_SOURCE:-$0}")
# first setup print-app
cd ${DIR_PATH}/print-hello
if [[ ! $(docker images | grep print-hello-world) ]];then 
/usr/bin/docker build -f Dockerfile -t print-hello-world:latest .
minikube image load print-hello-world
fi
kubectl create -f pod.yaml,service.yaml
# second setup rev-app
cd ${DIR_PATH}/rev-hello
if [[ ! $(docker images | grep rev-hello-world) ]];then
/usr/bin/docker build -f Dockerfile -t rev-hello-world:latest .
minikube image load rev-hello-world
fi
kubectl create -f pod.yaml,service.yaml
cd ${DIR_PATH}



