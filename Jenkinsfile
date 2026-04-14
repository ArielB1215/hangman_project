pipeline {
    agent any
    
    stages {
        stage('Code Checkout') {
            steps {
                git url: 'https://github.com/ArielB1215/hangman_project.git', branch: 'main'
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker run -it arielbm5911/hangman_project:1.0'
            }
        }
        
        // stage('Docker Push') {
        //     steps {
        //         sh 'docker push berezovsky8/test-june:1.0'
        //     }
        // }
    }
}