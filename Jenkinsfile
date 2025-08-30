pipeline {
    agent any
    
    stages {
        stage('Run Python Script') {
            steps {
                sh 'ls'
                sh 'pwd'
                //sh 'cd /home/cdci2025'
                sh 'python3 /var/lib/jenkins/workspace/test1.py'
          value=sh(script: 'python3 /var/lib/jenkins/workspace/test1.py', returnStdout: true)
            echo "value is $value"

                
            }
        }
    }
}
