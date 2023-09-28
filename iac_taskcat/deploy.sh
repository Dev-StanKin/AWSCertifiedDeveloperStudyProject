aws cloudformation create-stack --stack-name pipeline-taskcat --capabilities CAPABILITY_NAMED_IAM --disable-rollback --template-body file:////Users/stan/Code/awsSamples/dvac02/iac_taskcat/cf_temp.yml --parameters ParameterKey=GitHubUser,ParameterValue=Datastan ParameterKey=GitHubRepo,ParameterValue=aws-iac

# Sample pipeline https://gist.github.com/kevinkarwaski/00aa01826d88650ae5c0da54ae93f258