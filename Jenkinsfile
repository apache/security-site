#!groovy
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

pipeline {
    agent {
        // https://cwiki.apache.org/confluence/display/INFRA/Jenkins+node+labels
        label 'git-websites'
    }
   
    environment {
        HUGO_VERSION = '0.111.3'
        HUGO_HASH = 'b382aacb522a470455ab771d0e8296e42488d3ea4e61fe49c11c32ec7fb6ee8b'
        DEPLOY_BRANCH = 'asf-site'
    }

    stages {
        stage('Prepare') {
            steps {
                script {
                    // Capture last commit hash for final commit message
                    env.LAST_SHA = sh(script:'git log -n 1 --pretty=format:\'%H\'', returnStdout: true).trim()

                    // Download Hugo
                    env.HUGO_DIR = sh(script:'mktemp -d', returnStdout: true).trim()
                    sh "mkdir -p ${env.HUGO_DIR}/bin"
                    sh "wget --no-verbose -O ${env.HUGO_DIR}/hugo.tar.gz https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz"
                    // Verify the checksum
                    def hugo_hash = sha256 file: "${env.HUGO_DIR}/hugo.tar.gz"
                    assert hugo_hash == "${HUGO_HASH}"
                    // Unpack Hugo
                    sh "tar -C ${env.HUGO_DIR}/bin -xkf ${env.HUGO_DIR}/hugo.tar.gz"

                    // Setup directory structure for generated content
                    env.TMP_DIR = sh(script:'mktemp -d', returnStdout: true).trim()
                    env.OUT_DIR = "${env.TMP_DIR}/content"
                    sh "mkdir -p ${env.OUT_DIR}"
                    
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh "${HUGO_DIR}/bin/hugo --destination ${env.OUT_DIR}"
                }
            }
        }
        stage('Deploy') {
            when {
                anyOf {
                    branch 'main'
                }
            }
            steps {
                script {
                    // Checkout branch with generated content
                    sh """
                        git checkout ${DEPLOY_BRANCH}
                        git pull origin ${DEPLOY_BRANCH}
                    """
                    
                    // Remove the content of the target branch and replace it with the content of the temp folder
                    sh """
                        git rm -r --ignore-unmatch --cached ${WORKSPACE}/*
                        cp -r ${env.OUT_DIR}/* ${WORKSPACE}
                    """
                    
                    // Commit the changes to the target branch
                    env.COMMIT_MESSAGE = "Updated site from ${BRANCH_NAME} (${env.LAST_SHA})"
                    sh """
                        git add ${WORKSPACE}
                        git commit -m "${env.COMMIT_MESSAGE}" | true
                    """
                    
                    // Push the generated content for deployment
                    sh "git push -u origin ${DEPLOY_BRANCH}"
                }
            }
        }
    }
    
    post {
        always {
            script {
                sh """
                    rm -rf ${env.HUGO_DIR}
                    rm -rf ${env.TMP_DIR}
                """
            }
            deleteDir() /* clean up our workspace */
        }
    }
}
