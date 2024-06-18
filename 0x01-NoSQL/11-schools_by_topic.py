#!/usr/bin/env python3
"""
Module 11-schools_by_topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic
    :param mongo_collection: pymongo collection object
    :param topic: string, the topic searched
    :return: list of schools having the specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
