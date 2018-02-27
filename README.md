# json-2-csv-lambda

Clouformation stack that creates a S3 bucket and a Lambda function that automatically transforms json files to csv when a file is uploaded.It post a message to Slack if there is a problem.

## Getting Started

Instructions to set up and run this project

### Prerequisites

You need aws-cli and bash to deploy using the "deploy" wrapper

### Installing

Clone the repository

```
git clone git@github.com:AntoCard/json-2-csv-lambda.git
```

Install aws-cli

```
pip install awscli
```


## Deployment

From the project base directory run the wrapper script:

```
./deploy -s stackname -l lambda_bucket -b bucket -c channel -t token
```
Where required options are:

```
  -s = Stack name - Name of the Cloudformation stack
  -l = Lambda bucket - S3 bucket name where to store the lambda - Will be created if doesn't exist
  -b = Bucket - S3 bucket where to store csv and json files - Will be created in the stack.
  -c = Channel - Slack channel -  Channel where to post json processing errors
  -t = Token - Slack token - Needed to authenticate against your Slack account

```


## Authors

* **Antonio Cardenes** - *Initial work* - [AntoCard](https://github.com/AntoCard)


## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details

