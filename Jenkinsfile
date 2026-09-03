pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build stage – nothing to build'
            }
        }

        stage('Test') {
            steps {
                // Since your agent is Windows, use 'bat' for Windows commands
                bat 'python fac.py'
            }
        }
    }
}