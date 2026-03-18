#!/usr/bin/env python3
"""
EC2 Manager Script
Provides EC2 listing and start/stop automation using tags.
"""
import boto3
import argparse

def list_instances(ec2):
    """
    List all EC2 instances with ID, state, type, and tags.
    """
    for reservation in ec2.describe_instances()["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]
            itype = instance["InstanceType"]
            tags = {t["Key"]: t["Value"] for t in instance.get("Tags", [])}

            print(f"{instance_id} | {state} | {itype} | {tags}")

def manage_instances(ec2, action, tag_key, tag_value):
    """
    Start or stop EC2 instances filtered by tag.
    """
    filters = [
        {"Name": f"tag:{tag_key}", "Values": [tag_value]}
    ]

    instances = ec2.describe_instances(Filters=filters)["Reservations"]

    ids = [
        i["InstanceId"]
        for r in instances
        for i in r["Instances"]
    ]

    if not ids:
        print("No matching instances found.")
        return

    print(f"{action.capitalize()}ing instances: {ids}")

    if action == "start":
        ec2.start_instances(InstanceIds=ids)
    elif action == "stop":
        ec2.stop_instances(InstanceIds=ids)

def main():
    parser = argparse.ArgumentParser(description="EC2 Manager Script")
    parser.add_argument("--list", action="store_true", help="List EC2 instances")
    parser.add_argument("--start", action="store_true", help="Start instances by tag")
    parser.add_argument("--stop", action="store_true", help="Stop instances by tag")
    parser.add_argument("--tag-key", type=str, help="Tag key to filter")
    parser.add_argument("--tag-value", type=str, help="Tag value to filter")

    args = parser.parse_args()

    ec2 = boto3.client("ec2")

    if args.list:
        list_instances(ec2)
    elif args.start or args.stop:
        if not args.tag_key or not args.tag_value:
            print("Tag key and value required.")
            return

        action = "start" if args.start else "stop"
        manage_instances(ec2, action, args.tag_key, args.tag_value)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
