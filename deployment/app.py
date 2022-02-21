#!/usr/bin/env python3
from deployment.deployment_stack import LoadBalancerStack
from aws_cdk import App
import os


account = os.getenv('CDK_DEFAULT_ACCOUNT')
region = os.getenv('CDK_DEFAULT_REGION')


app = App()
LoadBalancerStack(app,
                  construct_id="LoadBalancerStack",
                  env={
                      'account': account,
                      'region': region
                  }
)
app.synth()
