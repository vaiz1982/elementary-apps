pipeline {
    agent any
    
    environment {
        DOCKER_HUB_REPO = "vaiz82/elementary-echo-app"
        TEST_PORT = "5001"
    }
    
    stages {
        stage("📥 Clone Repository") {
            steps {
                cleanWs()
                git branch: "main", url: "https://github.com/vaiz1982/elementary-apps.git"
            }
        }
        
        stage("🔨 Build Image") {
            steps {
                dir("echo-app") {
                    sh """
                    docker build -t ${DOCKER_HUB_REPO}:build-${BUILD_NUMBER} .
                    echo "✅ Image built"
                    """
                }
            }
        }
        
        stage("🚀 Test Container") {
            steps {
                sh """
                # Clean up
                docker stop test-container-${BUILD_NUMBER} 2>/dev/null || true
                docker rm test-container-${BUILD_NUMBER} 2>/dev/null || true
                
                echo "Starting container..."
                docker run -d --name test-container-${BUILD_NUMBER} -p ${TEST_PORT}:5000 ${DOCKER_HUB_REPO}:build-${BUILD_NUMBER}
                
                sleep 10
                
                echo "=== Testing POST /echo ==="
                curl -X POST http://localhost:${TEST_PORT}/echo \
                     -H "Content-Type: application/json" \
                     -d '{"test": "jenkins"}' \
                     -w "\nStatus: %{http_code}\n" || true
                
                docker stop test-container-${BUILD_NUMBER}
                docker rm test-container-${BUILD_NUMBER}
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
                    echo "$DOCKER_PAT" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push ${DOCKER_HUB_REPO}:build-${BUILD_NUMBER}
                    echo "✅ Pushed to Docker Hub!"
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
            echo "✅ Pipeline completed successfully!"
        }
    }
}
