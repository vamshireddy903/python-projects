# How to Build and Run the Container Manually

# Pre-requisites:

**Install python**

 Ubuntu/Debian
 
     sudo apt update
     sudo apt install python3 python3-pip -y
     
**Installl pip**
```
sudo apt update
sudo apt install python3-pip -y
```
**Install Flask in your environment:**

    pip3 install flask

# Step 1: Clone the Repository

Open your terminal and run:

    git clone https://github.com/vamshireddy903/python-project.git

Go inside the cloned repo:

    cd python-project

# Step 2: Build the Docker Image

Since the Dockerfile is inside docker/ and named MyDockerfile, run:

     docker build -t python-app -f docker/MyDockerfile .

**Explanation:**

- -t python-cicd-app → Names the Docker image.  
- -f docker/MyDockerfile → Uses the Dockerfile in the docker/ folder.  
- . → Sets the current folder as the build context so Docker can copy necessary files.

# Step 3: Verify the Image

Check the image exists:

     docker images

# Step 4: Run the Container

    docker run -d -p 5000:5000 --name python-cicd-app python-cicd-app

Explanation:

- -d → Run in detached mode.  
- -p 5000:5000 → Map host port 5000 to container port 5000.  
- --name python-cicd-app → Container name.

# Step 5: Verify the Container

    docker ps

Your container should be running.

# Step 6: Access the Application

Open a browser and go to:

    http://<EC2 Public-ip>:5000

# Implementing CI

 **Pre-requisites:**

 1. Docker: https://docs.docker.com/engine/install/ubuntu/  
 2. Java  
 3. Jenkins

    https://www.jenkins.io/doc/book/installing/linux/

Also add jenkins and ubuntu user to docker group

```
sudo usermod -aG docker $USER
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
sudo systemctl restart docker
```
Then logout and login again

# Step 1: Go to Jenkins Dashboard

Open your Jenkins URL in a browser:

    http://<jenkins-server>:8080

# Step 2: Create a New Pipeline Job

1. Click “New Item” on the left menu.  
2. Enter a job name (e.g., Python-App-CI-CD).  
3. Select Pipeline.  
4. Click OK.

# Step 3: Configure Pipeline

- Scroll to Pipeline section.  
- Under Definition, choose Pipeline script from SCM.  
- SCM: Git  
- Repository URL: https://github.com/vamshireddy903/python-project.git  
- Branch: main  
- Credentials: Select Jenkins GitHub credentials (if private repo)  
- Script Path: Jenkinsfile (if your Jenkinsfile is in the repo root)   
- Click Save.  
- Click Build Now to run manually.

# # Step 4: Build Triggers (Optional)

Check GitHub hook trigger for GITScm polling if you want automatic builds via webhook.

- Copy jenkins server url like 

<img width="810" height="257" alt="image" src="https://github.com/user-attachments/assets/e8d096f9-656a-4374-86c3-d6c151ad3488" />

- Go to your github repo -- settings -- webooks -- Add webhook -- paste url in payload 

  <img width="1452" height="875" alt="image" src="https://github.com/user-attachments/assets/d251bd94-270a-4ce1-a6db-42a2c4046c3d" />

Now your jenkins pipeline will trigger when make cahnges to your repository

# Implementing CD

# 1. Create Kubernetes cluster using kind**

  - Install kind

  ```
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-amd64
# For ARM64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

for more: https://kind.sigs.k8s.io/docs/user/quick-start/

# Install kubectl

**Install kubectl binary with curl on Linux **

    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
   
     sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Create k8's cluster

     kubectl create cluster --name demo-cluster

for moreinfo: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

# 2. Install Argocd on cluster

      kubectl create namespace argocd
      kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

  # Port-forward

      kubectl port-forward svc/argocd-server -n argocd 8002:80 --address=0.0.0.0

 # To access UI on browser

        http://<ec2 public-ip>:8002

 - username: admin
 - password:

     to fetech password

        kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d



