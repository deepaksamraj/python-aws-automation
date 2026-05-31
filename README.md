# ☁️ Python AWS Automation Toolkit

> Production-grade AWS automation scripts built with Python, boto3, and argparse — designed for real-world cloud operations, FinOps, and infrastructure management.

---

## 📋 Overview

A collection of three CLI-driven AWS automation tools that handle everyday cloud operations:

| Script | Purpose | Key Feature |
|---|---|---|
| **EC2 Manager** | Instance lifecycle management | Tag-based filtering for start/stop |
| **S3 Cleanup** | Storage cost optimization | Dry-run safety with age-based deletion |
| **Cost Report** | FinOps cost visibility | 30-day spend breakdown by service |

---

## 🚀 Features

### 1. EC2 Manager (`ec2_manager.py`)

- **List** all EC2 instances with ID, state, type, and tags
- **Start/Stop** instances filtered by tag key-value pairs
- Clean CLI interface with argument validation

```bash
# List all instances
python scripts/ec2_manager.py --list

# Stop instances tagged Environment=dev
python scripts/ec2_manager.py --stop --tag-key Environment --tag-value dev

# Start instances tagged Environment=dev
python scripts/ec2_manager.py --start --tag-key Environment --tag-value dev
```

### 2. S3 Cleanup (`s3_cleanup.py`)

- **List** all S3 buckets with total size in MB
- **Identify** objects older than a configurable number of days
- **Dry-run by default** — safe exploration before any deletion
- **`--execute`** flag required for actual deletion (safety-first design)

```bash
# List all buckets and sizes
python scripts/s3_cleanup.py --list

# Preview old objects (dry run)
python scripts/s3_cleanup.py --bucket my-bucket --days 90

# Actually delete objects older than 90 days
python scripts/s3_cleanup.py --bucket my-bucket --days 90 --execute
```

### 3. AWS Cost Report (`cost_report.py`)

- Pulls the last **30 days** of AWS spend via the Cost Explorer API
- Groups costs by **service** for clear visibility
- Outputs a clean, formatted table using `tabulate`

```bash
python scripts/cost_report.py
```

**Sample Output:**
```
Service              Cost (30 days)
-------------------  ----------------
Amazon EC2           $142.53
Amazon S3            $23.17
AWS Lambda           $8.42
Amazon RDS           $67.89
```

---

## 📦 Requirements

- **Python 3.8+**
- **AWS Credentials** configured via `aws configure` or environment variables
- **IAM Permissions** for the services you intend to manage

### Install Dependencies

```bash
pip install -r requirements.txt
```

### IAM Permissions

| Script | Required IAM Actions |
|---|---|
| EC2 Manager | `ec2:DescribeInstances`, `ec2:StartInstances`, `ec2:StopInstances` |
| S3 Cleanup | `s3:ListBucket`, `s3:ListObjectsV2`, `s3:DeleteObject`, `s3:ListAllMyBuckets` |
| Cost Report | `ce:GetCostAndUsage` |

---

## 🏗️ Project Structure

```
python-aws-automation/
├── README.md
├── requirements.txt
└── scripts/
    ├── cost_report.py      # FinOps cost reporting
    ├── ec2_manager.py      # EC2 lifecycle management
    └── s3_cleanup.py       # S3 storage optimization
```

---

## 🛡️ Safety Features

- **Dry-run default** on destructive operations (S3 cleanup)
- **Tag-based filtering** prevents accidental instance management
- **Explicit confirmation** required via `--execute` flag
- **No hardcoded credentials** — uses AWS SDK default credential chain

---

## 📸 Screenshots

> _To be updated_

---

## 🔮 Future Enhancements

- [ ] Add **Lambda support** for serverless function management
- [ ] Implement **CloudWatch log cleanup** for older log groups
- [ ] Add **RDS instance start/stop** scheduling
- [ ] Support **multi-account** via AWS Organizations / STS assume-role
- [ ] Add **JSON/YAML output** format options for CI/CD integration
- [ ] Include **unit tests** with moto for AWS mocking
- [ ] Add **pre-commit hooks** and linting (flake8, black, mypy)
- [ ] Package as a **CLI tool** with `setup.py` / `pyproject.toml`
- [ ] Add **Slack/Teams notifications** for cost alerts and cleanup summaries
- [ ] Support **Terraform state** integration for drift detection

---

## 📝 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a PR or issue.

---

> Built with ☕ and ☁️ by Deepak
