echo "pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/rookoe/flask-docker-jenkins.git'
            }
        }

        stage('Verify Network & Running Containers') {
            steps {
                sh '''
                echo "Ensuring network and container setup..."
                docker network create jenkins-network || true
                docker network connect jenkins-network flask-container || true
                '''
            }
        }

        stage('Check Flask API Before Test') {
            steps {
                sh '''
                echo "Checking if Flask container is running..."
                docker ps | grep flask-container || { echo "Flask container not running"; exit 1; }

                echo "Checking Flask API availability..."
                curl -s "http://flask-container:5000/" || { echo "Flask API not reachable"; exit 1; }
                '''
            }
        }

        stage('Test API') {
            steps {
                sh '''
                echo "Running test script..."
                chmod +x /app/test_api.sh
                /app/test_api.sh
                '''
            }
        }
    }

    post {
        always {
            sh 'docker logs flask-container'
            sh 'docker logs jenkins-docker'
        }
        success {
            echo "Pipeline executed successfully! ✅"
        }
        failure {
            echo "Pipeline failed! ❌ Check logs."
        }
    }
}" > Jenkinsfile
