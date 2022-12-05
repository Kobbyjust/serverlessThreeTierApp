#!/usr/bin/env python3

import aws_cdk as cdk
#
from presentationlayer.frontend import StaticSitePublicS3
from presentationlayer.site_stack import StaticSiteStack

app = cdk.App()
# ServerlessThreeTierAppStack(app, "serverless-three-tier-app")

props = {
    "namespace": app.node.try_get_context("namespace"),
    "domain_name": app.node.try_get_context("domain_name"),
    "sub_domain_name": app.node.try_get_context("sub_domain_name"),
    "domain_certificate_arn": app.node.try_get_context(
        "domain_certificate_arn"
    ),
    "enable_s3_website_endpoint": app.node.try_get_context(
        "enable_s3_website_endpoint"
    ),
    "origin_custom_header_parameter_name": app.node.try_get_context(
        "origin_custom_header_parameter_name"
    ),
    "hosted_zone_id": app.node.try_get_context("hosted_zone_id"),
    "hosted_zone_name": app.node.try_get_context("hosted_zone_name"),
}

# presentationLayer = StaticSitePublicS3(
#     app, "my s3 and cloudfront" 
# )
StaticSite = StaticSiteStack(
    scope=app,
    construct_id=f"{props['namespace']}-stack",
    props=props,
    description="Static Site using S3, CloudFront and Route53",
)

app.synth()
