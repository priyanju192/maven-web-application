pipeline {
    agent any
    stages {
    
         stage('Trivy scan') {
            steps {
                script {
                     def trivyOutput = sh(script: "trivy fs . -f json -o /var/jenkins_home/reports/trivy-report.json")
                }
            }

          } 
         stage('CSV report') {
            steps {
                script {
                     sh 'python3 conversion.py /var/jenkins_home/reports/trivy-report.json /var/jenkins_home/reports/try.csv'
                }
            }

          } 
        stage('Download reprot') {
            steps {
                script {
                     sh 'ls'
                     sh 'pwd'
                     sh 'cp /var/jenkins_home/reports/try.csv /var/jenkins_home/workspace/test_pipe'
                     sh 'ls'
                }
            }

        } 
    }   
    post {
        always {
            script {
            // ... your post-build steps ...
                emailext ( 
                    subject: '[Jenkins] Build Results for $BUILD_PROJECT - $BUILD_NUMBER',
                    body: 'Build status: $BUILD_STATUS<br><br>More details: <a href="$BUILD_URL">$BUILD_URL</a>',
                    to: 'kspriyanka1192@gmail.com',
                    replyTo: 'priyasrinivas192@gmail.com',
                    attachmentsPattern: 'try.csv'
                )
            }
        }
    }
}
