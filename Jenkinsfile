# Jenkinsfile v2.0 - Multi-App CI/CD Pipeline
# Created by Jenkins Build 2

pipeline {
    agent any
    
    environment {
        DOCKER_HUB_ORG = "vaiz82"
    }
    
    stages {
        stage("📥 Clone Repository") {
            steps {
                cleanWs()
                git branch: "main", url: "https://github.com/vaiz1982/elementary-apps.git"
            }
        }
        
        stage("🚀 Build All Apps") {
            steps {
                sh """
                echo "=== Building All Apps ==="
                
                for app_dir in */; do
                    app=\$(basename "\$app_dir")
                    echo "Building \$app..."
                    cd "\$app_dir"
                    docker build -t \${DOCKER_HUB_ORG}/\$app:build-\${BUILD_NUMBER} .
                    echo "✅ \$app image built"
                    cd ..
                done
                """
            }
        }
        
        stage("📤 Push to Docker Hub") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "docker-hub-credentials",
                    usernameVariable: "DOCKER_USER",
                    passwordVariable: "DOCKER_PAT"
                )]) {
                    sh """
                    echo "\$DOCKER_PAT" | docker login -u "\$DOCKER_USER" --password-stdin
                    echo "Pushing all apps to Docker Hub..."
                    
                    for app_dir in */; do
                        app=\$(basename "\$app_dir")
                        echo "Pushing \$app..."
                        docker push \${DOCKER_HUB_ORG}/\$app:build-\${BUILD_NUMBER}
                    done
                    
                    echo "✅ All apps pushed to Docker Hub!"
                    """
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo "🎉 Multi-app CI/CD pipeline completed successfully!"
        }
    }
}
