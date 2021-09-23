YouTube Tutorial:
https://www.youtube.com/watch?v=VDpAnE05Ic4

Jenkin-CI-Pipline Setup
----Step 1: Use below command to create jenkins server in AWS EC2 -----

#!/bin/bash sudo yum -y update sudo amazon-linux-extras install java-openjdk11 -y sudo amazon-linux-extras install epel -y sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key sudo yum install jenkins -y sudo yum install git -y sudo systemctl daemon-reload sudo systemctl start jenkins

----Step 2: Login EC2 Instance to check status of Jenkins Server and generete key pair ----- sudo systemctl status jenkins

ssh-keygen

----Step 3: Retrieve Jenkins init login password and login to install plug in----- sudo cat /var/lib/jenkins/secrets/initialAdminPassword

----Step 4: Add Credential to Jenkin Server -----

----Step 5: Create public key in Github -----

----Step 6: Generate Github Token -----

----Step 7: Add Webook ----- http://:/generic-webhook-trigger/invoke?token=

----Step 8: Install plug in Generic Webhook Trigger -----

----Step 9: Create Pipeline -----

----Step 10: Create Pipeline ----- Post Conetnt Parameters: Variable: ref Expression: $.ref

Optional Filter:

Exp: refs/heads/feature1 Text: $ref

add token

generate script

sh ''' python3 -m venv env source env/bin/activate pip3 install flake8 flake8 src/app.py ''' ----Step 11: VS Code create feature1 branch -----

----Step 12: Observe output of pipeline and fix any issues-----
