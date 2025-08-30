pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
    	            //sh 'cd /home/george/Desktop/Demo'
                script {
        sh 'python3 /home/cicd2025/test1.py'
            //value=sh(script: 'python3 /home/cicd2025/test1.py', returnStdout: true)
            //echo "value is $value"
            echo "Test"

        }
    	                  
            }
        }
    }
}


