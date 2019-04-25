pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh '''python3 manage.py runserver
'''
        echo 'run'
      }
    }
  }
}