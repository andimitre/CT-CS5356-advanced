#!/bin/sh

curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

mkdir ${HOME}/.kube
cp config ${HOME}/.kube/config

kubectl run am-flask-app-3 --image=amitre/rest-api:latest --port=5000
