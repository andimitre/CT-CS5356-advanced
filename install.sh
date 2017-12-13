#!/bin/sh

curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

mkdir ${HOME}/.kube
cp config ${HOME}/.kube/config

kubectl set image deployment/flask-am-app flask-am-app=https://hub.docker.com/r/amitre/rest-api/
