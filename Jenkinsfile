properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("close"){
        git "https://github.com/arturolga/devops3006_cours.git"
    }
    stage("show files"){
        sh "ls -l"
    }
}
