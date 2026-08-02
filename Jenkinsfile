pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Repository cloned successfully'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t notevault:v1 .'
            }
        }

        stage('Run Docker Compose') {
            steps {
                bat 'docker compose up -d'
            }
        }
    }
}