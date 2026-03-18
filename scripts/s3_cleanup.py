#!/usr/bin/env python3
"""
S3 Cleanup Script
Lists bucket sizes and deletes old objects (FinOps-friendly).
"""
import boto3
import argparse
from datetime import datetime, timezone, timedelta

def list_buckets(s3):
    """
    List S3 buckets and their total size in bytes.
    """
    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:
        name = bucket["Name"]
        size = 0

        for obj in s3.list_objects_v2(Bucket=name).get("Contents", []):
            size += obj["Size"]

        print(f"{name}: {size / (1024*1024):.2f} MB")

def cleanup_old_objects(s3, bucket, days, execute):
    """
    Delete objects older than N days. Dry-run unless --execute is passed.
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    response = s3.list_objects_v2(Bucket=bucket)

    if "Contents" not in response:
        print("Bucket is empty.")
        return

    for obj in response["Contents"]:
        key = obj["Key"]
        last_modified = obj["LastModified"]

        if last_modified < cutoff:
            if execute:
                print(f"Deleting {key}")
                s3.delete_object(Bucket=bucket, Key=key)
            else:
                print(f"[DRY RUN] Would delete {key}")

def main():
    parser = argparse.ArgumentParser(description="S3 Cleanup Script")
    parser.add_argument("--list", action="store_true", help="List buckets and sizes")
    parser.add_argument("--bucket", type=str, help="Bucket to clean")
    parser.add_argument("--days", type=int, help="Delete objects older than N days")
    parser.add_argument("--execute", action="store_true", help="Actually delete objects")

    args = parser.parse_args()
    s3 = boto3.client("s3")

    if args.list:
        list_buckets(s3)
    elif args.bucket and args.days:
        cleanup_old_objects(s3, args.bucket, args.days, args.execute)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
