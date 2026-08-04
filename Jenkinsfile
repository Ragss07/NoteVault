pipeline {
    agent any

    stages {
        stage('Download Docker Compose') {
            steps {
                sh '''
                    echo "Downloading standalone Docker Compose binary..."
                    curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -o docker-compose
                    chmod +x docker-compose
                    
                    # Verify it works
                    ./docker-compose version
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    # Stop any old containers
                    ./docker-compose down --remove-orphans || true
                    
                    # Build and start the app
                    ./docker-compose up -d --build
                    
                    # Show running containers
                    ./docker-compose ps
                '''
            }
        }
    }
}