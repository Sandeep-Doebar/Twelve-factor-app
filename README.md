# Twelve-factor-app
A journey from source (code) to destination (running in k8s). A fun exercise to learn how to deploy a app in k8s with DevOps principles (twelve factors) in mind.

Currently at step: 8

Steps:
1. Create a basic python flask app
2. Create a docker image
3. Add a database functionality to the python app (by adding visitor count to it)
4. Build it in docker and upload it to docker-hub
5. Setup a (local) k8s environment. I eventually settled with rocky linux / Ubuntu and kubeadm installation at it seems to be the most stable choice (tried Minikube, CRC for OpenShift, or microOS + RKE2).
6. Create the manifest files to that the app can run on k8s, with redis having persistent volume.

   
After above steps, i will:
- Add CI/CD pipelines
- Add Prometheus and Grafana
- See if i can add ArgoCD to the stack
- See if i can build security features in the pipeline
- Add Harbor as a private (local) repository)
- Add NeuVector for continous checking of security status
- Add Istio for Service Mesh for immense netwerk security
- Go in to the Cloud and deploy the app with AKS
- Create a bicep file for automatic deployment in AKS
