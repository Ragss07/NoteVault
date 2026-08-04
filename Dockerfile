FROM jenkins/jenkins:lts

USER root

RUN apt-get update && 
    apt-get install -y docker.io

RUN curl -SL "https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose

RUN chmod +x /usr/local/bin/docker-compose

# Keep running as root

