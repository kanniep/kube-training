# Getting Started

The [presentation](https://docs.google.com/presentation/d/18Z5TJ-CB0jLsdAnxbfoeA6S_18BuBo3nGko51TvhYKg/edit?usp=sharing)

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

# Run the example

## Locally

Using docker compose

    cd webapp
    docker compose up -d

Go to http://localhost and http://localhost/patients

## Deploy to kubernetes

    cd kube-resources
    kubectl apply -f db-deployment.yml
    kubectl apply -f web-deployment.yml

### Find the pods

    kubectl get pods

### Expose the application

    kubectl apply -f db-service.yml
    kubectl apply -f web-service.yml

### Get node IP

    kubectl get nodes -o wide

### Get the service port

    kubectl get service

### Delete the mess

    kubectl delete deployment kube-demo
    kubectl delete deployment kube-demo-db
    kubectl delete service kube-demo
    kubectl delete service kube-demo-db

## Deploy with Helm

### Deploy

    cd ../chart
    helm install kube-demo .
    helm list

Find the port the same way as before

### Delete the deployment

    helm uninstall kube-demo