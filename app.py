#!/usr/bin/env python3

import aws_cdk as cdk

from serverless_three_tier_app.serverless_three_tier_app_stack import ServerlessThreeTierAppStack


app = cdk.App()
ServerlessThreeTierAppStack(app, "serverless-three-tier-app")

app.synth()
