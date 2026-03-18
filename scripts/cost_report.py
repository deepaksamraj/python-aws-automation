#!/usr/bin/env python3
"""
AWS Cost Report Script
Generates a 30-day cost breakdown grouped by service.
"""

import boto3
from datetime import datetime, timedelta
from tabulate import tabulate

def get_cost_report():
    """
    Pull last 30 days AWS cost grouped by service.
    """
    ce = boto3.client("ce")

    end = datetime.utcnow().date()
    start = end - timedelta(days=30)

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start.strftime("%Y-%m-%d"),
            "End": end.strftime("%Y-%m-%d")
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
        GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}]
    )

    results = response["ResultsByTime"][0]["Groups"]

    table = []
    for r in results:
        service = r["Keys"][0]
        amount = float(r["Metrics"]["UnblendedCost"]["Amount"])
        table.append([service, f"${amount:.2f}"])

    print(tabulate(table, headers=["Service", "Cost (30 days)"]))

if __name__ == "__main__":
    get_cost_report()
