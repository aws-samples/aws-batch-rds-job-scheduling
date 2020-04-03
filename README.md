# How to schedule and execute Amazon RDS jobs using AWS Batch and CloudWatch rules

## Introduction
Database administrators and developers traditionally schedule the execution of scripts against databases using the system cron on the host where the database is running. As a managed database service, the Amazon Relational Database Service (RDS) does not provide access to the underlying infrastructure, so customers migrating such workloads from on-premises need to move these jobs. The focus of this blog is to provide an alternate mechanism to schedule and execute jobs centrally.

AWS Batch is a managed service that abstracts the complexities of provisioning, managing, monitoring,and scaling your computing jobs, and enables developers to easily and efficiently run jobs on AWS.Additionally, AWS Batch enables developers build jobs using language of their choice and deploy it as a Docker container.

In this blog post, we demonstrate how to use the combination of AWS Batch and CloudWatch rule to
dynamically provision resources, schedule and execute function or stored procedures on Amazon
Relational Database Service (RDS).

Please follow the blog post to schedule jobs and test in you account.

## Prerequisites 
    Make sure that Docker is installed and running on your machine. For instructions, see Docker Desktop and Desktop Enterprise.
    Set up and configure AWS CLI. For steps, see Getting Started (AWS CLI).
    Provide the comma-separated list of the default subnets and security groups as input parameters in the CloudFormation template.

## Walkthrough
    These steps provide a high-level overview followed by detailed steps to create and execute the Batch job.
        1.  Clone the project from AWS code samples repository.
        2.  Deploy the CloudFormation template to create the required services.
        3.  Go to AWS CloudFormation console and make sure that the resources are created.
        4.  Run Database scripts and create the required Tables and Stored Procedure.
        5.  Build, tag, and push Docker image to Elastic container registry.
        6.  Verify if AWS Batch is executing the job successfully based on the CloudWatch rule.

## Clone source code from AWS samples 
    Download the files required to set up the environment. 

    ```
    $ git clone https://github.com/aws-samples/aws-batch-rds-job-scheduling
    $ cd aws-batch-rds-job-scheduling

    ```

## Deploy the AWS CloudFormation template
    Execute the CloudFormation template to provision required services. 

    ```
    $ aws cloudformation create-stack --stack-name batchjob --template-body file://batchenv-cf.yaml --capabilities CAPABILITY_NAMED_IAM --region us-east-1
    {
        "StackId": "arn:aws:cloudformation:us-east-1:XXXXXXXXXXXXXX:stack/batchjob/73448940-63c5-11ea-918d-1208f0f76cbf"
    }
    
    ```

## Testing

    Please follow the blog post to schedule and the test you job execution.


## Code Cleanup

    To clean up, delete the contents of the Amazon S3 bucket and Amazon ECR repository.

    In the AWS Management Console, navigate to your CloudFormation stack “batch-processing-job” and delete it.

    Alternatively, run this command in AWS CLI to delete the job:

    ```
    $ aws cloudformation delete-stack --stack-name batchjob

    ```
## License

    This library is licensed under the MIT-0 License. See the LICENSE file.
