pipeline {

    agent any

    environment {
        DOCKER_HOST = 'unix:///home/lenovo/.docker/desktop/docker.sock'
        IMAGE_NAME = 'task_management_app'
        CONTAINER_NAME = 'task_app'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true

                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p 8000:8000 \
                        ${IMAGE_NAME}:latest
                '''
            }
        }
    }
}