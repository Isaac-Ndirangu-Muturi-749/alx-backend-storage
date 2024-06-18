#!/usr/bin/env python3
"""
Module 102-log_stats
"""

from pymongo import MongoClient


def log_stats(mongo_collection):
    # Count total logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count logs per method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count logs with method=GET and path=/status
    status_check = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Aggregate and sort the top 10 most present IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(mongo_collection.aggregate(pipeline))

    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    log_stats(collection)
