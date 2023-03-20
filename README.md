# Getting Started

## kubectl

Follow the guide at
https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

apt dependencies:

    sudo apt-get update
    sudo apt-get install -y ca-certificates curl apt-transport-https

Download the Google Cloud public signing key:

    sudo curl -fsSLo /etc/apt/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg

If you're getting "writting body failed" try create the directory first by:

    sudo mkdir /etc/apt/keyrings

Update apt package index with the new repository and install kubectl:

    sudo apt-get update
    sudo apt-get install -y kubectl

## minikube

    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube

## Setup cluster

Start minikube

    minikube start

Get node

    kubectl get nodes

Should return something like this

    NAME       STATUS   ROLES           AGE   VERSION
    minikube   Ready    control-plane   38s   v1.26.1

# 