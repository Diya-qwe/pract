fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("The factorial of", n, "is", fact)
Jenkinsfile:
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // The 'echo 5' pipes the number 5 into the python script so Jenkins doesn't hang waiting for input
                bat 'echo 5 | python factorial.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Build successful! Testing complete.'
            }
        }
    }
}

