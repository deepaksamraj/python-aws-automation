# Python AWS Automation

A collection of three production-grade AWS automation scripts using Python, boto3, and argparse. 
These scripts demonstrate cloud automation, FinOps awareness, and operational tooling.

## Features

### 1. EC2 Manager
- List EC2 instances (ID, state, type, tags)
- Start/stop instances filtered by tag
- CLI-driven automation

### 2. S3 Cleanup (FinOps)
- List buckets and total size
- Identify objects older than N days
- Dry-run by default, --execute for real deletion

### 3. AWS Cost Report (FinOps)
- Uses AWS Cost Explorer API
- Last 30 days spend grouped by service
- Outputs a clean, readable table

## Requirements
