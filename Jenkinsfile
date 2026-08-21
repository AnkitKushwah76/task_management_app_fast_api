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

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
                sh 'docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                        ${IMAGE_NAME}:${BUILD_NUMBER} \
                        pytest
                '''
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
                        ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD deployment successful!'
        }

        failure {
            echo 'CI/CD pipeline failed!'
        }
    }
}