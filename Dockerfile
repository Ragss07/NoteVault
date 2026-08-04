//FROM jenkins/jenkins:lts

//USER root

//RUN apt-get update && \
    apt-get install -y docker.io

# Keep running as root

FROM jenkins/jenkins:lts

USER root

# Install Docker CLI and curl
RUN apt-get update && \
    apt-get install -y docker.io curl

# Install Docker Compose V2 plugin so Jenkins can run "docker compose"
RUN mkdir -p /usr/local/lib/docker/cli-plugins && \
    curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -o /usr/local/lib/docker/cli-plugins/docker-compose && \
    chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
