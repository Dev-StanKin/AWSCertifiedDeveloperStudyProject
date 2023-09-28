# AWS Certified Developer Study Project

## Overview

This repository contains the code and artifacts developed as part of my study for the AWS Certified Developer - DVAC02 certification. It entails core AWS Services such as; Lambda, S3, DynamoDB, SNS, SQS, API G/W, Kinesis, CloudFormation, SAM, ElastiCache, CodePipeline, ECR/ECS, RDS, IAM and KMS. The language of choice was Python 3.9.

The main focus areas for this project include:

1. Developing code for applications hosted on AWS.
2. Developing code for AWS Lambda functions.
3. Using various data stores in application development.
4. Implementing authentication and/or authorization for applications using AWS services.
5. Managing sensitive data in application code.
6. Preparing application artifacts for deployment to AWS.
7. Testing applications in development environments.
8. Automating deployment testing.
9. Deploying code using AWS CI/CD services.
   10.Troubleshooting and optimization of AWS services and applications.

# Getting Started

To get started with this project, you'll need the following tools installed:

- **Python**: This project is developed in Python. If you don't have Python installed, you can download it from the [Python official website](https://www.python.org/downloads/).

- **Visual Studio Code (VSCode)**: I recommend using VSCode as your code editor. You can download it from the [VSCode official website](https://code.visualstudio.com/download).

Once you have Python and VSCode installed, follow the instructions in the below to clone the repository and set up your environment.

1. Clone this repository:
   git clone https://github.com/Dev-StanKin/AWSCertifiedDeveloperStudyProject.git

2. Set up your AWS credentials if not already configured:

Before you can interact with AWS services, you'll need to set up your AWS credentials. Follow these steps to configure AWS CLI credentials:

Step 1: Sign Up for an AWS Account

If you don't already have an AWS account, you can sign up for one at [AWS Sign-Up](https://aws.amazon.com/). You may need to provide billing information, but some services offer a free tier with limited usage.

Step 2: Install and Configure AWS CLI

1.  Install AWS CLI by following the instructions for your specific operating system: [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

2.  Open your terminal or command prompt and run the following command:

    bash
    aws configure

You will be prompted to enter your AWS Access Key ID, Secret Access Key, AWS region, and default output format. These credentials can be obtained from the AWS Management Console under My Security Credentials.

Step 3: Test Your AWS Configuration

To ensure your AWS CLI is configured correctly, you can run a simple command to list your S3 buckets (assuming you have S3 buckets in your AWS account):
aws s3 ls

Step 4 Installing the AWS SAM CLI

The AWS Serverless Application Model (SAM) CLI is a command-line tool for building, testing, and deploying serverless applications defined by AWS SAM templates. To use it in this project, follow these steps to install the SAM CLI:

      Step 4.1: Prerequisites

      Make sure you have the following prerequisites installed on your development machine:

     - **Python**: SAM CLI requires Python 3.6 or later. You can download Python from the [Python official website](https://www.python.org/downloads/).

     - **Docker**: SAM CLI uses Docker for building and testing Lambda functions locally. Install Docker from the [Docker official website](https://www.docker.com/get-started).

      Step 4.2: Install SAM CLI

     Open your terminal or command prompt and run the following command to install SAM CLI using  `pip`:

       bash
       pip install aws-sam-cli

       # Usage
       You can now use SAM CLI to build, test, and deploy your serverless applications. Refer to the SAM CLI documentation for detailed usage instructions.

       Here are some common SAM CLI commands to get you started:

       sam init: Initialize a new serverless application project.
       sam build: Build your serverless application.
       sam local invoke: Invoke a Lambda function locally.
       sam deploy: Deploy your serverless application to AWS.

3. Install any necessary dependencies:
   Example for Python project with pip
   pip install -r requirements.txt

# Acknowledgments

I would like to acknowledge the CBT Nuggets for offering the AWS DVAC02 IT training course.
CBT Nuggets is a leading provider of IT training courses. They offer a wide range of courses.
I would also like to praise my trainer, Knox Hutchinson, for his excellent teaching skills. He is an experienced and knowledgeable IT trainer. He is able to explain complex concepts in a clear and concise way.
