# How to schedule and execute Amazon RDS jobs using AWS Batch and CloudWatch rules

## Introduction
Database administrators and developers traditionally schedule scripts to run against databases using the system cron on the host where the database is running. As a managed database service, Amazon RDS does not provide access to the underlying infrastructure, so if you migrate such workloads from on premises, you must move these jobs. This post provides an alternate way to schedule and run jobs centrally.

AWS Batch is a managed service that abstracts the complexities of provisioning, managing, monitoring, and scaling your computing jobs, and enables you to easily and efficiently run jobs on AWS. Additionally, AWS Batch enables you to build jobs using the language of your choice and deploy it as a Docker container. 

This post demonstrates how to use the combination of AWS Batch and Amazon CloudWatch rules to dynamically provision resources and schedule and run functions or stored procedures on Amazon RDS. 

Please follow the blog post to schedule jobs and test in you account.

![Alt text](Scheduling%20and%20running%20Amazon%20RDS%20jobs%20with%20AWS%20Batch%20and%20Amazon%20CloudWatch%20rules.png?raw=true "Title")


## Prerequisites 
    Before you get started, complete the following prerequisites:

    •	Install Docker Desktop on your machine. 
    •	Set up and configure AWS CLI. For instructions, see Installing the AWS CLI.
    •	Provide the comma-separated list of the default subnets and security groups as input parameters in the AWS CloudFormation template.


## Walkthrough
    The following steps provide a high-level overview of the walkthrough:

    1.	Clone the project from the AWS code samples repository
    2.	Deploy the CloudFormation template to create the required services
    3.	Go to the AWS CloudFormation console and make sure that the resources are created
    4.	Run database scripts and create the required tables and functions
    5.	Build, tag, and push the Docker image to Amazon ECR
    6.	Verify if AWS Batch is running the job successfully based on the CloudWatch rule

    This post also includes optional instructions to manage changes to the job and schedule with AWS CodeCommit and AWS CodeBuild.


## Clone source code from AWS samples 
    Download the files required to set up the environment. See the following code:

    $ git clone https://github.com/aws-samples/aws-batch-rds-job-scheduling
    $ cd aws-batch-rds-job-scheduling


## Deploy the AWS CloudFormation template
    Run the CloudFormation template to provision the required services. See the following code:

    $ aws cloudformation create-stack --stack-name batchjob --template-body file://batchenv-cf.yaml --capabilities CAPABILITY_NAMED_IAM --region us-east-1
    {
        "StackId": "arn:aws:cloudformation:us-east-1:XXXXXXXXXXXXXX:stack/batchjob/73448940-63c5-11ea-918d-1208f0f76cbf"
    }
    
    The template creates the following:

    •	Docker registry to store the Docker image
    •	Job definition to define the Docker image, IAM role, and resource requirements for the job
    •	Queue for jobs until they are ready to run in a compute environment
    •	Compute environment in which AWS Batch manages the compute resources that jobs use
    •	PostgresSQL instance
    •	AWS Secrets Manager with PostgresSQL database login credentials
    •	CloudWatch rule to run the AWS Batch job based on the schedule
    •	Roles with appropriate permission

    The following are ancillary services, which are required only if you choose to manage changes to the job and schedule rule using CodeCommit and CodeBuild:

    •	Repository to store buildspec.yml and src folder 
    •	A CodeBuild project to build, tag, and push Docker images to the registry

    This post includes these instructions after the main walkthrough.

## Testing

    Please follow the blog post to schedule and the test you job execution.


## Code Cleanup

    On the AWS Management Console, navigate to your CloudFormation stack batchjob and delete it. 

    Alternatively, enter the following code in AWS CLI: 

    $ aws cloudformation delete-stack --stack-name batchjob



## License

    This library is licensed under the MIT-0 License. See the LICENSE file.