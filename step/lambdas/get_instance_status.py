#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copy an image"""
from __future__ import annotations
from typing import Any, Dict, List
import json
import boto3
import os

print("Loading function get_instance_status")

ec2_client = boto3.client("ec2")

# {
#   "original_id": "42283fd1-bbb3-a621-7217-4305c00aaaa",
#   "account": "460535642604",
#   "instance_id": "i-05afe08fb4efe8b40"
# }


def lambda_handler(event: Dict[str, Any], context: Any) -> str:
    print("Received event: " + json.dumps(event, indent=2))

    instance_id: str = event["instance_id"]

    state: str = "unknown"
    resp = ec2_client.describe_instance_status(InstanceIds=[instance_id])
    print(resp)
    for status in resp.get("InstanceStatuses", []):
        # check if running
        state = status["InstanceState"].get("Name")
        if state == "running":
            # check instance
            if status["InstanceStatus"].get("Status") != "ok":
                state = "instance_failed"

            # check system
            if status["SystemStatus"].get("Status") != "ok":
                state = "system_failed"

    return state
