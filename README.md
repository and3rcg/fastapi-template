## FastAPI template project
This is just a template for starting new projects using FastAPI, it supports routers for a more complex file system and has a Dockerfile.
Also, it has a deployment yaml file for the backend.  
You can connect to the backend using port-forward, like this:
`kubectl port-forward deployment/backend 8080:8000`. Then, just access `http://localhost:8000/users` and you should see the API working

## Applying the deployment file
First, make sure you've built the image with the tag `fastapi:v0.1` and loaded it using `kind load docker-image fastapi:v0.1`.  
Then, run `kubectl apply -f deployments/backend-deployment.yaml`

## To be added...
* Shellscripts for easy deployment with Kubernetes
* Support for a PostgreSQL database