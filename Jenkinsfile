pipeline {
    agent any

    environment {
        IMAGE_NAME = "ghcr.io/monteprj/user-registration-app"
        IMAGE_TAG = "latest"
        DOCKER_CREDENTIALS_ID = "ghcr-login"  // lo creiamo tra poco
        KUBE_CONTEXT = "minikube"
        HELM_RELEASE = "user-registration"
        HELM_CHART_PATH = "charts/user-registration-chart"
        NAMESPACE = "application"
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/monteprj/user-registration-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }

        stage('Push to GHCR') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'USERNAME', passwordVariable: 'TOKEN')]) {
                    sh '''
                        echo $TOKEN | docker login ghcr.io -u $USERNAME --password-stdin
                        docker push $IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Helm Upgrade') {
            steps {
                sh '''
                    helm upgrade $HELM_RELEASE $HELM_CHART_PATH \
                        --set image.repository=$IMAGE_NAME \
                        --set image.tag=$IMAGE_TAG \
                        --namespace $NAMESPACE
                '''
            }
        }
    }
}
