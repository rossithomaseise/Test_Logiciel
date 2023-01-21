docker pull ghcr.io/rossithomaseise/test-logiciel:devops-docker
docker stop $(docker ps | grep ghcr.io/rossithomaseise/test-logiciel:devops-docker | awk '{print $1}' | head -n 1)
docker stop $(docker ps | grep 0.0.0.0:8882 | awk '{print $1}' | head -n 1)
docker run -d -p 8882:8882 ghcr.io/rossithomaseise/test-logiciel:devops-docker
