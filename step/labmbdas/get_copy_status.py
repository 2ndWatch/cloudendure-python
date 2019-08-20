#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Get status of a copy job"""
import json
import boto3

from __future__ import annotations
from typing import Any, Dict, List

print("Loading function get_copy_status")

ec2_client = boto3.client("ec2")

# {
#     "ami"      : "ami-original"
#     "copy_ami" : "ami-copied",
#     "kms_id"   : "GUID",
#     "wait_time": 60
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    print("Received event: " + json.dumps(event, indent=2))

    copy_ami: str = event["copy_ami"]

    ami_state: Dict[str, Any] = ec2_client.describe_images(ImageIds=[copy_ami])

    return ami_state["Images"][0]["State"]
