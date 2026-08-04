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
                sh 'docker build -t notevault:v1 .'
            }
        }

        stage('Run Docker Compose') {
            steps {
               sh 'docker compose up -d'
            }
        }
    }
}
