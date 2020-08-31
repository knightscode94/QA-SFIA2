  
pipeline {
    agent any
    stages {
        stage("Build") {
            steps {
		sh 'chmod +x ./scripts/*.sh'
                sh "./scripts/build.sh"
            }
        }
        
        stage("Deploy") {
            steps {
                sh "./scripts/deploy.sh"
            }
        }
    }
}