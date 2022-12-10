
# A 3 Tier Serverless CDK Python project!

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`serverless_three_tier_app_stack`)
which contains

# PRESENTATION LAYER
1. Presentations Layer: Which contains S3 bucket configure for web hosting and attached to Cloudfront distribution

# APPLICATION AND DATABASE LAYER
1. Application Layer: 
    1. API GATEWAY
    2. LAMBDA
    3. SQS Queue

2. DATABASE LAYER
    Contains a a NoSql database. that is a dynamodb. 

# How to use this infrastructure
 1. Runing all the stacks in this aws cdk appplication will create an infrastructure as
    in the ServerlessThreeTierApp diagram provided.

 2. Modify your React based applications to use the api endpoints created by the stack and then   upload the application to the S3 bucket created by the stack.
 You can check this link to see how to host React based app on s3 https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-react-based-single-page-application-to-amazon-s3-and-cloudfront.html
 


The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
